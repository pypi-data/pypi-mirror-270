"""Test page requests.

SPDX-FileCopyrightText: © 2020 Brian S. Stephan <bss@incorporeal.org>
SPDX-License-Identifier: AGPL-3.0-or-later
"""
import re
from unittest.mock import patch


def test_page_that_exists(client):
    """Test that the app can serve a basic file at the index."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'<h1 id="test-index">test index</h1>' in response.data


def test_direct_file_that_exists(client):
    """Test that the app can serve a basic file at the index."""
    response = client.get('/foo.txt')
    assert response.status_code == 200
    assert b'test file' in response.data


def test_page_that_doesnt_exist(client):
    """Test that the app returns 404 for nonsense requests and they use my error page."""
    response = client.get('/ohuesthaoeusth')
    assert response.status_code == 404
    assert b'<b><tt>/ohuesthaoeusth</tt></b> does not seem to exist' in response.data
    # test the contact email config
    assert b'admin@example.com' in response.data


def test_files_outside_pages_do_not_get_served(client):
    """Test that page pathing doesn't break out of the instance/pages/ dir, and the error uses my error page."""
    response = client.get('/../unreachable')
    assert response.status_code == 400
    assert b'You\'re doing something you\'re not supposed to. Stop it?' in response.data


def test_internal_server_error_serves_error_page(client):
    """Test that various exceptions serve up the 500 page."""
    response = client.get('/actually-a-png')
    assert response.status_code == 500
    assert b'INTERNAL SERVER ERROR' in response.data
    # test the contact email config
    assert b'admin@example.com' in response.data


def test_oserror_is_500(client, app):
    """Test that an OSError raises as a 500."""
    with app.test_request_context():
        with patch('flask.current_app.open_instance_resource', side_effect=OSError):
            response = client.get('/')
            assert response.status_code == 500
            assert b'INTERNAL SERVER ERROR' in response.data


def test_unsupported_file_type_is_500(client, app):
    """Test a coding condition mishap raises as a 500."""
    with app.test_request_context():
        with patch('incorporealcms.pages.request_path_to_instance_resource_path', return_value=('foo', 'bar')):
            response = client.get('/')
            assert response.status_code == 500
            assert b'INTERNAL SERVER ERROR' in response.data


def test_weird_paths_do_not_get_served(client):
    """Test that we clean up requests as desired."""
    response = client.get('/../../')
    assert response.status_code == 400


def test_page_with_title_metadata(client):
    """Test that a page with title metadata has its title written."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'<title>Index - example.com</title>' in response.data


def test_page_without_title_metadata(client):
    """Test that a page without title metadata gets the default title."""
    response = client.get('/no-title')
    assert response.status_code == 200
    assert b'<title>/no-title - example.com</title>' in response.data


def test_page_in_subdir_without_title_metadata(client):
    """Test that the title-less page display is as expected."""
    response = client.get('/subdir//page-no-title')
    assert response.status_code == 200
    assert b'<title>/subdir/page-no-title - example.com</title>' in response.data


def test_page_with_card_metadata(client):
    """Test that a page with opengraph metadata."""
    response = client.get('/more-metadata')
    assert response.status_code == 200
    assert b'<meta property="og:title" content="title for the page - example.com">' in response.data
    assert b'<meta property="og:description" content="description of this page made even longer">' in response.data
    assert b'<meta property="og:image" content="http://buh.com/test.img">' in response.data


def test_page_with_card_title_even_when_no_metadata(client):
    """Test that a page without metadata still has a card with the derived title."""
    response = client.get('/no-title')
    assert response.status_code == 200
    assert b'<meta property="og:title" content="/no-title - example.com">' in response.data
    assert b'<meta property="og:description"' not in response.data
    assert b'<meta property="og:image"' not in response.data


def test_page_with_forced_empty_title_just_shows_suffix(client):
    """Test that if a page specifies a blank Title meta tag explicitly, only the suffix is used in the title."""
    response = client.get('/forced-no-title')
    assert response.status_code == 200
    assert b'<title>example.com</title>' in response.data


def test_page_with_redirect_meta_url_redirects(client):
    """Test that if a page specifies a URL to redirect to, that the site serves up a 301."""
    response = client.get('/redirect')
    assert response.status_code == 301
    assert response.location == 'http://www.google.com/'


def test_page_has_modified_timestamp(client):
    """Test that pages have modified timestamps in them."""
    response = client.get('/')
    assert response.status_code == 200
    assert re.search(r'Last modified: ....-..-.. ..:..:.. ...', response.data.decode()) is not None


def test_that_page_request_redirects_to_directory(client):
    """Test that a request to /foo reirects to /foo/, if foo is a directory.

    This might be useful in cases where a formerly page-only page has been
    converted to a directory with subpages.
    """
    response = client.get('/subdir')
    assert response.status_code == 301
    assert response.location == '/subdir/'


def test_that_request_to_symlink_redirects_markdown(client):
    """Test that a request to /foo redirects to /what-foo-points-at."""
    response = client.get('/symlink-to-no-title')
    assert response.status_code == 301
    assert response.location == '/no-title'


def test_that_request_to_symlink_redirects_file(client):
    """Test that a request to /foo.txt redirects to /what-foo-points-at.txt."""
    response = client.get('/symlink-to-foo.txt')
    assert response.status_code == 301
    assert response.location == '/foo.txt'


def test_that_request_to_symlink_redirects_directory(client):
    """Test that a request to /foo/ redirects to /what-foo-points-at/."""
    response = client.get('/symlink-to-subdir/')
    assert response.status_code == 301
    assert response.location == '/subdir'
    # sadly, this location also redirects
    response = client.get('/subdir')
    assert response.status_code == 301
    assert response.location == '/subdir/'
    # but we do get there
    response = client.get('/subdir/')
    assert response.status_code == 200


def test_that_request_to_symlink_redirects_subdirectory(client):
    """Test that a request to /foo/bar redirects to /what-foo-points-at/bar."""
    response = client.get('/symlink-to-subdir/page-no-title')
    assert response.status_code == 301
    assert response.location == '/subdir/page-no-title'
    response = client.get('/subdir/page-no-title')
    assert response.status_code == 200


def test_that_dir_request_does_not_redirect(client):
    """Test that a request to /foo/ serves the index page, if foo is a directory."""
    response = client.get('/subdir/')
    assert response.status_code == 200
    assert b'another page' in response.data


def test_setting_selected_style_includes_cookie(client):
    """Test that a request with style=foo sets the cookie and renders appropriately."""
    response = client.get('/')
    style_cookie = client.get_cookie('user-style')
    assert style_cookie is None

    response = client.get('/?style=light')
    style_cookie = client.get_cookie('user-style')
    assert response.status_code == 200
    assert b'/static/css/light.css' in response.data
    assert b'/static/css/dark.css' not in response.data
    assert style_cookie.value == 'light'

    response = client.get('/?style=dark')
    style_cookie = client.get_cookie('user-style')
    assert response.status_code == 200
    assert b'/static/css/dark.css' in response.data
    assert b'/static/css/light.css' not in response.data
    assert style_cookie.value == 'dark'


def test_pages_can_supply_alternate_templates(client):
    """Test that pages can supply templates other than the default."""
    response = client.get('/')
    assert b'class="site-wrap site-wrap-normal-width"' in response.data
    assert b'class="site-wrap site-wrap-double-width"' not in response.data
    response = client.get('/custom-template')
    assert b'class="site-wrap site-wrap-normal-width"' not in response.data
    assert b'class="site-wrap site-wrap-double-width"' in response.data


def test_extra_footer_per_page(client):
    """Test that we don't include the extra-footer if there isn't one (or do if there is)."""
    response = client.get('/')
    assert b'<div class="extra-footer">' not in response.data
    response = client.get('/index-but-with-footer')
    assert b'<div class="extra-footer"><i>ooo <a href="a">a</a></i>' in response.data


def test_serving_static_files(client):
    """Test the usage of send_from_directory to serve extra static files."""
    response = client.get('/custom-static/css/warm.css')
    assert response.status_code == 200

    # can't serve directories, just files
    response = client.get('/custom-static/')
    assert response.status_code == 404
    response = client.get('/custom-static/css/')
    assert response.status_code == 404
    response = client.get('/custom-static/css')
    assert response.status_code == 404

    # can't serve files that don't exist or bad paths
    response = client.get('/custom-static/css/cold.css')
    assert response.status_code == 404
    response = client.get('/custom-static/css/../../unreachable.md')
    assert response.status_code == 404

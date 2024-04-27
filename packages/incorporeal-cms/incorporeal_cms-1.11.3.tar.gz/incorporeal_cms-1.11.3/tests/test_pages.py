"""Unit test helper methods.

SPDX-FileCopyrightText: © 2020 Brian S. Stephan <bss@incorporeal.org>
SPDX-License-Identifier: AGPL-3.0-or-later
"""
import os

import pytest
from werkzeug.http import dump_cookie

from incorporealcms import create_app
from incorporealcms.pages import (generate_parent_navs, instance_resource_path_to_request_path, render,
                                  request_path_to_breadcrumb_display, request_path_to_instance_resource_path)

HERE = os.path.dirname(os.path.abspath(__file__))


def test_generate_page_navs_index(app):
    """Test that the index page has navs to the root (itself)."""
    with app.app_context():
        assert generate_parent_navs('pages/index.md') == [('example.com', '/')]


def test_generate_page_navs_subdir_index(app):
    """Test that dir pages have navs to the root and themselves."""
    with app.app_context():
        assert generate_parent_navs('pages/subdir/index.md') == [('example.com', '/'), ('subdir', '/subdir/')]


def test_generate_page_navs_subdir_real_page(app):
    """Test that real pages have navs to the root, their parent, and themselves."""
    with app.app_context():
        assert generate_parent_navs('pages/subdir/page.md') == [('example.com', '/'), ('subdir', '/subdir/'),
                                                                ('Page', '/subdir/page')]


def test_generate_page_navs_subdir_with_title_parsing_real_page(app):
    """Test that title metadata is used in the nav text."""
    with app.app_context():
        assert generate_parent_navs('pages/subdir-with-title/page.md') == [
            ('example.com', '/'),
            ('SUB!', '/subdir-with-title/'),
            ('page', '/subdir-with-title/page')
        ]


def test_generate_page_navs_subdir_with_no_index(app):
    """Test that breadcrumbs still generate even if a subdir doesn't have an index.md."""
    with app.app_context():
        assert generate_parent_navs('pages/no-index-dir/page.md') == [
            ('example.com', '/'),
            ('/no-index-dir/', '/no-index-dir/'),
            ('page', '/no-index-dir/page')
        ]


def test_render_with_user_dark_theme(app):
    """Test that a request with the dark theme selected renders the dark theme."""
    cookie = dump_cookie("user-style", 'dark')
    with app.test_request_context(headers={'COOKIE': cookie}):
        assert b'/static/css/dark.css' in render('base.html').data
        assert b'/static/css/light.css' not in render('base.html').data


def test_render_with_user_light_theme(app):
    """Test that a request with the light theme selected renders the light theme."""
    with app.test_request_context():
        assert b'/static/css/light.css' in render('base.html').data
        assert b'/static/css/dark.css' not in render('base.html').data


def test_render_with_no_user_theme(app):
    """Test that a request with no theme set renders the light theme."""
    with app.test_request_context():
        assert b'/static/css/light.css' in render('base.html').data
        assert b'/static/css/dark.css' not in render('base.html').data


def test_render_with_theme_defaults_affects_html(app):
    """Test that the base themes are all that's presented in the HTML."""
    # test we can remove stuff from the default
    with app.test_request_context():
        assert b'?style=light' in render('base.html').data
        assert b'?style=dark' in render('base.html').data
        assert b'?style=plain' in render('base.html').data


def test_render_with_theme_overrides_affects_html(app):
    """Test that the overridden themes are presented in the HTML."""
    # test we can remove stuff from the default
    restyled_app = create_app(instance_path=os.path.join(HERE, 'instance'),
                              test_config={'PAGE_STYLES': {'light': '/static/css/light.css'}})
    with restyled_app.test_request_context():
        assert b'?style=light' in render('base.html').data
        assert b'?style=dark' not in render('base.html').data
        assert b'?style=plain' not in render('base.html').data

    # test that we can add new stuff too/instead
    restyled_app = create_app(instance_path=os.path.join(HERE, 'instance'),
                              test_config={'PAGE_STYLES': {'cool': '/static/css/cool.css',
                                                           'warm': '/static/css/warm.css'},
                                           'DEFAULT_PAGE_STYLE': 'warm'})
    with restyled_app.test_request_context():
        assert b'?style=cool' in render('base.html').data
        assert b'?style=warm' in render('base.html').data


def test_render_with_theme_overrides(app):
    """Test that the loaded themes can be overridden from the default."""
    cookie = dump_cookie("user-style", 'cool')
    restyled_app = create_app(instance_path=os.path.join(HERE, 'instance'),
                              test_config={'PAGE_STYLES': {'cool': '/static/css/cool.css',
                                                           'warm': '/static/css/warm.css'}})
    with restyled_app.test_request_context(headers={'COOKIE': cookie}):
        assert b'/static/css/cool.css' in render('base.html').data
        assert b'/static/css/warm.css' not in render('base.html').data


def test_render_with_theme_overrides_not_found_is_default(app):
    """Test that theme overrides work, and if a requested theme doesn't exist, the default is loaded."""
    cookie = dump_cookie("user-style", 'nonexistent')
    restyled_app = create_app(instance_path=os.path.join(HERE, 'instance'),
                              test_config={'PAGE_STYLES': {'cool': '/static/css/cool.css',
                                                           'warm': '/static/css/warm.css'},
                                           'DEFAULT_PAGE_STYLE': 'warm'})
    with restyled_app.test_request_context(headers={'COOKIE': cookie}):
        assert b'/static/css/warm.css' in render('base.html').data
        assert b'/static/css/nonexistent.css' not in render('base.html').data


def test_request_path_to_instance_resource_path(app):
    """Test a normal URL request is transformed into the file path."""
    with app.test_request_context():
        assert request_path_to_instance_resource_path('index') == ('pages/index.md', 'markdown')


def test_request_path_to_instance_resource_path_direct_file(app):
    """Test a normal URL request is transformed into the file path."""
    with app.test_request_context():
        assert request_path_to_instance_resource_path('no-title') == ('pages/no-title.md', 'markdown')


def test_request_path_to_instance_resource_path_in_subdir(app):
    """Test a normal URL request is transformed into the file path."""
    with app.test_request_context():
        assert request_path_to_instance_resource_path('subdir/page') == ('pages/subdir/page.md', 'markdown')


def test_request_path_to_instance_resource_path_subdir_index(app):
    """Test a normal URL request is transformed into the file path."""
    with app.test_request_context():
        assert request_path_to_instance_resource_path('subdir/') == ('pages/subdir/index.md', 'markdown')


def test_request_path_to_instance_resource_path_relatives_walked(app):
    """Test a normal URL request is transformed into the file path."""
    with app.test_request_context():
        assert (request_path_to_instance_resource_path('subdir/more-subdir/../../more-metadata') ==
                ('pages/more-metadata.md', 'markdown'))


def test_request_path_to_instance_resource_path_relatives_walked_indexes_work_too(app):
    """Test a normal URL request is transformed into the file path."""
    with app.test_request_context():
        assert request_path_to_instance_resource_path('subdir/more-subdir/../../') == ('pages/index.md', 'markdown')


def test_request_path_to_instance_resource_path_relatives_walked_into_subdirs_also_fine(app):
    """Test a normal URL request is transformed into the file path."""
    with app.test_request_context():
        assert (request_path_to_instance_resource_path('subdir/more-subdir/../../subdir/page') ==
                ('pages/subdir/page.md', 'markdown'))


def test_request_path_to_instance_resource_path_permission_error_on_ref_above_pages(app):
    """Test that attempts to get above the base dir ("/../../foo") fail."""
    with app.test_request_context():
        with pytest.raises(PermissionError):
            assert request_path_to_instance_resource_path('../unreachable')


def test_request_path_to_instance_resource_path_isadirectory_on_file_like_req_for_dir(app):
    """Test that a request for e.g. '/foo' when foo is a dir indicate to redirect."""
    with app.test_request_context():
        with pytest.raises(IsADirectoryError):
            assert request_path_to_instance_resource_path('subdir')


def test_request_path_to_instance_resource_path_actual_file(app):
    """Test that a request for e.g. '/foo.png' when foo.png is a real file works."""
    with app.test_request_context():
        assert (request_path_to_instance_resource_path('bss-square-no-bg.png') ==
                ('pages/bss-square-no-bg.png', 'file'))


def test_request_path_to_instance_resource_path_markdown_symlink(app):
    """Test that a request for e.g. '/foo' when foo.md is a symlink to another .md file redirects."""
    with app.test_request_context():
        assert (request_path_to_instance_resource_path('symlink-to-no-title') ==
                ('pages/no-title.md', 'symlink'))


def test_request_path_to_instance_resource_path_file_symlink(app):
    """Test that a request for e.g. '/foo' when foo.txt is a symlink to another .txt file redirects."""
    with app.test_request_context():
        assert (request_path_to_instance_resource_path('symlink-to-foo.txt') ==
                ('pages/foo.txt', 'symlink'))


def test_request_path_to_instance_resource_path_dir_symlink(app):
    """Test that a request for e.g. '/foo' when /foo is a symlink to /bar redirects."""
    with app.test_request_context():
        assert (request_path_to_instance_resource_path('symlink-to-subdir/') ==
                ('pages/subdir', 'symlink'))


def test_request_path_to_instance_resource_path_subdir_symlink(app):
    """Test that a request for e.g. '/foo/baz' when /foo is a symlink to /bar redirects."""
    with app.test_request_context():
        assert (request_path_to_instance_resource_path('symlink-to-subdir/page-no-title') ==
                ('pages/subdir/page-no-title.md', 'symlink'))


def test_request_path_to_instance_resource_path_nonexistant_file_errors(app):
    """Test that a request for something not on disk errors."""
    with app.test_request_context():
        with pytest.raises(FileNotFoundError):
            assert request_path_to_instance_resource_path('nthanpthpnh')


def test_request_path_to_instance_resource_path_absolute_file_errors(app):
    """Test that a request for something not on disk errors."""
    with app.test_request_context():
        with pytest.raises(PermissionError):
            assert request_path_to_instance_resource_path('/etc/hosts')


def test_instance_resource_path_to_request_path_on_index(app):
    """Test index.md -> /."""
    with app.test_request_context():
        assert instance_resource_path_to_request_path('index.md') == ''


def test_instance_resource_path_to_request_path_on_page(app):
    """Test no-title.md -> no-title."""
    with app.test_request_context():
        assert instance_resource_path_to_request_path('no-title.md') == 'no-title'


def test_instance_resource_path_to_request_path_on_subdir(app):
    """Test subdir/index.md -> subdir/."""
    with app.test_request_context():
        assert instance_resource_path_to_request_path('subdir/index.md') == 'subdir/'


def test_instance_resource_path_to_request_path_on_subdir_and_page(app):
    """Test subdir/page.md -> subdir/page."""
    with app.test_request_context():
        assert instance_resource_path_to_request_path('subdir/page.md') == 'subdir/page'


def test_request_resource_request_root(app):
    """Test that a request can resolve to a resource and back to a request."""
    with app.test_request_context():
        instance_path, _ = request_path_to_instance_resource_path('index')
        instance_resource_path_to_request_path(instance_path) == ''


def test_request_resource_request_page(app):
    """Test that a request can resolve to a resource and back to a request."""
    with app.test_request_context():
        instance_path, _ = request_path_to_instance_resource_path('no-title')
        instance_resource_path_to_request_path(instance_path) == 'no-title'


def test_request_path_to_breadcrumb_display_patterns():
    """Test various conversions from request path to leaf nodes for display in the breadcrumbs."""
    assert request_path_to_breadcrumb_display('/foo') == 'foo'
    assert request_path_to_breadcrumb_display('/foo/') == 'foo'
    assert request_path_to_breadcrumb_display('/foo/bar') == 'bar'
    assert request_path_to_breadcrumb_display('/foo/bar/') == 'bar'
    assert request_path_to_breadcrumb_display('/') == ''

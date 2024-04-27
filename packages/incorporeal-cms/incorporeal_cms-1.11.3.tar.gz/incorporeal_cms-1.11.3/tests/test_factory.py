"""Test basic configuration stuff.

SPDX-FileCopyrightText: © 2020 Brian S. Stephan <bss@incorporeal.org>
SPDX-License-Identifier: AGPL-3.0-or-later
"""
import os

from incorporealcms import create_app

HERE = os.path.dirname(os.path.abspath(__file__))


def test_config():
    """Test create_app without passing test config."""
    instance_path = os.path.join(HERE, 'instance')
    assert not create_app(instance_path=instance_path).testing
    assert create_app(instance_path=instance_path, test_config={"TESTING": True}).testing


def test_markdown_meta_extension_always():
    """Test that the markdown meta extension is always loaded, even if not specified."""
    app = create_app(instance_path=os.path.join(HERE, 'instance'),
                     test_config={'MARKDOWN_EXTENSIONS': []})
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'<title>Index - example.com</title>' in response.data


def test_custom_markdown_extensions_work():
    """Test we can change extensions via config, and that they work.

    This used to test smarty, but that's added by default now, so we test
    that it can be removed by overriding the option.
    """
    app = create_app(instance_path=os.path.join(HERE, 'instance'))
    client = app.test_client()
    response = client.get('/mdash-or-triple-dash')
    assert response.status_code == 200
    assert b'word &mdash; word' in response.data

    app = create_app(instance_path=os.path.join(HERE, 'instance'),
                     test_config={'MARKDOWN_EXTENSIONS': []})
    client = app.test_client()
    response = client.get('/mdash-or-triple-dash')
    assert response.status_code == 200
    assert b'word --- word' in response.data


def test_title_override():
    """Test that a configuration with a specific title overrides the default."""
    instance_path = os.path.join(HERE, 'instance')
    app = create_app(instance_path=instance_path, test_config={'TITLE_SUFFIX': 'suou.net'})
    client = app.test_client()
    response = client.get('/no-title')
    assert response.status_code == 200
    assert b'<title>/no-title - suou.net</title>' in response.data


def test_media_file_access(client):
    """Test that media files are served, and properly."""
    response = client.get('/media/favicon.png')
    assert response.status_code == 200
    assert response.headers['content-type'] == 'image/png'


def test_favicon_override():
    """Test that a configuration with a specific favicon overrides the default."""
    instance_path = os.path.join(HERE, 'instance')
    app = create_app(instance_path=instance_path, test_config={'FAVICON': '/media/foo.png'})
    client = app.test_client()
    response = client.get('/no-title')
    assert response.status_code == 200
    assert b'<link rel="icon" href="/media/foo.png">' in response.data


def test_misconfigured_markdown_extensions():
    """Test that a misconfigured markdown extensions leads to a 500 at render time."""
    instance_path = os.path.join(HERE, 'instance')
    app = create_app(instance_path=instance_path, test_config={'MARKDOWN_EXTENSIONS': 'WRONG'})
    client = app.test_client()
    response = client.get('/no-title')
    assert response.status_code == 500

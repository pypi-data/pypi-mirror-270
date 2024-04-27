"""Test the feed methods.

SPDX-FileCopyrightText: © 2023 Brian S. Stephan <bss@incorporeal.org>
SPDX-License-Identifier: AGPL-3.0-or-later
"""
from incorporealcms.feed import serve_feed


def test_unknown_type_is_404(client):
    """Test that requesting a feed type that doesn't exist is a 404."""
    response = client.get('/feed/wat')
    assert response.status_code == 404


def test_atom_type_is_200(client):
    """Test that requesting an ATOM feed is found."""
    response = client.get('/feed/atom')
    assert response.status_code == 200
    assert 'application/atom+xml' in response.content_type
    print(response.text)


def test_rss_type_is_200(client):
    """Test that requesting an RSS feed is found."""
    response = client.get('/feed/rss')
    assert response.status_code == 200
    assert 'application/rss+xml' in response.content_type
    print(response.text)


def test_feed_generator_atom(app):
    """Test the root feed generator."""
    with app.test_request_context():
        content = serve_feed('atom')
    assert b'<id>https://example.com/</id>' in content.data
    assert b'<email>admin@example.com</email>' in content.data
    assert b'<name>Test Name</name>' in content.data


def test_feed_generator_rss(app):
    """Test the root feed generator."""
    with app.test_request_context():
        content = serve_feed('rss')
    assert b'<author>admin@example.com (Test Name)</author>' in content.data

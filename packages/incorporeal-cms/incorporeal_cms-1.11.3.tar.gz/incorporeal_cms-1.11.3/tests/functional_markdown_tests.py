"""Test graphviz functionality.

SPDX-FileCopyrightText: © 2021 Brian S. Stephan <bss@incorporeal.org>
SPDX-License-Identifier: AGPL-3.0-or-later
"""
import os

from incorporealcms import create_app

HERE = os.path.dirname(os.path.abspath(__file__))


def app_with_pydot():
    """Create the test app, including the pydot extension."""
    return create_app(instance_path=os.path.join(HERE, 'instance'),
                      test_config={'MARKDOWN_EXTENSIONS': ['incorporealcms.mdx.pydot']})


def test_functional_initialization():
    """Test initialization with the graphviz config."""
    app = app_with_pydot()
    assert app is not None


def test_graphviz_is_rendered():
    """Initialize the app with the graphviz extension and ensure it does something."""
    app = app_with_pydot()
    client = app.test_client()

    response = client.get('/test-graphviz')
    assert response.status_code == 200
    assert b'~~~pydot' not in response.data
    assert b'data:image/png;base64' in response.data


def test_two_graphviz_are_rendered():
    """Test two images are rendered."""
    app = app_with_pydot()
    client = app.test_client()

    response = client.get('/test-two-graphviz')
    assert response.status_code == 200
    assert b'~~~pydot' not in response.data
    assert b'data:image/png;base64' in response.data


def test_invalid_graphviz_is_not_rendered():
    """Check that invalid graphviz doesn't blow things up."""
    app = app_with_pydot()
    client = app.test_client()

    response = client.get('/test-invalid-graphviz')
    assert response.status_code == 500
    assert b'INTERNAL SERVER ERROR' in response.data


def test_figures_are_rendered(client):
    """Test that a page with my figure syntax renders as expected."""
    response = client.get('/figures')
    assert response.status_code == 200
    assert (b'<figure class="right"><img alt="fancy captioned logo" src="bss-square-no-bg.png" />'
            b'<figcaption>this is my cool logo!</figcaption></figure>') in response.data
    assert (b'<figure><img alt="vanilla captioned logo" src="bss-square-no-bg.png" />'
            b'<figcaption>this is my cool logo without an attr!</figcaption>\n</figure>') in response.data
    assert (b'<figure class="left"><img alt="fancy logo" src="bss-square-no-bg.png" />'
            b'<span></span></figure>') in response.data
    assert b'<figure><img alt="just a logo" src="bss-square-no-bg.png" /></figure>' in response.data

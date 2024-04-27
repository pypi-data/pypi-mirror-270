"""Create the test app and other fixtures.

SPDX-FileCopyrightText: © 2020 Brian S. Stephan <bss@incorporeal.org>
SPDX-License-Identifier: AGPL-3.0-or-later
"""
import os

import pytest

from incorporealcms import create_app

HERE = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def app():
    """Create the Flask application, with test settings."""
    app = create_app(instance_path=os.path.join(HERE, 'instance'))

    yield app


@pytest.fixture
def client(app):
    """Create a test client based on the test app."""
    return app.test_client()

"""Serve static files from the instance directory.

SPDX-FileCopyrightText: © 2022 Brian S. Stephan <bss@incorporeal.org>
SPDX-License-Identifier: AGPL-3.0-or-later
"""
import os

from flask import Blueprint
from flask import current_app as app
from flask import send_from_directory

bp = Blueprint('static', __name__, url_prefix='/custom-static')


@bp.route('/<path:name>')
def serve_instance_static_file(name):
    """Serve a static file from the instance directory, used for customization."""
    return send_from_directory(os.path.join(app.instance_path, 'custom-static'), name)

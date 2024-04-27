"""An application for running my Markdown-based sites.

SPDX-FileCopyrightText: © 2020 Brian S. Stephan <bss@incorporeal.org>
SPDX-License-Identifier: AGPL-3.0-or-later
"""
import logging
import os
from logging.config import dictConfig

from flask import Flask, request


def create_app(instance_path=None, test_config=None):
    """Create the Flask app, with allowances for customizing path and test settings."""
    app = Flask(__name__, instance_relative_config=True, instance_path=instance_path)

    # if it doesn't already exist, create the instance folder
    os.makedirs(app.instance_path, exist_ok=True)

    # load defaults from config provided with the application
    app.config.from_object('incorporealcms.config.Config')
    # load specific instance configurations
    app.config.from_pyfile('config.py', silent=True)
    if test_config:
        app.config.from_mapping(test_config)

    dictConfig(app.config['LOGGING'])

    logger = logging.getLogger(__name__)

    logger.debug("instance path: %s", app.instance_path)

    @app.before_request
    def log_request():
        logger.info("REQUEST:  %s %s", request.method, request.path)

    @app.after_request
    def log_response(response):
        logger.info("RESPONSE: %s %s: %s", request.method, request.path, response.status)
        return response

    from . import error_pages, feed, pages, static
    app.register_blueprint(feed.bp)
    app.register_blueprint(pages.bp)
    app.register_blueprint(static.bp)
    app.register_error_handler(400, error_pages.bad_request)
    app.register_error_handler(404, error_pages.page_not_found)
    app.register_error_handler(500, error_pages.internal_server_error)

    return app

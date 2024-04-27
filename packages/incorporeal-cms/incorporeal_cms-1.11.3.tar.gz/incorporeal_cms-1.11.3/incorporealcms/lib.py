"""Miscellaneous helper functions and whatnot.

SPDX-FileCopyrightText: © 2021 Brian S. Stephan <bss@incorporeal.org>
SPDX-License-Identifier: AGPL-3.0-or-later
"""
import datetime
import logging
import os
import re

import markdown
from flask import current_app as app
from flask import make_response, render_template, request
from markupsafe import Markup

logger = logging.getLogger(__name__)


def get_meta_str(md, key):
    """Provide the page's (parsed in Markup obj md) metadata for the specified key, or '' if unset."""
    return " ".join(md.Meta.get(key)) if md.Meta.get(key) else ""


def init_md():
    """Initialize the Markdown parser.

    This used to done at the app level in __init__, but extensions like footnotes apparently
    assume the parser to only live for the length of parsing one document, and create double
    footnote ref links if the one parser sees the same document multiple times.
    """
    # initialize markdown parser from config, but include
    # extensions our app depends on, like the meta extension
    return markdown.Markdown(extensions=app.config['MARKDOWN_EXTENSIONS'] + ['meta'],
                             extension_configs=app.config['MARKDOWN_EXTENSION_CONFIGS'])


def instance_resource_path_to_request_path(path):
    """Reverse a (presumed to exist) RELATIVE disk path to the canonical path that would show up in a Flask route.

    This does not include the leading /, so aside from the root index case, this should be
    bidirectional.
    """
    return re.sub(r'^pages/', '', re.sub(r'.md$', '', re.sub(r'index.md$', '', path)))


def parse_md(resolved_path):
    """Given a file to parse, return file content and other derived data along with the md object."""
    try:
        logger.debug("opening resolved path '%s'", resolved_path)
        with app.open_instance_resource(resolved_path, 'r') as entry_file:
            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(entry_file.name), tz=datetime.timezone.utc)
            entry = entry_file.read()
        logger.debug("resolved path '%s' read", resolved_path)
        md = init_md()
        content = Markup(md.convert(entry))
    except OSError:
        logger.exception("resolved path '%s' could not be opened!", resolved_path)
        raise
    except ValueError:
        logger.exception("error parsing/rendering markdown!")
        raise
    except TypeError:
        logger.exception("error loading/rendering markdown!")
        raise

    logger.debug("file metadata: %s", md.Meta)

    page_name = (get_meta_str(md, 'title') if md.Meta.get('title') else
                 f'/{instance_resource_path_to_request_path(resolved_path)}')
    page_title = f'{page_name} - {app.config["TITLE_SUFFIX"]}' if page_name else app.config['TITLE_SUFFIX']
    logger.debug("title (potentially derived): %s", page_title)

    return content, md, page_name, page_title, mtime


def render(template_name_or_list, **context):
    """Wrap Flask's render_template.

    * Determine the proper site theme to use in the template and provide it.
    """
    page_styles = app.config['PAGE_STYLES']
    selected_style = request.args.get('style', None)
    if selected_style:
        user_style = selected_style
    else:
        user_style = request.cookies.get('user-style')
        logger.debug("user style cookie: %s", user_style)
    context['user_style'] = page_styles.get(user_style, page_styles.get(app.config['DEFAULT_PAGE_STYLE']))
    context['page_styles'] = page_styles

    resp = make_response(render_template(template_name_or_list, **context))
    if selected_style:
        resp.set_cookie('user-style', selected_style)
    return resp

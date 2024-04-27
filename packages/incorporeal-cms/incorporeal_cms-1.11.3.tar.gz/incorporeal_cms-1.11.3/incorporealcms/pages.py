"""General page functionality.

SPDX-FileCopyrightText: © 2020 Brian S. Stephan <bss@incorporeal.org>
SPDX-License-Identifier: AGPL-3.0-or-later
"""
import logging
import os

from flask import Blueprint, abort
from flask import current_app as app
from flask import redirect, request, send_from_directory
from markupsafe import Markup
from werkzeug.security import safe_join

from incorporealcms.lib import get_meta_str, init_md, instance_resource_path_to_request_path, parse_md, render

logger = logging.getLogger(__name__)

bp = Blueprint('pages', __name__, url_prefix='/')


@bp.route('/', defaults={'path': 'index'})
@bp.route('/<path:path>')
def display_page(path):
    """Get the file contents of the requested path and render the file."""
    try:
        resolved_path, render_type = request_path_to_instance_resource_path(path)
        logger.debug("received request for path '%s', resolved to '%s', type '%s'",
                     path, resolved_path, render_type)
    except PermissionError:
        abort(400)
    except IsADirectoryError:
        return redirect(f'/{path}/', code=301)
    except FileNotFoundError:
        abort(404)

    if render_type == 'file':
        return send_from_directory(app.instance_path, resolved_path)
    elif render_type == 'symlink':
        logger.debug("attempting to redirect path '%s' to reverse of resource '%s'", path, resolved_path)
        redirect_path = f'/{instance_resource_path_to_request_path(resolved_path)}'
        logger.debug("redirect path: '%s'", redirect_path)
        return redirect(redirect_path, code=301)
    elif render_type == 'markdown':
        logger.debug("treating path '%s' as markdown '%s'", path, resolved_path)
        return handle_markdown_file_path(resolved_path)
    else:
        logger.exception("unsupported render_type '%s'!?", render_type)
        abort(500)


def handle_markdown_file_path(resolved_path):
    """Given a location on disk, attempt to open it and render the markdown within."""
    try:
        content, md, page_name, page_title, mtime = parse_md(resolved_path)
    except OSError:
        logger.exception("resolved path '%s' could not be opened!", resolved_path)
        abort(500)
    except ValueError:
        logger.exception("error parsing/rendering markdown!")
        abort(500)
    except TypeError:
        logger.exception("error loading/rendering markdown!")
        abort(500)
    else:
        parent_navs = generate_parent_navs(resolved_path)
        extra_footer = get_meta_str(md, 'footer') if md.Meta.get('footer') else None
        template = get_meta_str(md, 'template') if md.Meta.get('template') else 'base.html'

        # check if this has a HTTP redirect
        redirect_url = get_meta_str(md, 'redirect') if md.Meta.get('redirect') else None
        if redirect_url:
            logger.debug("redirecting via meta tag to '%s'", redirect_url)
            return redirect(redirect_url, code=301)

        return render(template, title=page_title, description=get_meta_str(md, 'description'),
                      image=get_meta_str(md, 'image'), base_url=request.base_url, content=content,
                      navs=parent_navs, mtime=mtime.strftime('%Y-%m-%d %H:%M:%S %Z'),
                      extra_footer=extra_footer)


def request_path_to_instance_resource_path(path):
    """Turn a request URL path to the full page path.

    flask.Flask.open_instance_resource will open a file like /etc/hosts if you tell it to,
    which sucks, so we do a lot of work here to make sure we have a valid request to
    something inside the pages dir.
    """
    # check if the path is allowed
    base_dir = os.path.realpath(f'{app.instance_path}/pages/')
    safe_path = safe_join(base_dir, path)
    # bail if the requested real path isn't inside the base directory
    if not safe_path:
        logger.warning("client tried to request a path '%s' outside of the base_dir!", path)
        raise PermissionError

    verbatim_path = os.path.abspath(safe_path)
    resolved_path = os.path.realpath(verbatim_path)
    logger.debug("base_dir '%s', constructed resolved_path '%s' for path '%s'", base_dir, resolved_path, path)

    # see if we have a real file or if we should infer markdown rendering
    if os.path.exists(resolved_path):
        # if this is a file-like request but actually a directory, redirect the user
        if os.path.isdir(resolved_path) and not path.endswith('/'):
            logger.info("client requested a path '%s' that is actually a directory", path)
            raise IsADirectoryError

        # if the requested path contains a symlink, redirect the user
        if verbatim_path != resolved_path:
            logger.info("client requested a path '%s' that is actually a symlink to file '%s'", path, resolved_path)
            return resolved_path.replace(f'{app.instance_path}{os.path.sep}', ''), 'symlink'

        # derive the proper markdown or actual file depending on if this is a dir or file
        if os.path.isdir(resolved_path):
            resolved_path = os.path.join(resolved_path, 'index.md')
            return resolved_path.replace(f'{app.instance_path}{os.path.sep}', ''), 'markdown'

        logger.info("final DIRECT path = '%s' for request '%s'", resolved_path, path)
        return resolved_path.replace(f'{app.instance_path}{os.path.sep}', ''), 'file'

    # if we're here, this isn't direct file access, so try markdown inference
    verbatim_path = f'{safe_path}.md'
    resolved_path = os.path.realpath(verbatim_path)

    # does the final file actually exist?
    if not os.path.exists(resolved_path):
        logger.warning("requested final path '%s' does not exist!", resolved_path)
        raise FileNotFoundError

    # check for symlinks
    if verbatim_path != resolved_path:
        logger.info("client requested a path '%s' that is actually a symlink to file '%s'", path, resolved_path)
        return resolved_path.replace(f'{app.instance_path}{os.path.sep}', ''), 'symlink'

    logger.info("final path = '%s' for request '%s'", resolved_path, path)
    # we checked that the file exists via absolute path, but now we need to give the path relative to instance dir
    return resolved_path.replace(f'{app.instance_path}{os.path.sep}', ''), 'markdown'


def generate_parent_navs(path):
    """Create a series of paths/links to navigate up from the given resource path."""
    if path == 'pages/index.md':
        # bail and return the domain name as a terminal case
        return [(app.config['DOMAIN_NAME'], '/')]
    else:
        if path.endswith('index.md'):
            # index case: one dirname for foo/bar/index.md -> foo/bar, one for foo/bar -> foo
            parent_resource_dir = os.path.dirname(os.path.dirname(path))
        else:
            # usual case: foo/buh.md -> foo
            parent_resource_dir = os.path.dirname(path)

        # generate the request path (i.e. what the link will be) for this path, and
        # also the resource path of this parent (which is always a dir, so always index.md)
        request_path = f'/{instance_resource_path_to_request_path(path)}'
        parent_resource_path = os.path.join(parent_resource_dir, 'index.md')

        logger.debug("resource path: '%s'; request path: '%s'; parent resource path: '%s'", path,
                     request_path, parent_resource_path)

        # for issues regarding parser reuse (see lib.init_md) we reinitialize the parser here
        md = init_md()

        # read the resource
        try:
            with app.open_instance_resource(path, 'r') as entry_file:
                entry = entry_file.read()
            _ = Markup(md.convert(entry))
            page_name = (" ".join(md.Meta.get('title')) if md.Meta.get('title')
                         else request_path_to_breadcrumb_display(request_path))
            return generate_parent_navs(parent_resource_path) + [(page_name, request_path)]
        except FileNotFoundError:
            return generate_parent_navs(parent_resource_path) + [(request_path, request_path)]


def request_path_to_breadcrumb_display(path):
    """Given a request path, e.g. "/foo/bar/baz/", turn it into breadcrumby text "baz"."""
    undired = path.rstrip('/')
    leaf = undired[undired.rfind('/'):]
    return leaf.strip('/')

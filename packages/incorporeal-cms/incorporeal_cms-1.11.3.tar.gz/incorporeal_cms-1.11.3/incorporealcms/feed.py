"""Generate Atom and RSS feeds based on content in a blog-ish location.

This parses a special root directory, feed/, for YYYYMMDD-foo.md files,
and combines them into an Atom or RSS feed. These files *should* be symlinks
to the real pages, which may mirror the same YYYYMMDD-foo.md file naming scheme
under pages/ (which may make sense for a blog) if they want, but could just
as well be pages/foo content.

SPDX-FileCopyrightText: © 2023 Brian S. Stephan <bss@incorporeal.org>
SPDX-License-Identifier: AGPL-3.0-or-later
"""
import logging
import os
import re

from feedgen.feed import FeedGenerator
from flask import Blueprint, Response, abort
from flask import current_app as app

from incorporealcms.lib import instance_resource_path_to_request_path, parse_md

logger = logging.getLogger(__name__)

bp = Blueprint('feed', __name__, url_prefix='/feed')


@bp.route('/<feed_type>')
def serve_feed(feed_type):
    """Serve the Atom or RSS feed as requested."""
    logger.warning("wat")
    if feed_type not in ('atom', 'rss'):
        abort(404)

    fg = FeedGenerator()
    fg.id(f'https://{app.config["DOMAIN_NAME"]}/')
    fg.title(f'{app.config["TITLE_SUFFIX"]}')
    fg.author(app.config["AUTHOR"])
    fg.link(href=f'https://{app.config["DOMAIN_NAME"]}/feed/{feed_type}', rel='self')
    fg.link(href=f'https://{app.config["DOMAIN_NAME"]}', rel='alternate')
    fg.subtitle(f"Blog posts and other dated materials from {app.config['TITLE_SUFFIX']}")

    # get recent feeds
    feed_path = os.path.join(app.instance_path, 'feed')
    feed_entry_paths = [os.path.join(dirpath, filename) for dirpath, _, filenames in os.walk(feed_path)
                        for filename in filenames if os.path.islink(os.path.join(dirpath, filename))]
    for feed_entry_path in sorted(feed_entry_paths):
        # get the actual file to parse it
        resolved_path = os.path.realpath(feed_entry_path).replace(f'{app.instance_path}/', '')
        try:
            content, md, page_name, page_title, mtime = parse_md(resolved_path)
            link = f'https://{app.config["DOMAIN_NAME"]}/{instance_resource_path_to_request_path(resolved_path)}'
        except (OSError, ValueError, TypeError):
            logger.exception("error loading/rendering markdown!")
            abort(500)

        fe = fg.add_entry()
        fe.id(_generate_feed_id(feed_entry_path))
        fe.title(page_name if page_name else page_title)
        fe.author(app.config["AUTHOR"])
        fe.link(href=link)
        fe.content(content, type='html')

    if feed_type == 'atom':
        return Response(fg.atom_str(pretty=True), mimetype='application/atom+xml')
    else:
        return Response(fg.rss_str(pretty=True), mimetype='application/rss+xml')


def _generate_feed_id(feed_entry_path):
    """For a relative file path, generate the Atom/RSS feed ID for it."""
    date = re.sub(r'.*(\d{4})(\d{2})(\d{2}).*', r'\1-\2-\3', feed_entry_path)
    cleaned = feed_entry_path.replace('#', '/').replace('feed/', '', 1).replace(app.instance_path, '')
    return f'tag:{app.config["DOMAIN_NAME"]},{date}:{cleaned}'

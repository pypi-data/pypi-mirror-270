"""Error page views for 400, 404, etc.

SPDX-FileCopyrightText: © 2021 Brian S. Stephan <bss@incorporeal.org>
SPDX-License-Identifier: AGPL-3.0-or-later
"""
from incorporealcms.lib import render


def bad_request(error):
    """Display 400 error messaging."""
    return render('400.html'), 400


def internal_server_error(error):
    """Display 500 error messaging."""
    return render('500.html'), 500


def page_not_found(error):
    """Display 404 error messaging."""
    return render('404.html'), 404

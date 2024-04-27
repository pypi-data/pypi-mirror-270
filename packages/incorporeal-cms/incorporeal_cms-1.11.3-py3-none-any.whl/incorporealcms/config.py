"""Default configuration.

SPDX-FileCopyrightText: © 2020 Brian S. Stephan <bss@incorporeal.org>
SPDX-License-Identifier: AGPL-3.0-or-later
"""


class Config(object):
    """Represent the default configuration.

    Reminder: this should be overwritten in the instance config.py, not here!
    """

    DEBUG = False
    TESTING = False

    LOGGING = {
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s %(levelname)-7s %(name)s] %(message)s',
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'default',
            },
        },
        'loggers': {
            '': {
                'level': 'INFO',
                'handlers': ['console'],
            },
        },
    }

    MARKDOWN_EXTENSIONS = ['extra', 'incorporealcms.mdx.figures', 'sane_lists', 'smarty', 'toc']
    MARKDOWN_EXTENSION_CONFIGS = {
        'extra': {
            'footnotes': {
                'UNIQUE_IDS': True,
            },
        },
        'smarty': {
            'smart_dashes': True,
            'smart_quotes': False,
            'smart_angled_quotes': False,
            'smart_ellipses': True,
        },
    }

    MEDIA_DIR = 'media'

    # customizations
    PAGE_STYLES = {
        'dark': '/static/css/dark.css',
        'light': '/static/css/light.css',
        'plain': '/static/css/plain.css',
    }

    DEFAULT_PAGE_STYLE = 'light'
    DOMAIN_NAME = 'example.com'
    TITLE_SUFFIX = DOMAIN_NAME
    CONTACT_EMAIL = 'admin@example.com'

    # feed settings
    AUTHOR = {'name': 'Test Name', 'email': 'admin@example.com'}

    # specify FAVICON in your instance config.py to override the provided icon

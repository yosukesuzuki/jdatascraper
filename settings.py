# -*- coding: utf-8 -*-

"""
A sample of kay settings.

:Copyright: (c) 2009 Accense Technology, Inc. 
                     Takashi Matsuo <tmatsuo@candit.jp>,
                     All rights reserved.
:license: BSD, see LICENSE for more details.
"""

DEFAULT_TIMEZONE = 'UTC'
DEBUG = True
PROFILE = False
SECRET_KEY = 'ReplaceItWithSecretString'
SESSION_PREFIX = 'gaesess:'
COOKIE_AGE = 1209600  # 2 weeks
COOKIE_NAME = 'KAY_SESSION'

ADMINS = (
)

TEMPLATE_DIRS = (
)

USE_I18N = False
DEFAULT_LANG = 'en'

INSTALLED_APPS = (
    'scraper',
    'core',
    'main',
)

APP_MOUNT_POINTS = {
    'scraper': '/scraper',
    'main': '/',
}

# You can remove following settings if unnecessary.
CONTEXT_PROCESSORS = (
    'kay.context_processors.request',
    'kay.context_processors.url_functions',
    'kay.context_processors.media_url',
)

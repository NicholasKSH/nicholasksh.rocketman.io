from .base import *
import os

DEBUG = False
SECRET_KEY='-f1a2i_ik&^crtmv*_n*k&rlvb1x**lo^$*$%=iqd(x6o2$%(3'
ALLOWED_HOSTS=['localhost', 'rocketman.wagtail.com', '*']

cwd = os.getcwd()
CACHES = {
    "default":{
        "BACKEND":"django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION":f"{cwd}/.cache"
    }
}

DATABASES={
    "defalut":{
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        "NAME": 'rocketman',
        "USER": 'rocketman',
        "PASSWORD": 'xfHjB^F2p9s*zhqFT6cNx2',
        "HOST": 'localhost',
        "port": "",
    }
}

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://4ceaf53e89a94ee1afe564297c881434@o1082323.ingest.sentry.io/6090611",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

try:
    from .local import *
except ImportError:
    pass

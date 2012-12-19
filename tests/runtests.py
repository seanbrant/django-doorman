#!/usr/bin/env python

import os
import sys

from django.conf import settings


if not settings.configured:
    settings.configure(
        DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3'}},
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'doorman',
            'basicapp',
        ],
        TEST_DISCOVER_ROOT=os.path.abspath(os.path.dirname(__file__)),
    )


def runtests():
    from discover_runner.runner import DiscoverRunner
    runner = DiscoverRunner(verbosity=1, interactive=True, failfast=False)
    failures = runner.run_tests([])
    sys.exit(failures)


if __name__ == '__main__':
    runtests()

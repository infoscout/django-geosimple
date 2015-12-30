#!/usr/bin/env python
import sys
import subprocess
import logging


logger = logging.getLogger(__name__)
FLAKE8_ARGS = ['geosimple/', '--ignore=E501', '--exclude=__init__.py']
COVERAGE_ARGS = ['--source=geosimple', '--omit=**tests**', 'manage.py', 'test']


def exit_on_failure(command, message=None):
    if command:
        sys.exit(command)


def flake8_main(args):
    print 'Running: flake8 %s' % " ".join(str(x) for x in args)
    command = subprocess.call(['flake8'] + args)
    logger.info('Success. flake8 passed.') if command else None
    return command


def run_tests_coverage(args):
    print 'Running: coverage %s' % " ".join(str(x) for x in args)
    command = subprocess.call(['coverage', 'run'] + args)
    logger.info('Success. Coverage generated.') if command else None
    command = subprocess.call(['coverage', 'report'])
    return command


exit_on_failure(flake8_main(FLAKE8_ARGS))
exit_on_failure(run_tests_coverage(COVERAGE_ARGS))

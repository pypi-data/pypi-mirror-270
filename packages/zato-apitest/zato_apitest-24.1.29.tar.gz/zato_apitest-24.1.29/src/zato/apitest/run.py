# -*- coding: utf-8 -*-

"""
Copyright (C) 2024, Zato Source s.r.o. https://zato.io

Licensed under SSPL 1.0, see LICENSE.txt for terms and conditions.
"""

# stdlib
import os
from logging import getLogger

# Behave
from behave.configuration import Configuration # type: ignore
from behave.runner import Runner # type: ignore

# ConfigObj
from configobj import ConfigObj # type: ignore

# ################################################################################################################################
# ################################################################################################################################

if 0:
    from zato.apitest.typing_ import strlistnone # type: ignore

# ################################################################################################################################
# ################################################################################################################################

logger = getLogger('apitest')

# ################################################################################################################################
# ################################################################################################################################

def patch_http_send():

    # stdlib
    import http.client

    # Extract for later use
    orig_send = http.client.HTTPConnection.send # type: ignore

    # This will log data sent
    def _send(self, data): # type: ignore
        logger.info('\n--------- BEGIN Send ---------\n%s\n--------- END Send ---------' % data.decode('utf8'))
        return orig_send(self, data)

    # Patch it now
    http.client.HTTPConnection.send = _send # type: ignore

# ################################################################################################################################
# ################################################################################################################################

def handle(path:'str', is_verbose:'bool', args:'strlistnone'=None):

    if is_verbose:

        # Patch the outgoing connections
        patch_http_send()

        # This needs to be a string
        os.environ['Zato_API_Test_Is_Verbose'] = 'True'

    file_conf = ConfigObj(os.path.join(path, 'features', 'config.ini'))
    try:
        behave_options = file_conf['behave']['options'] # type: ignore
    except KeyError:
        raise ValueError("Behave config not found. Are you running with the correct path?")
    if args:
        behave_options += ' ' + ' '.join(args)

    tags = os.environ.get('Zato_API_Test_Tags')
    if tags:
        behave_options += ' --tags '
        behave_options += ','.join(tags.split())

    conf = Configuration(behave_options)
    conf.paths = [os.path.join(path, 'features')]
    runner = Runner(conf)
    runner.run()

# ################################################################################################################################
# ################################################################################################################################

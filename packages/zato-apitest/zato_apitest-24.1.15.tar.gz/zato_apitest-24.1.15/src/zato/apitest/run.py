# -*- coding: utf-8 -*-

"""
Copyright (C) 2024, Zato Source s.r.o. https://zato.io

Licensed under SSPL 1.0, see LICENSE.txt for terms and conditions.
"""

# stdlib
import os

# Behave
from behave.configuration import Configuration # type: ignore
from behave.runner import Runner # type: ignore

# ConfigObj
from configobj import ConfigObj # type: ignore

# ################################################################################################################################
# ################################################################################################################################

if 0:
    from zato.apitest.typing_ import strlistnone

# ################################################################################################################################
# ################################################################################################################################

def handle(path:'str', args:'strlistnone'=None):
    e
    file_conf = ConfigObj(os.path.join(path, 'features', 'config.ini'))
    w
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
    result = runner.run()
    import time
    time.sleep(0.5)
    z

# ################################################################################################################################
# ################################################################################################################################

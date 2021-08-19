#!/usr/bin/env python3
# 
# File: test_run_analyzer_app.py

from __future__ import absolute_import

import connexion

## fix path so that contained py files can be imported
import os, sys

"""
# sys.path.append(os.path.curdir + "/analyzer_app")
sys.path.append(os.path.abspath(__file__))

from analyzer_app.openapi_server import encoder

def main():
    app = connexion.App(__name__, specification_dir='./analyzer_app/openapi_server/openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Analyzer and HUB API'},
                pythonic_params=True)

    app.run(port=8080)
"""

def main():
    sys.path.append(os.path.abspath(__file__))
    sys.path.append("/home/bag/Zoetis/bag_vetscan/make_analyzer_dracula/analyzer_app/openapi_server")

    options = {
        "swagger_ui": True
        }
    specification_dir = os.path.join(os.path.dirname(__file__), 'analyzer_app/openapi_server/openapi')
    app = connexion.AioHttpApp(__name__, specification_dir=specification_dir, options=options)
    app.add_api('openapi.yaml',
                arguments={'title': 'Analyzer and HUB API'},
                pythonic_params=True,
                pass_context_arg_name='request')

    app.run(port=8080)


if __name__ == '__main__':
    main()

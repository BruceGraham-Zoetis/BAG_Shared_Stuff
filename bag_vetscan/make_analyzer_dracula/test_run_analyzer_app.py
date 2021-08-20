#!/usr/bin/env python3
# 
# File: test_run_analyzer_app.py

from __future__ import absolute_import

import connexion

## fix path so that contained py files can be imported
import os, sys
sys.path.append(os.path.curdir + "/analyzer_app")

from analyzer_app.openapi_server import encoder


def main():
    app_options = {
        "swagger_ui": True
        #"swagger_ui": False
        }

    app = connexion.App(
                __name__,
                specification_dir='./analyzer_app/openapi_server/openapi/', 
                options = app_options)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Analyzer and HUB API'},
                pythonic_params=True)

    app.run(port=8080)


if __name__ == '__main__':
    main()

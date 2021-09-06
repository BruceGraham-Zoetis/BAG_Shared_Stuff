#!/usr/bin/env python3
# 
# File: test_run_analyzer_app.py

from __future__ import absolute_import

import connexion

## fix path so that contained py files can be imported
import os, sys
import threading

strThisFilePath = os.path.dirname(__file__)
sys.path.append(strThisFilePath)
sys.path.append(strThisFilePath + "/analyzer_app")
from analyzer_app.openapi_server import encoder



def thread_analyzer_apis():
    print("Running openAPIs")

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


def start_thread_openapi_server():
    print("Starting openAPI server")
    thread = threading.Thread(target = thread_analyzer_apis)
    thread.start()
    return thread



if __name__ == '__main__':
    print("")
    thread_openapi = start_thread_openapi_server()

    forever = threading.Event()
    forever.wait()


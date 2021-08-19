#!/bin/bash

# File: make_analyzer.sh
# Purpose: Rebuild the analyzer server.

# Notes: analyzer_config.yaml lists files that the generator will use instead of the generated code.

# openapi-generator-cli generate -c ./analyzer_config.yaml -g python-flask -i ../openAPISpecs/openAPISpec.json -o analyzer_app
openapi-generator-cli generate -c ./analyzer_config.yaml -g python-aiohttp -i ../openAPISpecs/openAPISpec.json -o analyzer_app




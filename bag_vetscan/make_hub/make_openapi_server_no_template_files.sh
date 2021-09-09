#!/bin/bash

# File: make_hub.sh
# Purpose: Rebuild the server's openAPI python code.

# Install the generator
# Open the terminal and run the following to install OpenAPI Generator:
# $ npm install @openapitools/openapi-generator-cli -g

# Notes: hub_config.yaml lists files that the generator will use instead of the generated code.

openapi-generator-cli generate -g python-legacy -i ../openAPISpecs/openAPISpec.json -o hub_app_no_template_files




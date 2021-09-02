#!/bin/bash

# File: make_openapi_java_client.sh
# Purpose: Rebuild the client's openAPI javas code.

# Install the generator
# Open the terminal and run the following to install OpenAPI Generator:
# $ npm install @openapitools/openapi-generator-cli -g

# Notes: java_config.yaml lists files that the generator will use instead of the generated code.

openapi-generator-cli generate -c ./java_config.yaml -g java artifactUrl=localhost:8080 -i ../openAPISpecs/openAPISpec.json -o hub_app



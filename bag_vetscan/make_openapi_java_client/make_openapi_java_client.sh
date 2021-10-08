#!/bin/bash

# File: make_openapi_java_client.sh
# Purpose: Rebuild the client's openAPI javas code.

# Install the generator
# Open the terminal and run the following to install OpenAPI Generator:
# $ npm install @openapitools/openapi-generator-cli -g

# output files:
#   util Java: openapi_client_java/src/main/java/org/openapitools/client
#   API Paths: openapi_client_java/src/main/java/org/openapitools/client/api
# API Schemas: openapi_client_java/src/main/java/org/openapitools/client/model

rm -rf openapi_client_java/

clear

## Options for openapi-generator-cli generate
# -c <configuration file>
# -g <the language for the generated files>
# -i <the api specification file>
# -o <output directory for the generated files>
# -t/--template CLI options
## https://openapi-generator.tech/docs/templating/

#openapi-generator-cli generate -c ./java_config.yaml -g java artifactUrl=localhost:8080 -i ./openAPISpecs/openAPISpec.json -o openapi_client_java
openapi-generator-cli generate -c ./java_config.yaml -g java -i ./openAPISpecs/openAPISpec.json -o openapi_client_java


# File: java_config.yaml lists files that the generator will use instead of the generated code.
# additionalProperties:
#   ...
# templateDir: 
#   templates <== a templates directory
# files:
#   file names <== the list of templates files to use instead of the generated code.

# Directory: templates


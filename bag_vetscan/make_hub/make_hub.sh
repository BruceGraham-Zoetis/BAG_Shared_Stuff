#!/bin/bash

# File: make_hub.sh
# Purpose: Rebuild the hub server.

# Notes: hub_config.yaml lists files that the generator will use instead of the generated code.

openapi-generator-cli generate -c ./hub_config.yaml -g python-legacy -i openAPISpecs/openAPISpec.json -o hub_app





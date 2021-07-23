# vetscan_hub_instrument_API
Implementation and documentation of the interface between the Vetscan HUB and all anlayzers.

# Design
The Vetscan HUB and Analyzer API (API) is defines the methods and formats of all data that passes back and forth between any analyzer and the HUB.

The HUB will be the client for all interfaces and the analyzers will be the server for all interfaces.

At this time, all data will be passed back and forth through the means of RESTful interfaces hosted by the server and queried by the HUB.  Best practices for the specification and implementation of RESTful interfaces should be followed as best as possible, but so rigidly that it causes undo design constraints and complexity.

## References
https://confluence.zoetis.com/pages/viewpage.action?spaceKey=DXRDSW&title=Analyzer+API+Reference
https://confluence.zoetis.com/display/DXRDSW/HUB+to+Instrument+API+Structure

# Implementation

There are three main functional parts to this repository:

1. Open API Specification File
   1. Built using Open API 3.0 specification
   2. Describes all interfaces and data
   3. Useful for creation of documentation
   4. Useful for auto generation of source code
   5. Useful for auto generation of web test utility
2. Python API Module named anaylzerHUBAPI.py
   1. This is the module that should be used by the HUB and any Zoetis (or OEM partner we release it to) to communicate using the API
   2. The client and server are both provided with blocking and non-blocking operational modes
   3. The client uses the API to send messages
   4. The server uses the API to register handlers for each API endpoint that are called when 
3. API and API module testing
   1. Provides automated testing of all interfaces
   2. Provides examples of how to register handlers for each API endpoint
   3. Provides examples of data passed along all interfaces
   4. Provides examples of sending to all data passed along all interfaces
   5. Provides examples of handlers receiving all data passed along all interfaces

# Tools and Major Libraries Used

## Swagger Editor
The OAS can be actively used by the tool https://editor.swagger.io/.  Any operator can manually act as the HUB and send requests and receive responses with this tool.  It is also an easy way to see the API visually.  From here you can generate server stubs for messages as well.  Those can be pulled into the API source code.  HTML documentation can also be generated here.

If a server is running, you can access the swagger UI at the following URL and manually allow the interface to be used:  http://localhost:8080/ui/.  Also if the server is running, you can access the OAS file at the following URL:  http://localhost:8080/openapi.json.  Both of these options can be disabled and may need to be later for production use.  See https://github.com/zalando/connexion#the-swagger-ui-console and https://github.com/zalando/connexion#swagger-json for how to enable and disable this functionality.

There is a library available that will allow this sort of code generation to be automated apart from the website called openapi-generator (https://github.com/OpenAPITools/openapi-generator).  This is actually a community supported fork of swagger-editor.  The issue with importing this and using it is that it is a java program.  At this time it seems unreasonable to put a java program requirement into the repository.  However, as we work towards greater automation in the future of code and documentation generation, this will serve as a good starting point for investigation and implementation.

## swagger-parser
There may be an advantage to fully resolving the OAS file (resolving $refs) in the file before using it in swagger editor.  Here is the tool to do that:  https://apitools.dev/swagger-parser/online/.  There would be a distinct advantage to putting this tool directly into the repository and doing this each time at runtime before the API module consumed it but is a javascript library that can be run with Node (https://github.com/APIDevTools/swagger-parser).  There is probably a good reason not to bring Node into the design just to take advantage of this library but that design decision can be revisited at a later time.

## connexion
Connexion is the python library that consumes the OAS file and generates the server.  Documentation for this package can be found here:  https://connexion.readthedocs.io/en/latest/

## aiohttp
aiohttp is the python server library that connexion uses.  Flask would also work with connexion but aiohttp was already a familiar tool being used by Elliot and Alex so the decision was made to stick with it for now.  aiohttp also has support for websockets so if we need to add that sort of bidirectional communication in the future, aiohttp will help support that.  aiohttp is a large tool and the documentation can be found here:  https://docs.aiohttp.org/en/stable/

## VSCode Extensions
The following VSCode extensions are helpful in working with OAS files:
1. OpenAPI (Swagger) Editor

# todo
* Automated testing and possibly automated test generation

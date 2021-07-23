# *****************************************************************************
# Dependencies
# *****************************************************************************
# system imports
import aiohttp
import connexion
from aiohttp import web
from urllib import parse
import asyncio
import aiohttp_cors
import json
import os
import threading
import requests
import inspect
import logging

# module globals
serverRunning = False
apiDetails = {}
app = {}
apprunner = {}
cors = {}
registeredMessageHandlers = {}
messageHandlersMutex = threading.Lock()

# *****************************************************************************
# FunctionName: registerMessageHandler
# Description:  Function will register a message handler as passed from the calling
#               function and all future API hits at the specified endpoint will
#               be routed back to that function
# Arguments:    string sChannel - the channel the message is on
#               string sMsgName - the name of the message
#               string sHTTPMethod - the http method.  Can be "put", "get", "post",
#                   or "delete"
#               function messageHandler - the function for this message.  Should
#                   accept arguments as passed by api call.  See the specific api
#                   call for what those arguments are
# Return:       None
# *****************************************************************************
def registerMessageHandler(sChannel, sMsgName, sHTTPMethod, messageHandler):

    # grab the mutex so adding is thread safe
    messageHandlersMutex.acquire()

    # check to see if the channel has already been declared
    if (sChannel in registeredMessageHandlers) == False:
        registeredMessageHandlers[sChannel] = {}

    # check to see if the message has already been declared on the channel
    if (sMsgName in registeredMessageHandlers[sChannel]) == False:
        registeredMessageHandlers[sChannel][sMsgName] = {}

    # now set the message handler passed into this function in the variable
    registeredMessageHandlers[sChannel][sMsgName][sHTTPMethod] = messageHandler

    # release the mutex
    messageHandlersMutex.release()

# *****************************************************************************
# FunctionName: _getMessageDetailsFromCallingFunctionName
# Description:  This function will find the channel, message name, and http method
#               based on the name of the function that called it.  Specific to connexion
#               function handlers.
# Arguments:    None
# Return:       string - the sChannel of the request
#               string - the sMsgName of the request
#               string - the http method.  Either "get", "put", "post", or "delete"
# *****************************************************************************
def _getMessageDetailsFromCallingFunctionName():
    # get the function name: https://www.stefaanlippens.net/python_inspect/
    callingFunctionName = inspect.stack()[2][3]

    callingFunctionNameSplit = callingFunctionName.split("_")

    # grab http method off the front
    sHTTPMethod = callingFunctionNameSplit.pop(0)

    # now loop through all the message parts remaining and make them upper case
    for index in range(len(callingFunctionNameSplit)): 
        callingFunctionNameSplit[index] = callingFunctionNameSplit[index].capitalize()

    # now grab the channel and handle any multiword channels
    sChannel = callingFunctionNameSplit.pop(0)

    if(sChannel == "Remote" and callingFunctionNameSplit[0] == "Control"):
        sChannel += callingFunctionNameSplit.pop(0)

    # create the message name from everything left
    sMsgName = "".join(callingFunctionNameSplit)

    return sChannel, sMsgName, sHTTPMethod

# *****************************************************************************
# FunctionName: callRegisteredMessageHandler
# Description:  All message routing from connexion should end up here to make
#               handling centralized.
# Arguments:    dictionary additionalArguments - a dictionary of any additional arguments
#                   that were passed along with the request.  If there are no additional
#                   arguments this will be an empty dictionary.  If the data was json, it 
#                   should be converted into a dictionary before being returned here.
# Return:       dictionary - if any data is going to be passed back, it should be
#                   passed in here as a python dictionary
#               number - the HTTP response code
# *****************************************************************************
def callRegisteredMessageHandler(additionalArguments=None):

    # grab information out of the calling functions name about the call
    sChannel, sMsgName, sHTTPMethod = _getMessageDetailsFromCallingFunctionName()

    # will put the response code here later
    responseCode = 0
    responseDictionary = {}

    # make sure there is a registered handler for this request
    if (sChannel in registeredMessageHandlers) == False or \
        (sMsgName in registeredMessageHandlers[sChannel]) ==False or \
        (sHTTPMethod in registeredMessageHandlers[sChannel][sMsgName]) == False:
        responseCode = 405
        responseDictionary = {
            "detail": "Valid path but this server has not registered a handler for it",
            "status": 405,
            "title": "Method Not Allowed",
            "type": sHTTPMethod + " on /" + sChannel + "/" + sMsgName
            }
    # if there is a registered handler, call it now with the arguments passed in here
    else:
        # grab the handler under mutex control
        messageHandlersMutex.acquire()
        messageHandler = registeredMessageHandlers[sChannel][sMsgName][sHTTPMethod]
        messageHandlersMutex.release()
        
        if(additionalArguments != None):
            responseDictionary,  responseCode = messageHandler(additionalArguments)
        else:
            responseDictionary,  responseCode = messageHandler()

    return responseDictionary, responseCode

# *****************************************************************************
# FunctionName: _initializeServer
# Description:  Function will initialize the webserver.  Should not be called outside
#               this module.
# Arguments:    None
# Return:       None
# https://github.com/zalando/connexion/issues/1072
# *****************************************************************************
def _initializeServer():
    
    # use module level app
    global app

    app = connexion.AioHttpApp(__name__, 
        port=8080, 
        specification_dir='openAPISpecs/',
        # https://github.com/OpenAPITools/openapi-generator/issues/1322
        only_one_api=True
        )
    
    app.add_api('openAPISpec.json', 
        arguments={'title': 'Analyzer and HUB API'}, 
        pythonic_params=True, 
        validate_responses=True,
        # doesn't always work with JSON bodies: https://github.com/zalando/connexion/issues/837
        strict_validation=True
        )

    # Configure default CORS settings.
    cors = aiohttp_cors.setup(app.app, defaults={
            "*": aiohttp_cors.ResourceOptions(allow_credentials=True,
                                            expose_headers="*",
                                            allow_headers="*", 
                                            allow_methods=["GET", "POST", "PUT", "DELETE"]
                                            )
    })

    # Configure CORS on every route
    for route in list(app.app.router.routes()):
        cors.add(route)

# *****************************************************************************
# FunctionName: startServer_Blocking
# Description:  Function will initialize and start webserver implementing the API.
#               This should be called when you want to start and initialize the server
#               in the foreground.  This function will block and not return.
# Arguments:    None
# Return:       None
# https://github.com/zalando/connexion/issues/1072
# *****************************************************************************
def startServer_Blocking():
    # grab module level serverRunning for comparison in next line
    global serverRunning

    # if the server is not already running, set flag, initialize server and start
    if(serverRunning == False):
        serverRunning = True
        _initializeServer()
        app.run()

# *****************************************************************************
# FunctionName: initializeServer_NonBlocking
# Description:  Function will initialize and start webserver implementing the API
#               in preparation to be started in non blocking operation.  This function
#               should not be called outside this module.
# Arguments:    None
# Return:       runner - an aiohttp supplied object that will hold the information
#                   needed to start asynchronously
# *****************************************************************************
def _initializeServer_NonBlocking():

    # call function to initialize server
    _initializeServer()
    
    # now create a runner we will start later
    return web.AppRunner(app.app)

# *****************************************************************************
# FunctionName: _startServerInBackground
# Description:  Function not to be called outside of this module that will
#               start the server in the background
# Arguments:    runner - an aiohttp supplied object that will hold the information
#                   needed to start asynchronously
# Return:       None
# *****************************************************************************
def _startServer_NonBlocking(runner):
    #store runner at module level for use later
    global apprunner
    apprunner = runner

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(runner.setup())
    # todo:  come back and fix this so we can use port from OAS
    site = web.TCPSite(runner, 'localhost', 8080)
    loop.run_until_complete(site.start())
    loop.run_forever()

# *****************************************************************************
# FunctionName: startServer_NonBlocking
# Description:  This function will start the server in nonblocking mode.
# Arguments:    None
# Return:       None
# https://newbedev.com/how-to-run-an-aiohttp-server-in-a-thread
# *****************************************************************************
def startServer_NonBlocking():
    # grab module level serverRunning for comparison in next line
    global serverRunning

    # if the server isn't already running
    if(serverRunning == False):
        # configure new thread and start it
        newThread = threading.Thread(target=_startServer_NonBlocking, args=(_initializeServer_NonBlocking(),))
        newThread.start()

        # set flag that the server is running so we don't ever try to start it again
        serverRunning = True

# *****************************************************************************
# FunctionName: stopServer
# Description:  This function will stop the server from running.
#               NOTE:  not working correctly at this time, more work needed
# Arguments:    None
# Return:       None
# *****************************************************************************
def stopServer():
    # grab module level serverRunning for comparison in next line
    global serverRunning

    # if the server is running
    if(serverRunning == True):
        print("Shutting down server. . . ")

        # call function to close
        # https://docs.aiohttp.org/en/stable/web_advanced.html
        # await apprunner.cleanup()

        loop = asyncio.new_event_loop()
        loop.run_until_complete(apprunner.cleanup())
        loop.close()

# *****************************************************************************
# Client Functions
# *****************************************************************************

# *****************************************************************************
# FunctionName: initiateRequest_Blocking
# Description:  This function will initiate a blocking HTTP request out to a server.
# Arguments:    string serverURL - the server URL to hit
#               string sChannel - the channel the message is to be sent on
#               string sMsgName - the name of the particular message we are asking about
#               string sHTTPMethod - the http method.  Can be "put", "get", "post",
#                   or "delete"
#               dictionary queryArgs - a dictionary of any arguments to put into the
#                   query string.  In requestData
#               dictionary bodyJSON - dictionary to be handled as JSON body of request.
#                   In requestData
# Return:       dictionary - if any data is going to be passed back, it should be
#                   passed back here as a python dictionary
#               number - the HTTP response code
# *****************************************************************************
def initiateRequest_Blocking(serverURL, sChannel, sMsgName, sHTTPMethod, **requestData):

    # build the full URL here for ease of use later
    fullURL = serverURL + "/" + sChannel + "/" + sMsgName 

    # log the data and the destination
    logging.info("APIRequest " + fullURL + " " + json.dumps(requestData))

    if(("queryArgs" in requestData) == False and ("bodyJSON" in requestData) == False):
        response = requests.request(sHTTPMethod, fullURL)
    # if query args but no JSON body
    elif(("queryArgs" in requestData) == True and ("bodyJSON" in requestData) == False):
        response = requests.request(sHTTPMethod, fullURL, params=requestData["queryArgs"])
    # if JSON body but no query args
    elif(("queryArgs" in requestData) == False and ("bodyJSON" in requestData) == True):
        response = requests.request(sHTTPMethod, fullURL, json=requestData["bodyJSON"])
    # if we have query args and JSON body
    else:
        response = requests.request(sHTTPMethod, fullURL, params=requestData["queryArgs"], json=requestData["bodyJSON"])
    
    # try to get out the json response if there is one, if not that's ok, just send back empty object
    try:
        jsonResponse = response.json()
    except:
        jsonResponse = {}

    # log the response
    logging.info("APIResponse " + fullURL  + " "+ str(response.status_code) + " " + json.dumps(jsonResponse))

    return jsonResponse, response.status_code

# *****************************************************************************
# FunctionName: initiateRequest_NonBlocking
# Description:  This function will kick off thread for request.
# Arguments:    function callback - the function to call back when response received
#               string serverURL - the server URL to hit
#               string sChannel - the channel the message is to be sent on
#               string sMsgName - the name of the particular message we are asking about
#               string sHTTPMethod - the http method.  Can be "put", "get", "post",
#                   or "delete"
#               dictionary queryArgs - a dictionary of any arguments to put into the
#                   query string.  In requestData
#               dictionary bodyJSON - dictionary to be handled as JSON body of request.
#                   In requestData
# Return:       None
# callback args:dictionary - if any data is going to be passed back, it should be
#                   passed back here as a python dictionary
#               number - the HTTP response code
# *****************************************************************************
def initiateRequest_NonBlocking(callback, serverURL, sChannel, sMsgName, sHTTPMethod, **requestData):

    # kick off new thread by passing it all parameters
    newThread = threading.Thread(
        target=_request_NonBlockingThread, 
        args=(callback, serverURL, sChannel, sMsgName, sHTTPMethod),
        kwargs=requestData
        )
    newThread.start()

# *****************************************************************************
# FunctionName: _request_NonBlockingThread
# Description:  This function will initiate a blocking HTTP request out to a server.
# Arguments:    same as initiateRequest_NonBlocking
# Return:       None
# *****************************************************************************
def _request_NonBlockingThread(callback, serverURL, sChannel, sMsgName, sHTTPMethod, **requestData):

    jsonBody, responseCode = initiateRequest_Blocking(serverURL, sChannel, sMsgName, sHTTPMethod, **requestData)
    callback(jsonBody, responseCode)

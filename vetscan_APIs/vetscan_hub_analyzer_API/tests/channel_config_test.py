import analyzerHUBAPI

sChannel = "Config"

# *****************************************************************************
# /Config/Configuration
# *****************************************************************************

testReturn_GetConfiguration = {
    "ConfigA": "A",
    "ConfigB": "B",
    "ConfigC": "C"
}

# *****************************************************************************
# FunctionName: testHandlerGetConfigConfiguration
# Description:  Test handler for a get request on /Config/Configuration
# Arguments:    dictionary requestVariables - data passed by request
# Return:       dictionary - according to OAS spec and request
#               number - the status code of the response
# *****************************************************************************
def testHandlerGetConfigConfiguration(requestVariables=None):

    # grab once and use multiple times below to simplify code
    if(requestVariables != None):
        configInfoRequested = requestVariables["sPartialConfigurationInformation"]
    else:
        configInfoRequested = None

    if(configInfoRequested == None):
        configToReturn = testReturn_GetConfiguration
        statusToReturn = 200
    elif(configInfoRequested in testReturn_GetConfiguration):
        configToReturn = {configInfoRequested: testReturn_GetConfiguration[configInfoRequested]}
        statusToReturn = 200
    else:
        configToReturn = {
            "detail": "Configuration parameter is unknown",
            "status": 503,
            "title": "Service Unavailable",
            "type": configInfoRequested
            }
        statusToReturn = 503

    return configToReturn, statusToReturn

# *****************************************************************************
# FunctionName: testSendGetConfigConfiguration
# Description:  Test client for /Config/Configuration
# Arguments:    None
# Return:       bool - true if test passed, false if it failed
# *****************************************************************************
def testSendGetConfigConfiguration():
    sMsgName = "Configuration"
    
    # test getting everything
    configInfo, responseCode = analyzerHUBAPI.initiateRequest_Blocking("http://localhost:8080", sChannel, sMsgName, "get")
    
    # test to make sure that the return was what was expected
    testPassed = (configInfo == testReturn_GetConfiguration) and (responseCode == 200)

    # test to make sure each individual config item is returned correctly
    if(testPassed == True):
       # test all correct returns first
        for member in testReturn_GetConfiguration:
            configInfo, responseCode = analyzerHUBAPI.initiateRequest_Blocking(
                "http://localhost:8080", 
                sChannel, 
                sMsgName, 
                "get", 
                queryArgs={"sPartialConfigurationInformation": member}
                )

            # check to make sure return matches what it should be
            testPassed = (configInfo == {member: testReturn_GetConfiguration[member]}) and (responseCode == 200)

            if(testPassed == False):
                break
    
    # if we didn't fail yet, test a bad argument and check for correct failure
    if(testPassed == True):
        partialVersionInfo, responseCode = analyzerHUBAPI.initiateRequest_Blocking(
            "http://localhost:8080", 
            sChannel, 
            sMsgName, 
            "get", 
            queryArgs={"sPartialConfigurationInformation": "veryBad"}
            )

        testPassed = (responseCode == 503)

    print("get: " + sChannel + "/" + sMsgName + (": passed" if testPassed else " failed"))
    
    return testPassed


# *****************************************************************************
# FunctionName: testHandlerPutConfigConfiguration
# Description:  Test handler for a put request on /Config/Configuration
# Arguments:    dictionary configUpdate - data passed by request
# Return:       dictionary - according to OAS spec and request
#               number - the status code of the response
# *****************************************************************************
def testHandlerPutConfigConfiguration(configUpdate):

    error = False

    # loop over every member in configUpdate passed in
    for member in configUpdate:
        # does config item not exist
        if(member in testReturn_GetConfiguration) == False:
            error = True
            memberError = member
            break

    # if no errors found, apply the changes
    if(error == False):
        for member in configUpdate:
            testReturn_GetConfiguration[member] = configUpdate[member]

        statusToReturn = 200
        bodyToReturn = {}
    else:
        bodyToReturn = {
            "detail": "Configuration parameter is unknown",
            "status": 503,
            "title": "Service Unavailable",
            "type": memberError
            }
        statusToReturn = 503

    return bodyToReturn, statusToReturn

# *****************************************************************************
# FunctionName: testSendPutConfigConfiguration
# Description:  Test client for /Config/Configuration
# Arguments:    None
# Return:       bool - true if test passed, false if it failed
# *****************************************************************************
def testSendPutConfigConfiguration():
    sMsgName = "Configuration"

    # test all correct returns first
    for member in testReturn_GetConfiguration:
        responseJSON, responseCode = analyzerHUBAPI.initiateRequest_Blocking(
            "http://localhost:8080", 
            sChannel, 
            sMsgName, 
            "put", 
            bodyJSON={member: member + "_New!"}
            )

        # check to make sure return matches what it should be
        testPassed = (responseJSON == {}) and (responseCode == 200)

        if(testPassed == False):
            break

    if(testPassed == True):
        # now let's try to see if it handles a bad request correctly
        responseJSON, responseCode = analyzerHUBAPI.initiateRequest_Blocking(
                "http://localhost:8080", 
                sChannel, 
                sMsgName, 
                "put", 
                bodyJSON={"bad": "veryBad"}
                )

        # check to make sure return matches what it should be
        testPassed = (responseCode == 503)

    if(testPassed == True):
        # now let's try to see if it handles an empty request correctly
        responseJSON, responseCode = analyzerHUBAPI.initiateRequest_Blocking(
                "http://localhost:8080", 
                sChannel,
                sMsgName,
                "put"
                )

        # check to make sure return matches what it should be
        testPassed = (responseCode == 400)

    print("put: " + sChannel + "/" + sMsgName + (": passed" if testPassed else " failed"))
    
    return testPassed

# *****************************************************************************
# /Config/FullVersion
# *****************************************************************************

testReturn_GetFullVersion = {
    "sAnalyzerID": "14B",
    "sAnalyzerType": "SPE",
    "sAnalyzerSerialNumber": "1111-2222-3333-AAAA-XXX",
    "sAnalyzerSoftwareVersion": "1.0R",
    "sAnalyzerFirmwareVersion": "2.7",
    "sAnalyzerHardwareVersion": "F"
}

# *****************************************************************************
# FunctionName: testHandlerGetConfigFullVersion
# Description:  Test handler for a get request on /Config/FullVersion
# Arguments:    None
# Return:       dictionary
# *****************************************************************************
def testHandlerGetConfigFullVersion():

    return testReturn_GetFullVersion, 200

# *****************************************************************************
# FunctionName: testSendGetConfigFullVersion
# Description:  Test client for /Config/FullVersion
# Arguments:    None
# Return:       bool - true if test passed, false if it failed
# *****************************************************************************
def testSendGetConfigFullVersion():
    sMsgName = "FullVersion"

    fullVersionInfo, responseCode = analyzerHUBAPI.initiateRequest_Blocking("http://localhost:8080", sChannel, sMsgName, "get")
    
    # test to make sure that the return was what was expected
    testPassed = (fullVersionInfo == testReturn_GetFullVersion) and (responseCode == 200)

    print("get: " + sChannel + "/" + sMsgName + (": passed" if testPassed else " failed"))
    
    return testPassed

# *****************************************************************************
# /Config/PartialVersion
# *****************************************************************************

testReturns_GetPartialVersion = {
    "sAnalyzerID": {"sAnalyzerID": "14B"},
    "sAnalyzerType": {"sAnalyzerType": "SPE"},
    "sAnalyzerSerialNumber": {"sAnalyzerSerialNumber": "1111-2222-3333-AAAA-XXX"},
    "sAnalyzerSoftwareVersion": {"sAnalyzerSoftwareVersion": "1.0R"},
    "sAnalyzerFirmwareVersion": {"sAnalyzerFirmwareVersion": "2.7"},
    "sAnalyzerHardwareVersion": {"sAnalyzerHardwareVersion": "F"}
}       

# *****************************************************************************
# FunctionName: testHandlerGetConfigParitalVersion
# Description:  Test server handler for /Config/Partial
# Arguments:    dictionary requestVariables - the query request variables, see 
#                   OAS spec for details
# Return:       dictionary - according to OAS spec and request
#               number - the status code of the response
# *****************************************************************************
def testHandlerGetConfigParitalVersion(requestVariables):
    return testReturns_GetPartialVersion[requestVariables["sPartialVersionInfo"]], 200

# *****************************************************************************
# FunctionName: testSendGetConfigPartialVersion
# Description:  Test handler for a get request on /Config/PartialVersion
# Arguments:    None
# Return:       bool - true if passed, false if there was an error
# *****************************************************************************
def testSendGetConfigPartialVersion():
    sMsgName = "PartialVersion"

    # test all correct returns first
    for member in testReturns_GetPartialVersion:
        partialVersionInfo, responseCode = analyzerHUBAPI.initiateRequest_Blocking(
            "http://localhost:8080", 
            sChannel, 
            sMsgName, 
            "get", 
            queryArgs={"sPartialVersionInfo": member}
            )

        # check to make sure return matches what it should be
        testPassed = (partialVersionInfo == testReturns_GetPartialVersion[member]) and (responseCode == 200)

        if(testPassed == False):
            break

    # if we didn't fail yet, test a bad argument and check for correct failure
    if(testPassed == True):
        partialVersionInfo, responseCode = analyzerHUBAPI.initiateRequest_Blocking(
            "http://localhost:8080", 
            sChannel, 
            sMsgName, 
            "get", 
            queryArgs={"sPartialVersionInfo": "bad"}
            )

        testPassed = (responseCode == 400)

    print("get: " + sChannel + "/" + sMsgName + (": passed" if testPassed else " failed"))
    
    return testPassed

# *****************************************************************************
# Channel Wide Test Code
# *****************************************************************************

# *****************************************************************************
# FunctionName: registerTestHandlers
# Description:  This function will register all test handlers
# Arguments:    None
# Return:       None
# *****************************************************************************
def registerTestHandlers():
    analyzerHUBAPI.registerMessageHandler(sChannel, "PartialVersion", "get", testHandlerGetConfigParitalVersion)
    analyzerHUBAPI.registerMessageHandler(sChannel, "FullVersion", "get", testHandlerGetConfigFullVersion)
    analyzerHUBAPI.registerMessageHandler(sChannel, "Configuration", "get", testHandlerGetConfigConfiguration)
    analyzerHUBAPI.registerMessageHandler(sChannel, "Configuration", "put", testHandlerPutConfigConfiguration)

# *****************************************************************************
# FunctionName: runAllClientTests
# Description:  This function will call all the tests on the client side and confirm
#               the operations.
# Arguments:    None
# Return:       bool - true if all tests pass, false if there was a failure
# *****************************************************************************
def runAllClientTests():
    allTestsPass = testSendGetConfigFullVersion()
    allTestsPass = testSendGetConfigPartialVersion() and allTestsPass
    allTestsPass = testSendGetConfigConfiguration() and allTestsPass
    allTestsPass = testSendPutConfigConfiguration() and allTestsPass

    return allTestsPass
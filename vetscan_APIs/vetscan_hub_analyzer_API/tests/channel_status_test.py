import analyzerHUBAPI

sChannel = "Status"

# *****************************************************************************
# /Status/Operational
# *****************************************************************************

testReturn_OperationalStatus = {
    "sStatus": "Analyzing"
}

# *****************************************************************************
# FunctionName: testHandlerGetStatusOperational
# Description:  Test handler for a get request on /Status/Operational
# Arguments:    dictionary requestVariables - data passed by request
# Return:       dictionary - according to OAS spec and request
#               number - the status code of the response
# *****************************************************************************
def testHandlerGetStatusOperational():
    # return test data
    return testReturn_OperationalStatus, 200

# *****************************************************************************
# FunctionName: testSendGetStatusOperational
# Description:  Test client for /Status/Operational
# Arguments:    None
# Return:       bool - true if test passed, false if it failed
# *****************************************************************************
def testSendGetStatusOperational(): 
    sMsgName = "Operational"

    # test getting operational status
    operationalStatus, responseCode = analyzerHUBAPI.initiateRequest_Blocking("http://localhost:8080", sChannel, sMsgName, "get")
    
    # test to make sure that the return was what was expected
    testPassed = (operationalStatus == testReturn_OperationalStatus) and (responseCode == 200)
    print("get: " + sChannel + "/" + sMsgName + (": passed" if testPassed else " failed"))
    
    return testPassed

# *****************************************************************************
# /Status/GetCurrentlyActivatedEvents
# *****************************************************************************

testReturn_GetCurrentlyActivatedEvents = {
    "aoCurrentlyActivatedEvents": [
        {
            "sActivationTime": "05-05-2021 22:07:04",
            "sSeverity": "Notification",
            "sEventName": "Event1",
            "sEventAdditionalInformation": "This event isn't serious, just letting you know what is happening"
        },
        {
            "sActivationTime": "05-05-2021 23:04:02",
            "sSeverity": "Notification",
            "sEventName": "Event2",
            "sEventAdditionalInformation": "This event is pretty serious and needs attention"
        },
        {
            "sActivationTime": "05-05-2021 23:14:17",
            "sSeverity": "Halt",
            "sEventName": "Event3",
            "sEventAdditionalInformation": "This event very serious.  Until you fix it machine won't work again"
        }
    ]
}

# *****************************************************************************
# FunctionName: testHandlerGetStatusCurrentlyActivatedEvents
# Description:  Test handler for a get request on /Config/FullVersion
# Arguments:    None
# Return:       dictionary
# *****************************************************************************
def testHandlerGetStatusCurrentlyActivatedEvents():

    return testReturn_GetCurrentlyActivatedEvents, 200

# *****************************************************************************
# FunctionName: testSendGetStatusCurrentlyActivatedEvents
# Description:  Test client for /Config/FullVersion
# Arguments:    None
# Return:       bool - true if test passed, false if it failed
# *****************************************************************************
def testSendGetStatusCurrentlyActivatedEvents():
    sMsgName = "CurrentlyActivatedEvents"

    currentlyActivatedEventsInfo, responseCode = analyzerHUBAPI.initiateRequest_Blocking("http://localhost:8080", sChannel, sMsgName, "get")
    
    # test to make sure that the return was what was expected
    testPassed = (currentlyActivatedEventsInfo == testReturn_GetCurrentlyActivatedEvents) and (responseCode == 200)
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
    analyzerHUBAPI.registerMessageHandler(sChannel, "Operational", "get", testHandlerGetStatusOperational)
    analyzerHUBAPI.registerMessageHandler(sChannel, "CurrentlyActivatedEvents", "get", testHandlerGetStatusCurrentlyActivatedEvents)

# *****************************************************************************
# FunctionName: runAllClientTests
# Description:  This function will call all the tests on the client side and confirm
#               the operations.
# Arguments:    None
# Return:       bool - true if all tests pass, false if there was a failure
# *****************************************************************************
def runAllClientTests():
    allTestsPass = testSendGetStatusOperational()
    allTestsPass = testSendGetStatusCurrentlyActivatedEvents() and allTestsPass

    return allTestsPass
import analyzerHUBAPI

sChannel = "Maintenance"

# *****************************************************************************
# /Maintenance/FactoryReset
# *****************************************************************************

# *****************************************************************************
# FunctionName: testHandlerPutMaintenanceFactoryReset
# Description:  Test handler for a put request on /Maintenance/FactoryReset
# Arguments:    None
# Return:       dictionary - according to OAS spec and request
#               number - the status code of the response
# *****************************************************************************
def testHandlerPutMaintenanceFactoryReset():
    return {}, 200

# *****************************************************************************
# FunctionName: testSendPutMaintenanceFactoryReset
# Description:  Test client for /Maintenance/FactoryReset
# Arguments:    None
# Return:       bool - true if test passed, false if it failed
# *****************************************************************************
def testSendPutMaintenanceFactoryReset():
    sMsgName = "FactoryReset"

    responseJSON, responseCode = analyzerHUBAPI.initiateRequest_Blocking(
            "http://localhost:8080", 
            sChannel, 
            sMsgName, 
            "put"
            )

    # check to make sure return matches what it should be
    testPassed = (responseCode == 200)

    print("put: " + sChannel + "/" + sMsgName + (": passed" if testPassed else " failed"))
    
    return testPassed

# *****************************************************************************
# Channel Wide Test Code
# *****************************************************************************

# *****************************************************************************
# FunctionName: registerTestHandlers
# Description:  This function will register all test handlers for the channel
# Arguments:    None
# Return:       None
# *****************************************************************************
def registerTestHandlers():
    analyzerHUBAPI.registerMessageHandler(sChannel, "FactoryReset", "put", testHandlerPutMaintenanceFactoryReset)
    return

# *****************************************************************************
# FunctionName: runAllClientTests
# Description:  This function will call all the tests on the client side and confirm
#               the operations.
# Arguments:    None
# Return:       bool - true if all tests pass, false if there was a failure
# *****************************************************************************
def runAllClientTests():
    allTestsPass = testSendPutMaintenanceFactoryReset()

    return allTestsPass
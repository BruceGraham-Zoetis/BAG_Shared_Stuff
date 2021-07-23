import analyzerHUBAPI

sChannel = "Power"

# *****************************************************************************
# /Power/Reboot, /Power/On, and /Power/Off
# *****************************************************************************

# *****************************************************************************
# FunctionName: testHandlerPutPowerAllMsgs
# Description:  Test handler for a put request on /Power/*
# Arguments:    None
# Return:       dictionary - according to OAS spec and request
#               number - the status code of the response
# *****************************************************************************
def testHandlerPutPowerAllMsgs():
    return {}, 200

# *****************************************************************************
# FunctionName: testSendPutPowerReboot
# Description:  Test client for /Power/*
# Arguments:    None
# Return:       bool - true if test passed, false if it failed
# *****************************************************************************
def testSendPutPowerMsg(sMsgName):

    responseJSON, responseCode = analyzerHUBAPI.initiateRequest_Blocking(
            "http://localhost:8080", 
            sChannel,
            sMsgName,
            "put"
            )

    # check to make sure return matches what it should be
    testPassed = (responseCode == 200)

    if(testPassed == True):
    # test going to the wrong HTTP method
        responseJSON, responseCode = analyzerHUBAPI.initiateRequest_Blocking(
                "http://localhost:8080", 
                sChannel,
                sMsgName,
                "get"
                )

        # check to make sure return matches what it should be
        testPassed = (responseCode == 405)

    print("put: " + sChannel + "/" + sMsgName + (": passed" if testPassed else " failed"))
    
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
    analyzerHUBAPI.registerMessageHandler(sChannel, "Reboot", "put", testHandlerPutPowerAllMsgs)
    analyzerHUBAPI.registerMessageHandler(sChannel, "On", "put", testHandlerPutPowerAllMsgs)
    analyzerHUBAPI.registerMessageHandler(sChannel, "Off", "put", testHandlerPutPowerAllMsgs)
    return

# *****************************************************************************
# FunctionName: runAllClientTests
# Description:  This function will call all the tests on the client side and confirm
#               the operations.
# Arguments:    None
# Return:       bool - true if all tests pass, false if there was a failure
# *****************************************************************************
def runAllClientTests():
    allTestsPass = testSendPutPowerMsg("Reboot")
    allTestsPass = testSendPutPowerMsg("On") and allTestsPass
    allTestsPass = testSendPutPowerMsg("Off") and allTestsPass

    return allTestsPass
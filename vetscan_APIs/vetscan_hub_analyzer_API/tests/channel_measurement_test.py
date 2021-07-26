import analyzerHUBAPI

sChannel = "Measurement"

# *****************************************************************************
# /Measurement/SupportedConsumables
# *****************************************************************************

testReturn_GetSupportedConsumables = {
        "aoSupportedConsumables": [
            {
                "sName": "Consumable1",
                "sUUID": "123456789ABCDE",
                "sType": "Cartridge",
                "sSpecies": "Cat",
                "sDuration_sec": 35,
                "asAssays": [
                    "PT"
                ]
            },
            {
                "sName": "Consumable2",
                "sUUID": "abcdefghijklmnopqrstuvwxyz",
                "sType": "Cartridge",
                "sSpecies": "Dog",
                "sDuration_sec": 35,
                "asAssays": [
                    "aPTT"
                ]
            }
        ]
    }

# *****************************************************************************
# FunctionName: testHandlerGetMeasurementSupportedConsumables
# Description:  Test handler for a get request on /Measurement/SupportedConsumables
# Arguments:    dictionary requestVariables - data passed by request
# Return:       dictionary - according to OAS spec and request
#               number - the status code of the response
# *****************************************************************************
def testHandlerGetMeasurementSupportedConsumables():
    return testReturn_GetSupportedConsumables, 200

# *****************************************************************************
# FunctionName: testSendGetMeasurementSupportedConsumables
# Description:  Test client for /Measurement/SupportedConsumables
# Arguments:    None
# Return:       bool - true if test passed, false if it failed
# *****************************************************************************
def testSendGetMeasurementSupportedConsumables():
    sMsgName = "SupportedConsumables"
    
    # test getting everything
    configInfo, responseCode = analyzerHUBAPI.initiateRequest_Blocking("http://localhost:8080", sChannel, sMsgName, "get")
    
    # test to make sure that the return was what was expected
    testPassed = (configInfo == testReturn_GetSupportedConsumables) and (responseCode == 200)

    print("get: " + sChannel + "/" + sMsgName + (": passed" if testPassed else " failed"))
    
    return testPassed

# *****************************************************************************
# /Measurement/ByScript
# *****************************************************************************

testReturn_PostMeasurementByScript = {
    "sMeasurementID": "Script101",
    "nElapsedTime_msec": 1.3,
    "sMeasurementStatus": "Initializing",
    "sStatusDetail": "It's initializing, nothing else to say"
}

# *****************************************************************************
# FunctionName: testHandlerPostMeasurementByScript
# Description:  Test handler for a post request on /Measurement/ByScript
# Arguments:    dictionary requestBody - according to OAS spec
# Return:       dictionary - according to OAS spec and request
#               number - the status code of the response
# *****************************************************************************
def testHandlerPostMeasurementByScript(requestBody):

    return testReturn_PostMeasurementByScript, 200

# *****************************************************************************
# FunctionName: testSendPostMeasurementByScript
# Description:  Test client for /Measurement/ByScript
# Arguments:    None
# Return:       bool - true if test passed, false if it failed
# *****************************************************************************
def testSendPostMeasurementByScript():
    sMsgName = "ByScript"

    measurementStatus, responseCode = analyzerHUBAPI.initiateRequest_Blocking("http://localhost:8080", 
        sChannel, 
        sMsgName, 
        "post",
        bodyJSON={"sScript": "This is a script, it could be anything.  It could be JSON as string or a simple string"})
    
    # test to make sure that the return was what was expected
    testPassed = (measurementStatus == testReturn_PostMeasurementByScript) and (responseCode == 200)

    print("post: " + sChannel + "/" + sMsgName + (": passed" if testPassed else " failed"))
    
    return testPassed

# *****************************************************************************
# /Measurement/ByFile
# *****************************************************************************

testReturn_PostMeasurementByFile = {
    "sMeasurementID": "File102",
    "nElapsedTime_msec": 15,
    "sMeasurementStatus": "Initializing",
    "sStatusDetail": "JUMANJI!!"
}    

# *****************************************************************************
# FunctionName: testHandlerPostMeasurementByFile
# Description:  Test server handler for /Measurement/ByFile
# Arguments:    dictionary requestBody - according to OAS spec
# Return:       dictionary - according to OAS spec and request
#               number - the status code of the response
# *****************************************************************************
def testHandlerPostMeasurementByFile(requestBody):
    return testReturn_PostMeasurementByFile, 200

# *****************************************************************************
# FunctionName: testSendPostMeasurementByFile
# Description:  Test client for a post request on /Measurement/ByFile
# Arguments:    None
# Return:       bool - true if passed, false if there was an error
# *****************************************************************************
def testSendPostMeasurementByFile():
    sMsgName = "ByFile"

    measurementStatus, responseCode = analyzerHUBAPI.initiateRequest_Blocking("http://localhost:8080", 
        sChannel, 
        sMsgName, 
        "post",
        bodyJSON={"sFilename": "/Full/Path/Of/File.json"})
    
    # test to make sure that the return was what was expected
    testPassed = (measurementStatus == testReturn_PostMeasurementByFile) and (responseCode == 200)

    print("post: " + sChannel + "/" + sMsgName + (": passed" if testPassed else " failed"))
    
    return testPassed

# *****************************************************************************
# /Measurement/Normal
# *****************************************************************************

testReturn_PostMeasurementNormal = {
    "sMeasurementID": "Normal103",
    "nElapsedTime_msec": 99,
    "sMeasurementStatus": "Initializing",
    "sStatusDetail": "Boring old normal"
}    

# *****************************************************************************
# FunctionName: testHandlerPostMeasurementNormal
# Description:  Test server handler for /Measurement/Normal
# Arguments:    dictionary requestBody - according to OAS spec
# Return:       dictionary - according to OAS spec and request
#               number - the status code of the response
# *****************************************************************************
def testHandlerPostMeasurementNormal(requestBody):
    return testReturn_PostMeasurementNormal, 200

# *****************************************************************************
# FunctionName: testSendPostMeasurementNormal
# Description:  Test handler for a post request on /Measurement/Normal
# Arguments:    None
# Return:       bool - true if passed, false if there was an error
# *****************************************************************************
def testSendPostMeasurementNormal():
    sMsgName = "Normal"

    measurementStatus, responseCode = analyzerHUBAPI.initiateRequest_Blocking("http://localhost:8080", 
        sChannel, 
        sMsgName, 
        "post",
        bodyJSON={"sConsumableName": "Lunchables"})
    
    # test to make sure that the return was what was expected
    testPassed = (measurementStatus == testReturn_PostMeasurementNormal) and (responseCode == 200)

    print("post: " + sChannel + "/" + sMsgName + (": passed" if testPassed else " failed"))
    
    return testPassed

# *****************************************************************************
# /Measurement/Status
# *****************************************************************************

testReturn_GetMeasurementStatus = {
    "sMeasurementID": "R2D2",
    "nElapsedTime_msec": 4589,
    "sMeasurementStatus": "Running",
    "sStatusDetail": "Spin Cycle"
    }

# *****************************************************************************
# FunctionName: testHandlerGetMeasurementStatus
# Description:  Test handler for a get request on /Measurement/Status
# Arguments:    dictionary requestVariables - data passed by request
# Return:       dictionary - according to OAS spec and request
#               number - the status code of the response
# *****************************************************************************
def testHandlerGetMeasurementStatus():
    return testReturn_GetMeasurementStatus, 200

# *****************************************************************************
# FunctionName: testSendGetMeasurementStatus
# Description:  Test client for /Measurement/Status
# Arguments:    None
# Return:       bool - true if test passed, false if it failed
# *****************************************************************************
def testSendGetMeasurementStatus():
    sMsgName = "Status"
    
    # test getting everything
    configInfo, responseCode = analyzerHUBAPI.initiateRequest_Blocking("http://localhost:8080", sChannel, sMsgName, "get")
    
    # test to make sure that the return was what was expected
    testPassed = (configInfo == testReturn_GetMeasurementStatus) and (responseCode == 200)

    print("get: " + sChannel + "/" + sMsgName + (": passed" if testPassed else " failed"))
    
    return testPassed

# *****************************************************************************
# /Measurement/Cancel
# *****************************************************************************

testReturn_PostMeasurementCancel = {
    "sMeasurementID": "Cancel104",
    "nElapsedTime_msec": 42,
    "sMeasurementStatus": "Stopping",
    "sStatusDetail": "Whoa nelly!"
}    

# *****************************************************************************
# FunctionName: testHandlerDeleteMeasurementCancel
# Description:  Test server handler for /Measurement/Cancel
# Arguments:    None
# Return:       dictionary - according to OAS spec and request
#               number - the status code of the response
# *****************************************************************************
def testHandlerDeleteMeasurementCancel():
    return testReturn_PostMeasurementCancel, 200

# *****************************************************************************
# FunctionName: testSendDeleteMeasurementCancel
# Description:  Test handler for a delete request on /Measurement/Cancel
# Arguments:    None
# Return:       bool - true if passed, false if there was an error
# *****************************************************************************
def testSendDeleteMeasurementCancel():
    sMsgName = "Cancel"

    measurementStatus, responseCode = analyzerHUBAPI.initiateRequest_Blocking("http://localhost:8080", 
        sChannel, 
        sMsgName, 
        "delete"
    )
    
    # test to make sure that the return was what was expected
    testPassed = (measurementStatus == testReturn_PostMeasurementCancel) and (responseCode == 200)

    print("delete: " + sChannel + "/" + sMsgName + (": passed" if testPassed else " failed"))
    
    return testPassed

# *****************************************************************************
# /Measurement/Result
# *****************************************************************************

testReturn_GetMeasurementResult = {
    "sConsumableName": "string",
    "sStartDateAndTime": "05-05-2021 22:07:04",
    "sEndDateAndTime": "05-05-2021 22:07:55",
    "nDuration_sec": 42,
    "sResult": "Failed",
    "oTestResults": {}
}

# *****************************************************************************
# FunctionName: testHandlerGetMeasurementResult
# Description:  Test handler for a get request on /Measurement/Result
# Arguments:    dictionary requestVariables - data passed by request
# Return:       dictionary - according to OAS spec and request
#               number - the Result code of the response
# *****************************************************************************
def testHandlerGetMeasurementResult():
    return testReturn_GetMeasurementResult, 200

# *****************************************************************************
# FunctionName: testSendGetMeasurementResult
# Description:  Test client for /Measurement/Result
# Arguments:    None
# Return:       bool - true if test passed, false if it failed
# *****************************************************************************
def testSendGetMeasurementResult():
    sMsgName = "Result"
    
    # test getting everything
    configInfo, responseCode = analyzerHUBAPI.initiateRequest_Blocking("http://localhost:8080", sChannel, sMsgName, "get")
    
    # test to make sure that the return was what was expected
    testPassed = (configInfo == testReturn_GetMeasurementResult) and (responseCode == 200)

    print("get: " + sChannel + "/" + sMsgName + (": passed" if testPassed else " failed"))
    
    return testPassed

# *****************************************************************************
# /Measurement/PastResults
# *****************************************************************************

testReturn_GetMeasurementPastResults = {
    "aoMeasurementResults": [
        {
            "sConsumableName": "Muffins",
            "sStartDateAndTime": "05-05-2021 22:07:04",
            "sEndDateAndTime": "05-05-2021 22:07:55",
            "nDuration_sec": 14,
            "sResult": "Completed",
            "oTestResults": {}
        },
        {
            "sConsumableName": "Brownies",
            "sStartDateAndTime": "05-05-2021 22:07:04",
            "sEndDateAndTime": "05-05-2021 22:07:55",
            "nDuration_sec": 28,
            "sResult": "Cancelled",
            "oTestResults": {}
        },
        {
            "sConsumableName": "Cookies",
            "sStartDateAndTime": "05-05-2021 22:07:04",
            "sEndDateAndTime": "05-05-2021 22:07:55",
            "nDuration_sec": 56,
            "sResult": "Completed",
            "oTestResults": {}
        }
    ]
}

# *****************************************************************************
# FunctionName: testHandlerGetMeasurementPastResults
# Description:  Test handler for a get request on /Measurement/PastResults
# Arguments:    dictionary requestVariables - data passed by request
# Return:       dictionary - according to OAS spec and request
#               number - the PastResults code of the response
# *****************************************************************************
def testHandlerGetMeasurementPastResults(body):
    return testReturn_GetMeasurementPastResults, 200

# *****************************************************************************
# FunctionName: testSendGetMeasurementPastResults
# Description:  Test client for /Measurement/PastResults
# Arguments:    None
# Return:       bool - true if test passed, false if it failed
# *****************************************************************************
def testSendGetMeasurementPastResults():
    sMsgName = "PastResults"
    
    # test getting everything
    configInfo, responseCode = analyzerHUBAPI.initiateRequest_Blocking("http://localhost:8080", sChannel, sMsgName, "get",
        queryArgs={
            "sStartTime": "10:10:09",
            "sStartDate": "2021-05-18",
            "sEndTime": "23:59:59",
            "sEndDate": "2021-05-20"
        })
    
    # test to make sure that the return was what was expected
    testPassed = (configInfo == testReturn_GetMeasurementPastResults) and (responseCode == 200)

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
    analyzerHUBAPI.registerMessageHandler(sChannel, "SupportedConsumables", "get", testHandlerGetMeasurementSupportedConsumables)
    analyzerHUBAPI.registerMessageHandler(sChannel, "ByScript", "post", testHandlerPostMeasurementByScript)
    analyzerHUBAPI.registerMessageHandler(sChannel, "ByFile", "post", testHandlerPostMeasurementByFile)
    analyzerHUBAPI.registerMessageHandler(sChannel, "Normal", "post", testHandlerPostMeasurementNormal)
    analyzerHUBAPI.registerMessageHandler(sChannel, "Status", "get", testHandlerGetMeasurementStatus)
    analyzerHUBAPI.registerMessageHandler(sChannel, "Cancel", "delete", testHandlerDeleteMeasurementCancel)
    analyzerHUBAPI.registerMessageHandler(sChannel, "Result", "get", testHandlerGetMeasurementResult)
    analyzerHUBAPI.registerMessageHandler(sChannel, "PastResults", "get", testHandlerGetMeasurementPastResults)
    
# *****************************************************************************
# FunctionName: runAllClientTests
# Description:  This function will call all the tests on the client side and confirm
#               the operations.
# Arguments:    None
# Return:       bool - true if all tests pass, false if there was a failure
# *****************************************************************************
def runAllClientTests():
    allTestsPass = testSendGetMeasurementSupportedConsumables()
    allTestsPass = testSendPostMeasurementByScript() and allTestsPass
    allTestsPass = testSendPostMeasurementByFile() and allTestsPass
    allTestsPass = testSendPostMeasurementNormal() and allTestsPass
    allTestsPass = testSendGetMeasurementStatus() and allTestsPass
    allTestsPass = testSendDeleteMeasurementCancel() and allTestsPass
    allTestsPass = testSendGetMeasurementResult() and allTestsPass
    allTestsPass = testSendGetMeasurementPastResults() and allTestsPass

    return allTestsPass
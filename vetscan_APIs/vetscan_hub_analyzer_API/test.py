import sys, os
sys.path.append(os.path.dirname(__file__))
import analyzerHUBAPI

import time
import logging

# grab all the tests
from tests import channel_config_test
from tests import channel_remote_control_test
from tests import channel_maintenance_test
from tests import channel_power_test
from tests import channel_status_test
from tests import channel_measurement_test

asyncTestPassed = False

# *****************************************************************************
# FunctionName:   ReceiveFullVersion
# Description:    This function will receive response from async call to get 
#                 full version
# Arguments:      dictionary versionInfo - should contain the information back
#                    from the response with all version info
#                 number responseCode - should contain number of status code
#                    from the response
# Return:         None
# *****************************************************************************
def ReceiveFullVersion(versionInfo, responseCode):
   # use module level to get state out asynchronously
   global asyncTestPassed

   #check response against expected and then print result to screen
   asyncTestPassed = (responseCode == 200)
   print("async get: /Config/FullVersion"+ (": passed" if asyncTestPassed else " failed"))

# *****************************************************************************
# Mainline executable code
# *****************************************************************************

logging.basicConfig(filename="example.log", level=logging.DEBUG)

# call function to start the server
analyzerHUBAPI.startServer_NonBlocking()

# register handlers
channel_config_test.registerTestHandlers()
channel_remote_control_test.registerTestHandlers()
channel_maintenance_test.registerTestHandlers()
channel_power_test.registerTestHandlers()
channel_status_test.registerTestHandlers()
channel_measurement_test.registerTestHandlers()

# wait for server to come up
time.sleep(2)

# perform non blocking client request first
analyzerHUBAPI.initiateRequest_NonBlocking(ReceiveFullVersion, "http://localhost:8080", "Config", "FullVersion", "get")

# begin tests by hitting the server through client calls on each channel
allPassed = channel_config_test.runAllClientTests()
allPassed = channel_remote_control_test.runAllClientTests() and allPassed
allPassed = channel_maintenance_test.runAllClientTests() and allPassed
allPassed = channel_power_test.runAllClientTests() and allPassed
allPassed = channel_status_test.runAllClientTests() and allPassed
allPassed = channel_measurement_test.runAllClientTests() and allPassed

# now combine with async test for final result
allPassed = allPassed and asyncTestPassed

print("*******************************************************")
print("Test Results")
print("*******************************************************")
print("All tests passed" if allPassed else "One or more tests failed")

# call function to stop the server so we can gracefully exit
# todo:  not working yet, fix this later
# analyzerHUBAPI.stopServer()

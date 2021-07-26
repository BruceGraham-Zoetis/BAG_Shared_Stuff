import time
import json
from vetscan_hub_analyzer_API import analyzerHUBAPI

# *****************************************************************************
# Client function that receives the message
# *****************************************************************************
def ReceiveFullVersion(versionInfo, responseCode):
   print("versionInfo: " + json.dumps(versionInfo))
   print("responseCode: " + str(responseCode))

# *****************************************************************************
# Mainline executable code
# *****************************************************************************

# perform non blocking client request and wait for server to handle, should 405 fail
analyzerHUBAPI.initiateRequest_NonBlocking(ReceiveFullVersion, "http://localhost:8080", "Config", "FullVersion", "get")
time.sleep(2)

# now register handler and perform a blocking call, perform non blocking client request first
versionInfo, responseCode = analyzerHUBAPI.initiateRequest_Blocking("http://localhost:8080", "Config", "FullVersion", "get")
print("Blocking versionInfo: " + json.dumps(versionInfo))
print("Blocking responseCode: " + str(responseCode))

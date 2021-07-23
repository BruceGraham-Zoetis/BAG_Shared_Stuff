import time
import json
import sys, os
sys.path.append(os.path.dirname(__file__) + "/vetscan_hub_analyzer_API")
import analyzerHUBAPI

# *****************************************************************************
# Client function that receives the message
# *****************************************************************************
def ReceiveFullVersion(versionInfo, responseCode):
   print("versionInfo: " + json.dumps(versionInfo))
   print("responseCode: " + str(responseCode))

# *****************************************************************************
# Server function that receives request and responds
# *****************************************************************************
def FullVersionHandler():

   testReturn_GetFullVersion = {
      "sAnalyzerID": "14B",
      "sAnalyzerType": "SPE",
      "sAnalyzerSerialNumber": "1111-2222-3333-AAAA-XXX",
      "sAnalyzerSoftwareVersion": "1.0R",
      "sAnalyzerFirmwareVersion": "2.7",
      "sAnalyzerHardwareVersion": "F"
   }

   return testReturn_GetFullVersion, 200

# *****************************************************************************
# Mainline executable code
# *****************************************************************************

# call function to start the server
analyzerHUBAPI.startServer_NonBlocking()
analyzerHUBAPI.registerMessageHandler("Config", "FullVersion", "get", FullVersionHandler)
time.sleep(2)


# perform non blocking client request and wait for server to handle, should 405 fail
analyzerHUBAPI.initiateRequest_NonBlocking(ReceiveFullVersion, "http://localhost:8080", "Config", "FullVersion", "get")
time.sleep(2)

# now register handler and perform a blocking call, perform non blocking client request first
versionInfo, responseCode = analyzerHUBAPI.initiateRequest_Blocking("http://localhost:8080", "Config", "FullVersion", "get")
print("Blocking versionInfo: " + json.dumps(versionInfo))
print("Blocking responseCode: " + str(responseCode))

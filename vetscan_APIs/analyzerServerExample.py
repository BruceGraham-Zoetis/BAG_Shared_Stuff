import time
import json
import sys, os
sys.path.append(os.path.dirname(__file__) + "/vetscan_hub_analyzer_API")
import analyzerHUBAPI

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


def LightBlinkHandler():
   LightBlinkHandler_msg = {
      "Light": "Blinking"
      }

   return LightBlinkHandler_msg, 200

def LightOffHandler():
   LightOffHandler_msg = {
      "Light": "Off"
      }

   return LightOffHandler_msg, 200
# *****************************************************************************
# Mainline executable code
# *****************************************************************************

# call function to start the server
analyzerHUBAPI.startServer_NonBlocking()
analyzerHUBAPI.registerMessageHandler("Config", "FullVersion", "get", FullVersionHandler)
analyzerHUBAPI.registerMessageHandler("RemoteControl", "LightBlink", "put", LightBlinkHandler)
analyzerHUBAPI.registerMessageHandler("RemoteControl", "LightOff", "put", LightOffHandler)

while True:
   time.sleep(2)
   print("Still running. . . ")

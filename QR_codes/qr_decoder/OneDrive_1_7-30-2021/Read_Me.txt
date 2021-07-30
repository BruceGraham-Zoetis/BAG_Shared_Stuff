How to manually control 1W LED Flash of SJ5050A12 under Linux Platforms

1W LED Flash is maunually turned on/off via GPIO2.
With input of backend register 0x2041, 0x2043 bit 2
"1" is to turn on
"0" is to turn off


1. Please unzip "SP_V4L2_API-2021-07-19"
2. Make "Demo_V4L2" within the file
3. Main executive file is generated
4. Confirm the node of SJ5050A12 (/dev/video#) under the Main. Example is as following

"""
test code logic

def getNextTry(iLow : int, iHigh : int, iTried : int, bToHigh : bool) -> int:
    if (bToHigh):
        # try between iLow and iTried
        # iLow:10 + iTried:20 / 2 = 15
        return (iLow + iTried) // 2
    else:
        # try between iTried and iHigh
        # iTried:20 + iHigh:30 / 2 = 25
        return (iTried + iHigh) // 2

iTry = 10
iLow = 0
iHigh = 5000

def tryEncoding(iDataLength : int) -> bool:
    if (iDataLength <= 3333): 
        return True
    else:
        return False

while (True): 
    if (tryEncoding(iTry)): 
        # try between iTry and iHigh
        # iTry:20 + iHigh:30 / 2 = 25
        iLow = iTry
        iTried = iTry
        iTry = (iTry + iHigh) // 2
        print("fit " + str(iTried) + "  Try " + str(iTry))
        if ((iTried + 1) == iHigh):
            print("Found " + str(iLow))
            break
    else:
        # try between iLow and iTry
        # iLow:10 + iTry:20 / 2 = 15
        iHigh = iTry
        iTried = iTry
        iTry = (iLow + iTry) // 2
        print("big " + str(iTried) + "  Try " + str(iTry))
exit()
"""

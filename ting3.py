tmp = "_CHECK_ARG(NULL != %s);"

listT = [
"szIP",
"szIPLen",
"szMask",
"szMaskLen",
"szGateWay",
"szGateWayLen",
"szMac",
"szMacLen"]

for item in listT:
    print tmp %(item)

#coding utf-8

lt = [
    "ObservedFrames",
"Confidence",
"FirstCharConf",
"AmbientLight",
"PlateLight",
"PlateVariance",
"RoadNumber",
"PlateLightType",
"CplStatus",
    ]

tRe = r'''re%s = re.compile(r'<%s value=\"(.*?)\"', re.M)
'''

t = r'''
%s = ""
result%s = re%s.findall(lineFull)
if len(result%s) != 0:
    %s = result%s[0]'''

for item in lt:
    print tRe %(item, item)
    #print t %(item, item, item, item, item, item )
    #print item + ", ",

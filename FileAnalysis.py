#-*- coding: gb18030 -*-
import os  
import re
import shutil 

#print os.path.abspath(os.curdir)


'''
读取所有的文件名  ok!
根据文件名分组(key   时间  cardID 序号)  ok!
读取xml，解析车牌信息   ok!
根据xml生成新的文件  !
重命名文件到新目录  ok!
把信息插入数据库  
'''



sourceDir = r"J:/Download/hvdeviceNewTestResult/sourceTest0"
desDir = r"J:/Download/hvdeviceNewTestResult/sourceTest0New"

listFile =[]
distFileGroup = {}


distCarID = {}
distTime = {}

if  not os.path.exists(desDir):
	os.makedirs(desDir)

tmpInf = r'''
有效帧数:%s
平均可信度:%s
首字可信度:%s
环境亮度:%s
车牌亮度:%s
车牌对比度:%s
车辆类型:小
车道:%s
起始车道号:<左,0>
路口名称:NULL
路口方向:NULL
压线:无
越线:无
摄像机亮度等级:%s
偏光镜状态:%s
结果类型:实时
'''	
	
print "你妹。。。"	
	
for x in os.listdir(sourceDir):
	fileName = os.path.join(sourceDir,x)
	if os.path.isfile(fileName):
		file_path = os.path.split(fileName) #分割出目录与文件
		#lists = file_path[1].split('.') #分割出文件与文件扩展名
		#file_ext = lists[-1] #取出后缀名(列表切片操作)
		#print file_path
		#print lists
		#print file_ext

		keyList = file_path[1].split('_')
		if len(keyList) < 3:
			continue
		key = keyList[0] + keyList[1] #card + time
		#print key, file_path[1]
		if key not in distFileGroup:
			listTemp = []
			listTemp.append(file_path[1])
			distFileGroup[key] = listTemp
		else:
			listTemp = distFileGroup[key]
			listTemp.append(file_path[1])
			distFileGroup[key] = listTemp
			
		if key not in distCarID:
			distCarID[key] = keyList[0]

			
		if key not in distTime:
			distTime[key] = keyList[1]
			
			


rePlate = re.compile(r'<PlateName>(.*?)</PlateName>', re.M)

reObservedFrames = re.compile(r'<ObservedFrames value=\"(.*?)\"', re.M)
reConfidence = re.compile(r'<Confidence value=\"(.*?)\"', re.M)
reFirstCharConf = re.compile(r'<FirstCharConf value=\"(.*?)\"', re.M)
reAmbientLight = re.compile(r'<AmbientLight value=\"(.*?)\"', re.M)
rePlateLight = re.compile(r'<PlateLight value=\"(.*?)\"', re.M)
rePlateVariance = re.compile(r'<PlateVariance value=\"(.*?)\"', re.M)
reRoadNumber = re.compile(r'<RoadNumber value=\"(.*?)\"', re.M)
rePlateLightType = re.compile(r'<PlateLightType value=\"(.*?)\"', re.M)
reCplStatus = re.compile(r'<CplStatus value=\"(.*?)\"', re.M)


#rePlate = re.compile(r'.*')
for key in distFileGroup:
	#print key, distFileGroup[key]
	for item in distFileGroup[key]:
		fileName = os.path.join(sourceDir,item)
		#print item
		if 'xml' in item:
			#print item			
			#print fileName
			f = open(fileName, "r")
			lineFull = f.read()
			#print lineFull
			result = rePlate.findall(lineFull)
			#print result

			#lines = f.readlines()
			#print lines			
			#for line in lines:
				#match = rePlate.match(line)
				#if match:
					#print match.group(1)
					#print "good! bingoo"
			f.close()
			
			#if 'J837' in result[0]:
				#print result[0]
				#print fileName
				
			# plate
			fileNameNew = distTime[key] + "-00000" + distCarID[key] + ".txt"
			fullfileNameNew = os.path.join(desDir,fileNameNew)
			#print result[0]#print fullfileNameNew
			f = open(fullfileNameNew, "w+")
			f.write(result[0])
			f.close()
			
			ObservedFrames = ""
			resultObservedFrames = reObservedFrames.findall(lineFull)
			if len(resultObservedFrames) != 0:
				ObservedFrames = resultObservedFrames[0]

			Confidence = ""
			resultConfidence = reConfidence.findall(lineFull)
			if len(resultConfidence) != 0:
				Confidence = resultConfidence[0]

			FirstCharConf = ""
			resultFirstCharConf = reFirstCharConf.findall(lineFull)
			if len(resultFirstCharConf) != 0:
				FirstCharConf = resultFirstCharConf[0]

			AmbientLight = ""
			resultAmbientLight = reAmbientLight.findall(lineFull)
			if len(resultAmbientLight) != 0:
				AmbientLight = resultAmbientLight[0]

			PlateLight = ""
			resultPlateLight = rePlateLight.findall(lineFull)
			if len(resultPlateLight) != 0:
				PlateLight = resultPlateLight[0]

			PlateVariance = ""
			resultPlateVariance = rePlateVariance.findall(lineFull)
			if len(resultPlateVariance) != 0:
				PlateVariance = resultPlateVariance[0]

			RoadNumber = ""
			resultRoadNumber = reRoadNumber.findall(lineFull)
			if len(resultRoadNumber) != 0:
				RoadNumber = resultRoadNumber[0]

			PlateLightType = ""
			resultPlateLightType = rePlateLightType.findall(lineFull)
			if len(resultPlateLightType) != 0:
				PlateLightType = resultPlateLightType[0]

			CplStatus = ""
			resultCplStatus = reCplStatus.findall(lineFull)
			#print len(resultCplStatus)
			if len(resultCplStatus) !=  0:
				CplStatus = resultCplStatus[0]
				#print lineFull
			
			# inf
			fileNameNew = distTime[key] + "-00000" + distCarID[key] + ".inf"
			fullfileNameNew = os.path.join(desDir,fileNameNew)
			#print result[0]#print fullfileNameNew
			inf = tmpInf   %(ObservedFrames,  Confidence,  FirstCharConf,  AmbientLight,  PlateLight,  PlateVariance,  RoadNumber,  PlateLightType,  CplStatus)
			#print inf
			f = open(fullfileNameNew, "w+")			
			f.write(inf)
			f.close()
			
		else:
			#big picture
			###shutil.copy2(myfile, os.path.join(d, myfile))  
			fileNameNew = distTime[key] + "-00000" + distCarID[key] + "-1.jpg"
			fullfileNameNew = os.path.join(desDir,fileNameNew)
			#print fullfileNameNew
			shutil.copy2(fileName, fullfileNameNew)  
			



#coding=gbk
#access mdb
'''
import win32com.client   
conn = win32com.client.Dispatch(r'ADODB.Connection')   
DSN = 'PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE=C:/test2.mdb;'  
conn.Open(DSN)
rs = win32com.client.Dispatch(r'ADODB.Recordset')
rs.Cursorlocation=3
rs_name = 'select * from test'#表名   
rs.Open('[' + rs_name + ']', conn, 1, 3) 
rs.MoveFirst()
for x in range(rs.RecordCount):
    if rs.EOF:
        print "End of records"
        break
    else:
        print rs.Fields.Item(0).Value,rs.Fields.Item(1).Value,rs.Fields.Item(2).Value
        rs.MoveNext()
rs.Close()
conn.Close()
'''
				
	
'''
Python操作Access数据库步骤之1、建立数据库连接

import win32com.client   
conn = win32com.client.Dispatch(r'ADODB.Connection')   
DSN = 'PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE=C:/MyDB.mdb;'   
conn.Open(DSN) 
Python操作Access数据库步骤之2、打开一个记录集

rs = win32com.client.Dispatch(r'ADODB.Recordset')   
rs_name = 'MyRecordset'#表名   
rs.Open('[' + rs_name + ']', conn, 1, 3) 
Python操作Access数据库步骤之3、对记录集操作

rs.AddNew()   
rs.Fields.Item(1).Value = 'data'   
rs.Update() 
Python操作Access数据库步骤之4、用SQL来插入或更新数据

conn = win32com.client.Dispatch(r'ADODB.Connection')   
DSN = 'PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE=C:/MyDB.mdb;'   
sql_statement = "Insert INTO [Table_Name] ([Field_1], 
[Field_2]) VALUES ('data1', 'data2')"   
conn.Open(DSN)   
conn.Execute(sql_statement)   
conn.Close() 
Python操作Access数据库步骤之5、遍历记录

rs.MoveFirst()   
count = 0   
while 1:   
if rs.EOF:   
break   
else:   
countcount = count + 1   
rs.MoveNext() 
注意：如果一个记录是空的，那么将指针移动到第一个记录将导致一个错误，因为此时recordcount是无效的。解决的方法是：打开一个记录集之前，先将Cursorlocation设置为3，然后再打开记录集，此时recordcount将是有效的。例如：

rs.Cursorlocation = 3 # don't use parenthesis here   
rs.Open('Select * FROM [Table_Name]', conn) # be sure conn is open   
rs.RecordCount # no parenthesis here either 
'''		




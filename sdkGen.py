#
#-*- coding: gbk -*-
#print('Hello World')

listSDK = []
listSDK.append([ "SetF1TriggerOut",     "SETTER",     "INTARRAY1D",  "nEnable, nCoupling, nOutputType, nPolarity, nPulseWidth", "����F1ץ�����" ])
listSDK.append([ "GetF1TriggerOut",     "GETTER",     "INTARRAY1D",  "pnEnable, pnCoupling, pnOutputType, pnPolarity, pnPulseWidth", "��ȡF1ץ�����" ])
listSDK.append([ "SetAlarmTriggerOut",     "SETTER",     "INTARRAY1D",  "nEnable, nCoupling, nOutputType, nPolarity, nPulseWidth", "����ALM��ץ�����" ])
listSDK.append([  "GetAlarmTriggerOut",     "GETTER",     "INTARRAY1D", "pnEnable, pnCoupling, pnOutputType, pnPolarity, pnPulseWidth",   "��ȡALM��ץ�����" ])


DARRAYSETHeaderDeclaration = '''
/**
* @brief                %s
* @param[in]    hHandle                 ��Ӧ�豸����Ч���     
* @return               �ɹ���S_OK��ʧ�ܣ�E_FAIL
*/
HV_API_EX HRESULT CDECL HVAPI_%s_Legacy(HVAPI_HANDLE_EX hHandle, %s );
'''


DARRAYGETHeaderDeclaration = '''
/**
* @brief                %s
* @param[in]    hHandle                 ��Ӧ�豸����Ч���   
* @return               �ɹ���S_OK��ʧ�ܣ�E_FAIL
*/
HV_API_EX HRESULT CDECL HVAPI_%s_Legacy(HVAPI_HANDLE_EX hHandle, %s );
'''

DARRAYSETDefinition = '''
HV_API_EX HRESULT CDECL HVAPI_%s_Legacy(HVAPI_HANDLE_EX hHandle, %s)
{
	%s

	return Default_Setter_INTARRAY1D_ForMercuryProtocol(hHandle, "%s" ,rgValue, %d);
}
'''

DARRAYGETDefinition = '''
HV_API_EX HRESULT CDECL HVAPI_%s_Legacy(HVAPI_HANDLE_EX hHandle, %s)
{
	if (%s)
	{
		return S_FALSE;
	}
	INT rgValue[%d];
	HRESULT ret=Default_Getter_INTARRAY1D_ForMercuryProtocol(hHandle, "%s", rgValue, %d);
        %s
	return ret;
}
'''

#listSDK.append([  "GetAlarmTriggerOut",     "GETTER",     "INTARRAY1D", "pnEnable, pnCoupling, pnOutputType, pnPolarity, pnPulseWidth",   "��ȡALM��ץ�����" ])
for item in listSDK:
    if item[1] == "SETTER" :
        listParam = item[3].split(',')
        strListParam = "INT "+ ", INT ".join(listParam)
       
        print DARRAYSETHeaderDeclaration   %(item[4], item[0], strListParam)
    else:
        listParam = item[3].split(',')
        strListParam = "INT* "+ ", INT* ".join(listParam)
        
        print DARRAYGETHeaderDeclaration   %(item[4], item[0], strListParam)


for item in listSDK:
    if item[1] == "SETTER" :
        listParam = item[3].split(',')
        strListParam = "INT "+ ", INT ".join(listParam)

        strSetList = "INT rgValue[%d];\n"  %(len(listParam))
        for index in range(0, len(listParam)):
            strSetList += "rgValue[%d] = %s;\n" %(index, listParam[index])
           
        print DARRAYSETDefinition   %(item[0], strListParam, strSetList, item[0], len(listParam) )
    else:
        listParam = item[3].split(',')
        strListParam = "INT* "+ ", INT* ".join(listParam)

        listNULL = ""
        for itemParam in listParam:
            listNULL += " NULL == %s|| " %(itemParam)

        strSetList = ""
        for index in range(0, len(listParam)):
            strSetList += "*%s = rgValue[%d];\n" %(listParam[index], index)
        
        print DARRAYGETDefinition   %(item[0], strListParam, listNULL, len(listParam), item[0],  len(listParam), strSetList)

#listCmd = ["CmdName", "SetOrGet", "DateType", "ParamName" ]
listCmd = [
    ["SetJpegOutType", "SET", "INT", "nMode"],
    ["GetJpegOutType", "GET", "INT", "pnMode"],
    ["SetCoilEnable", "SET", "INT", "nMode"],
    ["GetCoilEnable", "GET", "INT", "pnMode"],

    ]

ShellSet = '''
HV_API_EX HRESULT CDECL HVAPI_%s(HVAPI_HANDLE_EX hHandle, %s %s )
{
	_CHECK_HANDKE(hHandle);       
	
	if (_IsLegacy(pHHC))
	{
		return HVAPI_%s_Legacy( hHandle, %s);
	}
	else
	{
		return pHHC->pAgent->GetDeviceManager()->%s(%s);
	}
}
'''
ShellGet = '''
HV_API_EX HRESULT CDECL HVAPI_%s(HVAPI_HANDLE_EX hHandle, %s* %s )
{
	_CHECK_HANDKE(hHandle);       
	
	if (_IsLegacy(pHHC))
	{
		return HVAPI_%s_Legacy( hHandle, %s);
	}
	else
	{
		return pHHC->pAgent->GetDeviceManager()->%s(%s);
	}
}
'''
DoSet = '''
HRESULT CHvDeviceManager::%s(%s %s)
{
	CHAR szArg[32] = {0};	
	sprintf(szArg, "#d", %s);

	_EXEC_XML_CMD("%s", szArg, CLASS_%sTER, DATA_TYPE_%s, DEFAULT_RECV_TIMEOUT_MS);
	
	_RETURN();
}
'''
DoGet='''
HRESULT CHvDeviceManager::%s(%s* %s)
{
	_CHECK_ARG(NULL != %s);

	_EXEC_XML_CMD("%s", NO_ARG, CLASS_%sTER, DATA_TYPE_%s, DEFAULT_RECV_TIMEOUT_MS);

	if (_EXEC_CMD_SUCCEEDED())
	{
		*%s = atoi(_GET_RETMSG());
	}
	
	_RETURN();		
}
'''
for item in listCmd:
    if item[1] == 'SET':
        print ShellSet %(item[0], item[2], item[3], item[0], item[3], item[0], item[3])
    else:
        print ShellGet %(item[0], item[2], item[3], item[0], item[3], item[0], item[3])

        
for item in listCmd:
    if item[1] == 'SET':
        print DoSet %(item[0], item[2], item[3], item[3], item[0], item[1], item[2])
    else:
        print DoGet %(item[0], item[2], item[3], item[3], item[0], item[1], item[2], item[3])
        

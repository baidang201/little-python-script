#-*- coding: cp936 -*-

listSDK = []
'''
listSDK.append([ "HVAPI_TuneZoomAdv",     "TuneZoom",     "SETTER",     "INT",     "���ý���ֵ" ])
listSDK.append([ "HVAPI_TuneFocusAdv",     "TuneFocus",     "SETTER",     "INT",     "���þ۽�" ])
listSDK.append([ "HVAPI_TuneIrisAdv",     "TuneIris",     "SETTER",     "INT",     "���ù�Ȧ" ])
listSDK.append([ "HVAPI_SetIRCUTAdv",     "SetIRCUT",     "SETTER",     "INT",     "���ú����л���" ])
listSDK.append([ "HVAPI_SwitchFPGAAdv",     "SwitchFPGA",     "SETTER",     "INT",     "����FPGAģʽ" ])  # ����ʱ
listSDK.append([ "HVAPI_SetSwitchLEDAdv",     "SetSwitchLED",     "SETTER",     "INT",     "����LED�����" ])
listSDK.append([ "HVAPI_SetPMTagAdv",     "SetPMTag",     "SETTER",     "STRING",     "����λ��" ])
listSDK.append([ "HVAPI_GetPMTagAdv",     "GetPMTag",     "GETTER",     "STRING",     "��ȡλ��" ])
listSDK.append([ "HVAPI_SetPMMainSNAdv",     "SetPMMainSN",     "SETTER",     "STRING",     "���������к�" ])  #������
listSDK.append([ "HVAPI_GetPMMainSNAdv",     "GetPMMainSN",     "GETTER",     "STRING",     "��ȡ�����к�" ])
listSDK.append([ "HVAPI_GetGPSInfoAdv",     "GetGPSInfo",     "GETTER",     "STRING",     "��ȡ������Ϣ" ])

listSDK.append([ "HVAPI_ResetCoilTiggerCount",     "ResetCoilTiggerCount",     "SETTER",     "NULL",     "������Ȧ��������" ])
listSDK.append([ "HVAPI_GetCoilTiggerCount",     "GetCoilTiggerCount",     "GETTER",     "INT",     "��ȡ��Ȧ��������" ])
listSDK.append([ "HVAPI_AutoTestIOAdv",     "AutoTestIO",     "SETTER",     "NULL",     "�Զ���IO����" ])
'''

listSDK.append([ "HVAPI_StartAutoTestIOAdv",     "StartAutoTestIOAdv",     "SETTER",     "STRING",     "�����Զ���IO����" ])
listSDK.append([ "HVAPI_GetAutoTestIOAdvStatusAdv",     "GetAutoTestIOAdvStatus",     "GETTER",     "STRING",     "��ȡ�Զ���IO����״̬������" ])


NULLSETHeaderDeclaration = '''
/**
* @brief                %s
* @param[in]    szIP                 ��Ӧ�豸��IP     
* @return               �ɹ���S_OK��ʧ�ܣ�E_FAIL
*/
HV_API_EX HRESULT CDECL %s(CHAR* szIP);
'''

BOOLSETHeaderDeclaration = '''
/**
* @brief                %s
* @param[in]    szIP                 ��Ӧ�豸��IP     
* @param[in]    fEnable    
* @return               �ɹ���S_OK��ʧ�ܣ�E_FAIL
*/
HV_API_EX HRESULT CDECL %s(CHAR* szIP, BOOL fEnable);
'''

INTSETHeaderDeclaration = '''
/**
* @brief                %s
* @param[in]    szIP                 ��Ӧ�豸��IP     
* @param[in]    nValue
* @return               �ɹ���S_OK��ʧ�ܣ�E_FAIL
*/
HV_API_EX HRESULT CDECL %s(CHAR* szIP, INT nValue );
'''

STRINGSETHeaderDeclaration = '''
/**
* @brief                %s
* @param[in]    szIP                 ��Ӧ�豸��IP     
* @param[in]    szValue
* @return               �ɹ���S_OK��ʧ�ܣ�E_FAIL
*/
HV_API_EX HRESULT CDECL %s(CHAR* szIP, CHAR* szValue );
'''

BOOLGETHeaderDeclaration = '''
/**
* @brief                %s
* @param[in]    szIP                 ��Ӧ�豸��IP
* @param[out]    pfValue     
* @return               �ɹ���S_OK��ʧ�ܣ�E_FAIL
*/
HV_API_EX HRESULT CDECL %s(CHAR* szIP, BOOL* pfEnable);
'''

INTGETHeaderDeclaration = '''
/**
* @brief                %s
* @param[in]    szIP                 ��Ӧ�豸��IP   
* @param[out]    pnValue   
* @return               �ɹ���S_OK��ʧ�ܣ�E_FAIL
*/
HV_API_EX HRESULT CDECL %s(CHAR* szIP, INT* pnValue );
'''

STRINGGETHeaderDeclaration = '''
/**
* @brief                %s
* @param[in]    szIP                 ��Ӧ�豸��IP   
* @param[out]    pnValue   
* @return               �ɹ���S_OK��ʧ�ܣ�E_FAIL
*/
HV_API_EX HRESULT CDECL %s(CHAR* szIP, CHAR* szValue, INT* pnValue );
'''





NULLSETDefinition = '''
HV_API_EX HRESULT CDECL %s(CHAR* szIP)
{
         return Default_Setter_Int_ForMercuryProtocolAdv(szIP, "%s", 0);
}

'''

BOOLSETDefinition = '''
HV_API_EX HRESULT CDECL %s(CHAR* szIP, BOOL fValue )
{
         return Default_Setter_Bool_ForMercuryProtocolAdv(szIP, "%s", fValue);
}
'''

INTSETDefinition = '''
HV_API_EX HRESULT CDECL %s(CHAR* szIP, INT nValue )
{
         return Default_Setter_Int_ForMercuryProtocolAdv(szIP, "%s", nValue);
}
'''

STRINGSETDefinition = '''
HV_API_EX HRESULT CDECL %s(CHAR* szIP, CHAR* szValue  )
{
         return Default_Setter_String_ForMercuryProtocolAdv(szIP, "%s", szValue);
}
'''

BOOLGETDefinition = '''
HV_API_EX HRESULT CDECL %s(CHAR* szIP, BOOL* pfEnable)
{
     return Default_Getter_Bool_ForMercuryProtocolAdv(szIP, "%s", pfEnable);
}
'''

INTGETDefinition = '''
HV_API_EX HRESULT CDECL %s(CHAR* szIP, INT* pnValue )
{
         return Default_Getter_Int_ForMercuryProtocolAdv(szIP, "%s", pnValue);
}
'''

STRINGGETDefinition = '''
HV_API_EX HRESULT CDECL %s(CHAR* szIP, CHAR* szValue, INT* pnValue )
{
         return Default_Getter_String_ForMercuryProtocolAdv(szIP, "%s", szValue, pnValue);
}
'''

#######################Csharp#

CSHARPNULLSETDefinition = '''
[DllImport("HvDevice.dll", EntryPoint = "%s", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.Cdecl)]
static extern HRESULT %s(string szIP);
                public static Boolean %sAdv(string szIP)
                {
                    HRESULT res = %s(szIP);
                    //LogToolsEx.Info2File(DEVICESDKLOG, "%s:res={0}",  res);
                    return res == HRESULT.S_OK;
                }
'''

CSHARPINTSETDefinition = '''
[DllImport("HvDevice.dll", EntryPoint = "%s", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.Cdecl)]
static extern HRESULT %s(string szIP, int nValue );
                public static Boolean %sAdv(string szIP, int nValue)
                {
                    HRESULT res = %s(szIP, nValue);
                    //LogToolsEx.Info2File(DEVICESDKLOG, "%s:nValue={0} res={1}", nValue, res);
                    return res == HRESULT.S_OK;
                }
'''

CSHARPSTRINGSETDefinition = '''
[DllImport("HvDevice.dll", EntryPoint = "%s", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.Cdecl)]
static extern HRESULT %s(string szIP, string szValue  );
                public static Boolean %sAdv(string szIP, string szValue  )
                {
                    HRESULT res = %s(szIP, szValue);
                    //LogToolsEx.Info2File(DEVICESDKLOG, "%s:nValue={0} res={1}", nValue, res);
                    return res == HRESULT.S_OK;
                }
'''

CSHARPINTGETDefinition = '''
[DllImport("HvDevice.dll", EntryPoint = "%s", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.Cdecl)]
static extern HRESULT %s(string szIP, ref int pnValue );
                public static Boolean %sAdv(string szIP, ref int nValue)
                {
                    HRESULT res = %s(szIP,ref nValue);
                    //LogToolsEx.Info2File(DEVICESDKLOG, "%s:nValue={0} res={1}", nValue, res);
                    return res == HRESULT.S_OK;
                }
'''

CSHARPSTRINGGETDefinition = r'''
[DllImport("HvDevice.dll", EntryPoint = "%s", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.Cdecl)]
static extern HRESULT %s(string szIP, byte[] byteValue, ref int pnValue );
                public static Boolean %sAdv(string szIP,ref string szValue  )
                {
                    int buflen = 1024 * 1024;
                    Byte[] docbuf = new Byte[buflen];
                    HRESULT res = %s(szIP, docbuf, ref buflen);
                    if( res == HRESULT.S_OK)
                    {
                         szValue = System.Text.Encoding.GetEncoding(("GB2312")).GetString(docbuf, 0, buflen).Trim().Trim('\0');
                         return res == HRESULT.S_OK;
                    }
                    //LogToolsEx.Info2File(DEVICESDKLOG, "%s:nValue={0} res={1}", nValue, res);
                    return res == HRESULT.S_OK;
                    
                }
'''


'''
0 funcName,
1 CMDName,
2 SetOrGetType,
3 DateType(NULL,INT,BOOL),
4 Comment
'''

'''
mapӳ���
for item in listSDK:
    if "NULL" == item[3]:
        print "{ \"%s\", XML_CMD_SETTER, XML_CMD_TYPE_NULL_ENTRY(), 0, EMPTY_PARAMNAME32 }," %(item[1])
    elif "BOOL" == item[3] or "INT" == item[3]:
        print "{ \"%s\", DEFAULT_SETTER }," %(item[1])

print "\n\n"
'''


#ͷ�ļ�
for item in listSDK:
    if "NULL" == item[3]:
        print NULLSETHeaderDeclaration %(item[4], item[0])
    elif "BOOL" == item[3]:
        if "SETTER" == item[2]:
            print BOOLSETHeaderDeclaration %(item[4], item[0])
        elif "GETTER" == item[2]:
            print BOOLGETHeaderDeclaration %(item[4], item[0])
    elif "INT" == item[3]:
        if "SETTER" == item[2]:
            print INTSETHeaderDeclaration %(item[4], item[0])
        elif "GETTER" == item[2]:
            print INTGETHeaderDeclaration %(item[4], item[0])
    elif "STRING" == item[3]:
        if "SETTER" == item[2]:
            print STRINGSETHeaderDeclaration %(item[4], item[0])
        elif "GETTER" == item[2]:
            print STRINGGETHeaderDeclaration %(item[4], item[0])
print "\n\n"

#ʵ����
for item in listSDK:
    if "NULL" == item[3]:
        print NULLSETDefinition %(item[0], item[1])
    elif "BOOL" == item[3]:
        if "SETTER" == item[2]:
            print BOOLSETDefinition %(item[0], item[1])
        elif "GETTER" == item[2]:
            print BOOLGETDefinition %(item[0], item[1])
    elif "INT" == item[3]:
        if "SETTER" == item[2]:
            print INTSETDefinition %(item[0], item[1])
        elif "GETTER" == item[2]:
            print INTGETDefinition %(item[0], item[1])
    elif "STRING" == item[3]:
        if "SETTER" == item[2]:
            print STRINGSETDefinition %(item[0], item[1])
        elif "GETTER" == item[2]:
            print STRINGGETDefinition %(item[0], item[1])


'''
0 funcName,
1 CMDName,
2 SetOrGetType,
3 DateType(NULL,INT,BOOL),
4 Comment
'''
#CSharpʵ����
for item in listSDK:  
    if "NULL" == item[3]:
        print CSHARPNULLSETDefinition %(item[0], item[0], item[1],item[0],item[0] )  
    elif "INT" == item[3]:
        if "SETTER" == item[2]:
            print CSHARPINTSETDefinition %(item[0],item[0], item[1],item[0],item[0])
        elif "GETTER" == item[2]:
            print CSHARPINTGETDefinition %(item[0],item[0], item[1],item[0],item[0])
    elif "STRING" == item[3]:
        if "SETTER" == item[2]:
            print CSHARPSTRINGSETDefinition %(item[0],item[0], item[1],item[0],item[0])
        elif "GETTER" == item[2]:
            print CSHARPSTRINGGETDefinition %(item[0],item[0], item[1],item[0],item[0])

tempNULLSetCase =r'''
            case CMD_%sADV:   //%s
                                param = dcCommand.Parameters as object[];
                                pmdevice = param[0] as PMDevice;
                                iResult = pmdevice.%sAdv();
                                dcCommand.IsSuccess = iResult.Success;
                                if (!iResult.Success)
                                    dcCommand.FailMessage = iResult.Message;
                                else
                                    dcCommand.SuccessMessage = iResult.Message;
                                break;'''
tempINTSetCase =r'''
            case CMD_%sADV:   //%s
                                param = dcCommand.Parameters as object[];
                                pmdevice = param[0] as PMDevice;
                                iResult = pmdevice.%sAdv(int.Parse((param[1] as string[])[1]));
                                dcCommand.IsSuccess = iResult.Success;
                                if (!iResult.Success)
                                    dcCommand.FailMessage = iResult.Message;
                                else
                                    dcCommand.SuccessMessage = iResult.Message;
                                break;'''
tempSTRINGSetCase =r'''
            case CMD_%sADV: //%s
                                param = dcCommand.Parameters as object[];
                                pmdevice = param[0] as PMDevice;
                                iResult = pmdevice.%sAdv((param[1] as string[])[1]);
                                dcCommand.IsSuccess = iResult.Success;
                                if (!iResult.Success)
                                    dcCommand.FailMessage = iResult.Message;
                                else
                                    dcCommand.SuccessMessage = iResult.Message;
                                break;'''

tempINTGetCase =r'''
            case CMD_%sADV://%s
                                param = dcCommand.Parameters as object[];
                                pmdevice = param[0] as PMDevice;
                                int %s = -1;
                                iResult = pmdevice.%sAdv( ref %s);
                                dcCommand.IsSuccess = iResult.Success;
                                if (!iResult.Success)
                                    dcCommand.FailMessage = iResult.Message;
                                else
                                    dcCommand.SuccessMessage = iResult.Message;
                                break;'''
tempSTRINGGetCase =r'''
            case CMD_%sADV://%s
                                param = dcCommand.Parameters as object[];
                                pmdevice = param[0] as PMDevice;
                                string str%s = "";
                                iResult = pmdevice.%sAdv( ref str%s);
                                dcCommand.IsSuccess = iResult.Success;
                                if (!iResult.Success)
                                    dcCommand.FailMessage = iResult.Message;
                                else
                                    dcCommand.SuccessMessage = iResult.Message;
                                break;'''
for item in listSDK:
    if "SETTER" == item[2]:
        if "INT" == item[3]:
            print tempINTSetCase %(item[1].upper(),item[4],item[1])
        elif "STRING" == item[3]:
            print tempSTRINGSetCase %(item[1].upper(),item[4],item[1])
        elif "NULL" == item[3]:
            print tempNULLSetCase %(item[1].upper(),item[4],item[1])
    elif "GETTER" == item[2]:
         strParam = item[1].replace("Get", "").replace("Set", "")
         if "INT" == item[3]:
            print tempINTGetCase %(item[1].upper(),item[4],strParam,item[1],strParam)
         elif "STRING" == item[3]:
            print tempSTRINGGetCase %(item[1].upper(),item[4],strParam,item[1], strParam)
             
    


tempString = r'''
public const string CMD_%sADV = "%sAdv";
public const string CMD_%sADV_ED = "%sAdv_ed";
'''
for item in listSDK:
    print tempString %(item[1].upper(), item[1], item[1].upper(), item[1])


tempExeed = r'''            else if (cmd.CommandKey == DevicesManager.CMD_%sADV)
            {
                /*%s���*/
                this.Dispatcher.BeginInvoke((ParameterizedThreadStart)delegate(object parameter)
                {
                    (CurrentAppObj.MainWindow as MainWindow).CloseWaitBox();
                    DeviceCommand Command = parameter as DeviceCommand;
                    CheckActionFinish(Command);
                }, DispatcherPriority.Normal, cmd);
            }'''
for item in listSDK:
    print tempExeed %(item[1].upper(), item[4])

#������  ע��   ������  ע�� 
tempNULLSetClassDefine = '''
    public ResultInfo %sAdv()
        {
            ResultInfo result = new ResultInfo(true, string.Format("��{0}��%s���.", IP));

            if (!ISDKDevice.%sAdv(IP))
            {
                result.Success = false;
                result.Message = string.Format("��{0}��%sʧ��.", IP);
            }

            return result;
        }
'''   
tempINTSetClassDefine = '''
    public ResultInfo %sAdv(int value)
        {
            ResultInfo result = new ResultInfo(true, string.Format("��{0}��%s���.", IP));

            if (!ISDKDevice.%sAdv(IP, value))
            {
                result.Success = false;
                result.Message = string.Format("��{0}��%sʧ��.", IP);
            }

            return result;
        }
'''
tempSTRINGSetClassDefine = '''
    public ResultInfo %sAdv(string value)
        {
            ResultInfo result = new ResultInfo(true, string.Format("��{0}��%s���.", IP));

            if (!ISDKDevice.%sAdv(IP, value))
            {
                result.Success = false;
                result.Message = string.Format("��{0}��%sʧ��.", IP);
            }

            return result;
        }
'''
tempINTGetClassDefine = '''
    public ResultInfo %sAdv(ref int value)
        {
            ResultInfo result = new ResultInfo(true, string.Format("��{0}��%s���.", IP));

            if (!ISDKDevice.%sAdv(IP, ref value))
            {
                result.Success = false;
                result.Message = string.Format("��{0}��%sʧ��.", IP);
            }
            return result;
        }
'''
tempSTRINGGetClassDefine = '''
    public ResultInfo %sAdv(ref string value)
        {
            ResultInfo result = new ResultInfo(true, string.Format("��{0}��%s���.", IP));

            if (!ISDKDevice.%sAdv(IP,ref value))
            {
                result.Success = false;
                result.Message = string.Format("��{0}��%sʧ��.", IP);
            }

            return result;
        }
'''

for item in listSDK:
    if "SETTER" == item[2]:
        if "INT" == item[3]:
            print tempINTSetClassDefine %(item[1],item[4],item[1],item[4])
        elif "STRING" == item[3]:
            print tempSTRINGSetClassDefine %(item[1],item[4],item[1],item[4])
        elif "NULL" == item[3]:
            print tempNULLSetClassDefine %(item[1],item[4],item[1],item[4])
    elif "GETTER" == item[2]:
         if "INT" == item[3]:
            print tempINTGetClassDefine %(item[1],item[4],item[1],item[4])
         elif "STRING" == item[3]:
            print tempSTRINGGetClassDefine %(item[1],item[4],item[1],item[4])
            
tempSend = r'''
            DeviceCommand cmd = new DeviceCommand();
            List<string> keys = null;
            object[] param = new object[2];
            param[0] = CurrentAppObj.CurrentDevice;
            cmd.CommandKey = DevicesManager.CMD_%sADV;
            keys = new List<string>();
            keys.Add(Convert.ToString(#####));
            param[1] = keys.ToArray();
            cmd.Parameters = param;
            cmd.SuccessMessage = "%s���..";
            cmd.FailMessage = "%sʧ��..";
            CurrentAppObj.m_DevicesManager.ExcuteCommand(cmd);
'''
for item in listSDK:
    print tempSend %(item[1].upper(), item[4], item[4])

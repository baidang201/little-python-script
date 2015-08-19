# -*- coding: cp936 -*-
l = []
'''
l.append(["StartFocusAdv", "开始聚焦"])
l.append(["StopFocusAdv", "停止聚焦"])
'''
l.append(["GetLEDSwitchAdv", "获取LED开关"])

'''
l.append(["GetManualShutter", "获取快门"])
l.append(["GetManualGain", "获取增益"])
l.append(["GetManualRGB", "获取RGB"])
l.append(["GetFPGAMode", "获取FPGAMode"])
l.append(["AGCEnable", "设置AGC"])
l.append(["AWBEnable", "设置AWB"])

l.append(["GetDCAperture", "获取DC光圈"])

l.append(["GetAGCEnable", "获取AGC"])
l.append(["GetAWBEnable", "获取AWB"])
'''

t = '''
        [DllImport("HvDevice.dll", EntryPoint = "HVAPI_%s", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.Cdecl)]
        static extern HRESULT HVAPI_%s(IntPtr hHandle, ref int Value);

        public static Boolean %s(IntPtr hHandle, ref int Value)
        {
            HRESULT res = HVAPI_%s(hHandle, ref Value);
            //LogToolsEx.Info2File(DEVICESDKLOG, "%s: hHandle={0} Value={1} res={2} ", hHandle, Value, res);
            return res == HRESULT.S_OK;
        }
'''


t2 = '''
/// <summary>
        /// %s
        /// </summary>
        /// <param name="shutter">%s</param>
        /// <returns>执行结果</returns>
        public ResultInfo %s( ref int value)
        {
            ResultInfo result = new ResultInfo(true, string.Format("【{0}】%s完成.", IP));
            bool newConnected = false;
            if (m_DeviceHandle == IntPtr.Zero)
            {
                if (!Connect().Success)
                {
                    result.Success = false;
                    result.Message = string.Format("【{0}】设备未连接,%s失败.", IP);
                    return result;
                }
                newConnected = true;
            }

            if (!ISDKDevice.%s(m_DeviceHandle, ref value))
            {
                result.Success = false;
                result.Message = string.Format("【{0}】%s失败.", IP);
            }

            if (newConnected) Disconnect();

            return result;
        }
'''

t3 = '''
case CMD_%s: //%s
                                param = dcCommand.Parameters as object[];
                                int value = -1;
                                iResult = (param[0] as SignalwayDevice).%s(ref value);
                                dcCommand.IsSuccess = iResult.Success;
                                if (!iResult.Success)
                                    dcCommand.FailMessage = iResult.Message;
                                else
                                    dcCommand.SuccessMessage = iResult.Message;
                                break;
'''


l2 =[]
l2.append(["CMD_STARTFOCUSADV", ""])
l2.append(["CMD_STOPFOCUSADV", ""])


t4 ='''
            DeviceCommand cmd_%s = new DeviceCommand();
            cmd_%s.CommandKey = DevicesManager.%s;
            cmd_%s.Parameters = m_currentdevice;
            CurrentAppObj.m_DevicesManager.ExcuteCommand(cmd_%s);
'''

for item in l2:
    print t4 %(item[0], item[0], item[0], item[0], item[0])



for item in l:
    print t %(item[0], item[0],item[0],item[0],item[0],)


for item in l:
    print t2 %(item[1], item[1],item[0],item[1],item[1],item[0],item[1],)


'''
for item in l:
    print t3 %(item[0], item[1], item[0],)
   
for item in l2:
    print t4 %(item[0], item[0], item[0], item[0], item[0])
'''

listSrc = [
"HVAPI_CHvDeviceManager",
"HVAPI_~CHvDeviceManager",
"HVAPI_UploadData",
"HVAPI_DownloadData",
"HVAPI_ExecXmlCmd",
"HVAPI_ParseXmlCmdResponse",
"HVAPI_ResetDevice",
"HVAPI_GetResetCount",
"HVAPI_GetResetReport",
"HVAPI_GetDeviceSetting",
"HVAPI_SetDeviceSetting",
"HVAPI_SendControlPanelUpdateFile",
"HVAPI_RestoreDefaultSetting",
"HVAPI_RestoreFactorySetting",
"HVAPI_SetStreamFps",
"HVAPI_SetH264BitRateControl",
"HVAPI_SetH264BitRate",
"HVAPI_SetJpegCompressRate",
"HVAPI_SetOSDEnable",
"HVAPI_SetOSDPlateEnable",
"HVAPI_SetOSDFontSize",
"HVAPI_SetOSDFontRGB",
"HVAPI_SetOSDTimeEnable",
"HVAPI_SetOSDPosition",
"HVAPI_SetOSDFont",
"HVAPI_SetOSDText",
"HVAPI_SetCharactorFontData",
"HVAPI_SetCVBDisplayMode",
"HVAPI_SetManualShutter",
"HVAPI_SetManualGain",
"HVAPI_SetAWBEnable",
"HVAPI_SetAWBMode",
"HVAPI_SetManualRGB",
"HVAPI_SetAGCEnable",
"HVAPI_SetAGCLightBaseLine",
"HVAPI_SetAGCZone",
"HVAPI_SetAGCParam",
"HVAPI_SetLUT",
"HVAPI_SetBrightness",
"HVAPI_GetBrightness",
"HVAPI_SetContrast",
"HVAPI_SetSharpness",
"HVAPI_SetSaturation",
"HVAPI_SetWDREnable",
"HVAPI_SetWDRLevel",
"HVAPI_SetBLCEnable",
"HVAPI_SetBLCLevel",
"HVAPI_SetDREEnable",
"HVAPI_SetDRELevel",
"HVAPI_SetDREMode",
"HVAPI_SetDeNoiseSNFEnable",
"HVAPI_SetDeNoiseTNFEnable",
"HVAPI_SetDeNoiseMode",
"HVAPI_SetDeNoiseLevel",
"HVAPI_SetFilterMode",
"HVAPI_SetDCIRIS",
"HVAPI_SetSensorWDREnable",
"HVAPI_SetOCGate",
"HVAPI_SetColor",
"HVAPI_SetACSync",
"HVAPI_GetCameraState",
"HVAPI_GetCameraBasicInfo",
"HVAPI_GetLUT",
"HVAPI_GetAGCZone",
"HVAPI_StartCameraTest",
"HVAPI_ZoomDCIRIS",
"HVAPI_ShrinkDCIRIS",
"HVAPI_GetContrast",
"HVAPI_GetSaturation",
"HVAPI_GetWDRLevel",
"HVAPI_GetAWBEnable",
"HVAPI_GetAGCEnable",
"HVAPI_GetSyncPower",
"HVAPI_GetManualRGB",
"HVAPI_GetAGCParam",
"HVAPI_GetWDREnable",
"HVAPI_GetBLCEnable",
"HVAPI_GetBLCLevel",
"HVAPI_GetDREEnable",
"HVAPI_GetDREMode",
"HVAPI_GetDRELevel",
"HVAPI_GetDeNoiseEnable",
"HVAPI_GetSensorWDREnable",
"HVAPI_GetManualShutter",
"HVAPI_GetManualGain",
"HVAPI_SetJpegOutType",
"HVAPI_GetJpegOutType",
"HVAPI_SetCoilEnable",
"HVAPI_GetCoilEnable",
"HVAPI_GetAWBMode",
"HVAPI_GetAWBWorkMode",
"HVAPI_SetAWBWorkMode",
"HVAPI_GetAGCLightBaseLine",
"HVAPI_SetCtrlCplEnable",
"HVAPI_GetDCAperture",
"HVAPI_SetAEScene",
"HVAPI_GetAEScene",
"HVAPI_GetVideoState",
"HVAPI_SetDebugJpegStatus",
"HVAPI_GetDebugJpegStatus",
"HVAPI_SetAutoJpegCompressEnable",
"HVAPI_SetTraceRank",
"HVAPI_GetTraceRank",
"HVAPI_GetAutoJpegCompressEnable",
"HVAPI_SetAutoJpegCompressParam",
"HVAPI_GetAutoJpegCompressParam",
"HVAPI_SetVedioRequestControl",
"HVAPI_SetMJPEGRect",
"HVAPI_SetH264SecondBitRate",
"HVAPI_GetH264SecondBitRate",
"HVAPI_GetAutoControlCameraEnable",
"HVAPI_SetAutoControlCameraEnable",
"HVAPI_SetIPInfo",
"HVAPI_SetFTPServerIP",
"HVAPI_SetFTPPort",
"HVAPI_SetFTPUserInfo",
"HVAPI_SetFTPUpLoadPath",
"HVAPI_SetRTSPMulticastEnable",
"HVAPI_SetHttpPort",
"HVAPI_SetHttpsPort",
"HVAPI_SetSMTPAuthenticationEnable",
"HVAPI_SetSMTPUserInfo",
"HVAPI_SetSMTPSender",
"HVAPI_SetSMTPServerIP",
"HVAPI_SetSMTPPort",
"HVAPI_SetSMTPEmail",
"HVAPI_SetTime",
"HVAPI_SetTimeZone",
"HVAPI_SetNTPEnable",
"HVAPI_SetNTPServerIP",
"HVAPI_SetNTPServerUpdateInterval",
"HVAPI_GetTime",
"HVAPI_GetTimeZone",
"HVAPI_GetNTPEnable",
"HVAPI_Set2DDeNoiseEnable",
"HVAPI_Set2DDeNoiseStrength",
"HVAPI_SetGammaEnable",
"HVAPI_SetGammaStrength",
"HVAPI_SetGrayImageEnable",
"HVAPI_SetSharpnessEnable",
"HVAPI_GetSharpnessEnable",
"HVAPI_GetSharpness",
"HVAPI_GetEnableGrayImage",
"HVAPI_GetDeNoiseMode",
"HVAPI_GetDeNoiseLevel",
"HVAPI_SetImageEnhancementEnable",
"HVAPI_GetImageEnhancementEnable",
"HVAPI_SetEdgeEnhance",
"HVAPI_SetColorGradation",
"HVAPI_SetDeNoiseSwitch",
"HVAPI_GetDeviceBasicInfo",
"HVAPI_GetRunningMode",
"HVAPI_GetDeviceState",
"HVAPI_GetLog",
"HVAPI_GetCustomizedDevName",
"HVAPI_SetCustomizedDevName",
"HVAPI_GetBlackBoxMessage",
"HVAPI_GetRunningStatus",
"HVAPI_GetCameraWorkState",
"HVAPI_Login",
"HVAPI_AddUser",
"HVAPI_DeleteUser",
"HVAPI_ModifyUser",
"HVAPI_GetUsersList",
"HVAPI_StartCOMCheck",
"HVAPI_ReadFPGA",
"HVAPI_WriteFPGA",
"HVAPI_SetTGIO",
"HVAPI_GetTGIO",
"HVAPI_SetF1IO",
"HVAPI_GetF1IO",
"HVAPI_SetEXPIO",
"HVAPI_GetEXPIO",
"HVAPI_SetALMIO",
"HVAPI_GetALMIO",
"HVAPI_SetExpPluseWidth",
"HVAPI_SetEnRedLightEnable",
"HVAPI_GetEnRedLightEnable",
"HVAPI_SetRedLightRect",
"HVAPI_SetEnRedLightThreshold",
"HVAPI_TriggerImage",
"HVAPI_TriggerSignal",
"HVAPI_TriggerAlarmSignal",
"HVAPI_SoftTriggerCapture",
"HVAPI_SetManualCaptureRGB",
"HVAPI_SetManualCaptureShutter",
"HVAPI_SetManualCaptureGain",
"HVAPI_SetManualCaptureSharpen",
"HVAPI_Capture",
"HVAPI_SendCaptureCmd",
"HVAPI_ImportNameList",
"HVAPI_GetNameList",
"HVAPI_GetNameListXml",
"HVAPI_SetTransparentSerialData",
"HVAPI_SetMJPEGOverlay",
"HVAPI_SetH264VbrSensitivity",
"HVAPI_SetH264VbrDuration",
"HVAPI_SetH264SecondVbrSensitivity",
"HVAPI_SetH264SecondVbrDuration",
"HVAPI_SetH264SecondRateControl",
"HVAPI_SetH264SecondIFrameInterval",
"HVAPI_SetH264Resolution",
"HVAPI_SetH264IFrameInterval",
"HVAPI_GetH264SecondIFrameInterval",
"HVAPI_GetH264Resolution",
"HVAPI_GetH264IFrameInterval",
"HVAPI_SetFaceDataAdv",
"HVAPI_SetDSPParam",
"HVAPI_SetAlgorithmParameterData",
"HVAPI_SetAlgorithmModelData",
"HVAPI_GetPCSFlow",
"HVAPI_GetOSDInfo",
"HVAPI_GetHDDStatus",
"HVAPI_GetHddCheckReport",]

listMy = [
"HVAPI_SetIPByMacAddr",
"HVAPI_SetIPInfo",
"HVAPI_GetDeviceTypeEx",
"HVAPI_OpenEx",
"HVAPI_CloseEx",
"HVAPI_GetConnStatusEx",
"HVAPI_GetReConnectTimesEx",
"HVAPI_StartRecvH264Video",
"HVAPI_StopRecvH264Video",
"HVAPI_StartRecvMJPEG",
"HVAPI_StopRecvMJPEG",
"HVAPI_StartRecvResult",
"HVAPI_StopRecvResult",
"HVAPI_CALLBACK_H264_EX",
"HVAPI_CALLBACK_JPEG_EX",
"HVAPI_CALLBACK_RESULT",
"HVAPI_SearchDeviceEx",
"HVAPI_GetDevBasicInfo",
"HVAPI_GetDevState",
"HVAPI_GetParamEx",
"HVAPI_SetParamEx",
"HVAPI_SetNTPServerIP",
"HVAPI_SetNTPEnable",
"HVAPI_SetTime",
"HVAPI_SetTimeZone",
"HVAPI_ResetDevice",
"HVAPI_RestoreDefaultParam",
"HVAPI_RestoreFactoryParam",
"HVAPI_InportNameList",
"HVAPI_GetNameList",
"HVAPI_GetTimeZone",
"HVAPI_GetCameraBasicInfo",
"HVAPI_GetCameraState",
"HVAPI_SetAGCLightBaseLine",
"HVAPI_SetAGCParam",
"HVAPI_GetRunStatusString",
"HVAPI_SetAEScene",
"HVAPI_SetZoom",
"HVAPI_GetZoom",
"HVAPI_SetAssistantFocus",
"HVAPI_TuneFocus",
"HVAPI_SetH264BitRate",
"HVAPI_GetVideoState",
"HVAPI_GetOSDInfo",
"HVAPI_SetJpegCompressRate",
"HVAPI_SetDebugJpegStatus",
"HVAPI_SetOSDEnable",
"HVAPI_SetOSDTimeEnable",
"HVAPI_SetOSDText",
"HVAPI_SetOSDFont",
"HVAPI_SetOSDPos"
]

listNotShiXian = [
    "HVAPI_SetAutoControlCammeraEnable",
"HVAPI_GetAutoControlCammeraEnable",
"HVAPI_SetCallBackListen",
"HVAPI_OpenListenCMDSever",
"HVAPI_CloseListenCMDSever",
"HVAPI_OpenListenClientEx",
"HVAPI_CloseListenClientEx",
"HVAPI_AntiTamper_Embed",
"HVAPI_SetAEMode",
"HVAPI_GetAEMode",
"HVAPI_CallFigureScan",
"HVAPI_CallPreset",
"HVAPI_ClearHScan",
"HVAPI_ClearPreset",
"HVAPI_SetAF",
"HVAPI_GetAF",
"HVAPI_GetFocusing",
"HVAPI_GetFreezeFlag",
"HVAPI_GetHScanParam",
"HVAPI_GetIRIS",
"HVAPI_GetLEDMode",
"HVAPI_GetLEDPower",
"HVAPI_GetManualAWBMode",
"HVAPI_GetPreset",
"HVAPI_GetPresetNameList",
"HVAPI_GetZoom",
"HVAPI_SetAssistantFocus",
"HVAPI_SetFocusing",
"HVAPI_SetFreezeFlag",
"HVAPI_SetHScanLeftPos",
"HVAPI_SetHScanParam",
"HVAPI_SetHScanRightPos",
"HVAPI_SetIRIS",
"HVAPI_SetLEDMode",
"HVAPI_SetLEDPower",
"HVAPI_SetManualAWBMode",
"HVAPI_SetPreset",
"HVAPI_SetZoom",
"HVAPI_StartFigureScanRecord",
"HVAPI_StartHScan",
"HVAPI_StartWiper",
"HVAPI_StopFigureScanRecord",
"HVAPI_StopHScan",
"HVAPI_CallCruise",
"HVAPI_ClearCruise",
"HVAPI_ClearFScan",
"HVAPI_ClearMask",
"HVAPI_GetCruise",
"HVAPI_GetCurrentTask",
"HVAPI_GetFScanNameList",
"HVAPI_GetMask",
"HVAPI_GetMaxPanSpeed",
"HVAPI_GetMaxTiltSpeed",
"HVAPI_GetPanCoordinate",
"HVAPI_GetPanSpeed",
"HVAPI_GetFScanName",
"HVAPI_GetSpeedDomeParam",
"HVAPI_GetTiltCoordinate",
"HVAPI_GetTiltSpeed",
"HVAPI_GetTimingParam",
"HVAPI_GetWatch",
"HVAPI_MoveBlockToCenter",
"HVAPI_MovePointToCenter",
"HVAPI_ResetDevicePosition",
"HVAPI_SetCruise",
"HVAPI_SetDefog",
"HVAPI_SetFScanName",
"HVAPI_SetMask",
"HVAPI_SetMaxPanSpeed",
"HVAPI_SetMaxTiltSpeed",
"HVAPI_SetPanCoordinate",
"HVAPI_SetPanSpeed",
"HVAPI_SetSpeedDomeParam",
"HVAPI_SetTiltCoordinate",
"HVAPI_SetTiltSpeed",
"HVAPI_SetTimingParam",
"HVAPI_SetWatch",
"HVAPI_StartInfinityPan",
"HVAPI_StartPan",
"HVAPI_StartPanAndTilt",
"HVAPI_StartTilt",
"HVAPI_StartVturnOver",
"HVAPI_StartWatchKeeping",
"HVAPI_StartZoom",
"HVAPI_StopCruise",
"HVAPI_StopFigureScan",
"HVAPI_StopInfinityPan",
"HVAPI_StopPan",
"HVAPI_StopPanAndTilt",
"HVAPI_StopTilt",
"HVAPI_StopVturnOver",
"HVAPI_StopZoom",
"HVAPI_TuneFocus",
"HVAPI_TuneIris",
"HVAPI_GetSleepEnable",
"HVAPI_GetSleepIdleTime",
"HVAPI_SetSleepEnable",
"HVAPI_SetSleepIdleTime",
"HVAPI_SetIdleTimeToSleep",
"HVAPI_GetIdleTimeToSleep",
"HVAPI_StartSleepCountDown",
    ]

for item in listMy:
    #print item
    if item not in listSrc:
        print item, "           not find"
    if item in listNotShiXian:
        print item, "           find but return -1"

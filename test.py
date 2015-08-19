temp =		'''_GET_STRING_VALUE(_GET_RETMSG(), "%s", 			szTmp, 		sizeof(szTmp));	\n		%s = atoi(szTmp);'''

listParam = [
["pCameraBasicInfo->nContrast","Contrast"  ],
["pCameraBasicInfo->nSharpness","Sharpness" ],
["pCameraBasicInfo->nSaturation","Saturation" ],
["pCameraBasicInfo->fWDREnable","WDREnable" ],
["pCameraBasicInfo->nWDRLevel","WDRLevel" ],
["pCameraBasicInfo->nDeNoiseMode","DeNoiseMode" ],
["pCameraBasicInfo->nDeNoiseLevel","DeNoiseLevel" ],
["pCameraBasicInfo->nManualShutter", "ManualShutter" ],
["pCameraBasicInfo->nManualGain", "ManualGain" ],
["pCameraBasicInfo->nManualGainR", "ManualGainR" ],
["pCameraBasicInfo->nManualGainG", "ManualGainG" ],
["pCameraBasicInfo->nManualGainB", "ManualGainB" ],
["pCameraBasicInfo->fAWBEnable","AWBEnable"  ],
["pCameraBasicInfo->fAGCEnable","AGCEnable" ],
["pCameraBasicInfo->nAGCLightBaseLine","AGCLightBaseLine" ],
["pCameraBasicInfo->nAGCShutterMin","AGCShutterMin" ],
["pCameraBasicInfo->nAGCShutterMax","AGCShutterMax" ],
["pCameraBasicInfo->nAGCGainMin","AGCGainMin" ],
["pCameraBasicInfo->nAGCGainMax","AGCGainMax" ],
["pCameraBasicInfo->nFilterMode","FilterMode"],
["pCameraBasicInfo->fDCEnable","DCEnable" ],
["pCameraBasicInfo->fGammaEnable","GammaEnable" ],
["pCameraBasicInfo->nGammaStrength","GammaValue" ],
["pCameraBasicInfo->fSharpnessEnable","SharpnessEnable" ],
["pCameraBasicInfo->nACSyncMode","ACSyncMode" ],
["pCameraBasicInfo->nACSyncDelay","ACSyncDelay" ],
["pCameraBasicInfo->fGrayImageEnable","GrayImageEnable" ],
["pCameraBasicInfo->fImageEnhancementEnable","ImageEnhancementEnable" ],
["pCameraBasicInfo->nEnRedLightThreshold","EnRedLightThreshold" ],
["pCameraBasicInfo->fDeNoiseSNFEnable","DeNoiseSNFEnable"],
["pCameraBasicInfo->fDeNoiseTNFEnable","DeNoiseTNFEnable"],
["pCameraBasicInfo->nEdgeEnhance","EdgeEnhance"],
]

for item in listParam:
			print temp %(item[1], item[0])

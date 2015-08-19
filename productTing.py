# -*- coding: cp936 -*-


l = []
'''
l.append(["Shutter", "快门", "5", "ParameterKey.INT_TYEP", "30000", "0", "9900", "2000"])
l.append(["Gain", "增益", "5", "ParameterKey.INT_TYEP", "480", "0", "150", "70"])
l.append(["GainR", "R增益", "5", "ParameterKey.INT_TYEP", "255", "36", "69", "36"])
l.append(["GainG", "G增益", "5", "ParameterKey.INT_TYEP", "255", "36", "36", "36"])
l.append(["GainB", "B增益", "5", "ParameterKey.INT_TYEP", "255", "36", "69", "36"])
l.append(["EnableDCAperture", "使能DC光圈", "5", "ParameterKey.INT_TYEP", "1", "0", "0", "0"])
l.append(["AGCEnable", "AGC使能", "5", "ParameterKey.INT_TYEP", "1", "0", "0", "1"])
l.append(["AWBEnable", "AWB使能", "5", "ParameterKey.INT_TYEP", "1", "0", "0", "1"])
'''
l.append(["Zoom", "聚焦", "5", "ParameterKey.INT_TYEP", "540", "0", "0", "1"])
l.append(["Focus", "焦距", "5", "ParameterKey.INT_TYEP", "754", "0", "0", "1"])
l.append(["Iris", "光圈", "5", "ParameterKey.INT_TYEP", "24", "0", "0", "1"])


d = '''
        protected ParameterKey m_%s = new ParameterKey();
        /// <summary>
        /// %s
        /// </summary>
        public ParameterKey %s
        {
            get { return this.m_%s;}
            set 
            {
                this.m_%s = value;
                NotifyChanged("%s");
            }
        }
'''

'''
            m_Shutter.Name = "Shutter";
            m_Shutter.CHName = "手动快门";
            m_Shutter.Rank = 5;
            m_Shutter.Type = ParameterKey.INT_TYEP;
            m_Shutter.Max = "30000";
            m_Shutter.Min = "0";
            m_Shutter.Value = "0";
            m_Shutter.Default = "0";
'''

init = '''
            m_%s.Name = "%s";
            m_%s.CHName = "%s";
            m_%s.Rank = %s;
            m_%s.Type = %s;
            m_%s.Max = "%s";
            m_%s.Min = "%s";
            m_%s.Value = "%s";
            m_%s.Default = "%s";
'''

'''
for item in l:
    print d %(item[0], item[1], item[0], item[0], item[0], item[0])
   '''  

for item in l:
    print init %(item[0], item[0], item[0], item[1], item[0], item[2], item[0], item[3],
                 item[0], item[4], item[0], item[5], item[0], item[6], item[0], item[7], )
       

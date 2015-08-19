import socket


strBo = '<?xml version="1.0" encoding="GB2312" standalone="yes" ?>\n<HvCmdRespond Ver="3.0">\n    <CmdName IP="172.19.253.253" Mask="255.255.0.0" Gateway="172.19.99.99" MAC="0c:f4:05:12:70:ff" SN="PMX-1UT-LS13014158" Mode="\xd5\xfd\xb3\xa3\xc4\xa3\xca\xbd" WorkMode="\xc9\xfa\xb2\xfa\xc4\xa3\xca\xbd" DevVersion="3.1.0.1280" DevType="PM" Remark="Remark" PMTag="FA" PMMainSN="NULL" RetCode="0" RetMsg="OK">Probe</CmdName>\n</HvCmdRespond>\n'

tempStrBo = '<?xml version="1.0" encoding="GB2312" standalone="yes" ?>\n<HvCmdRespond Ver="3.0">\n    <CmdName IP="172.18.253.%d" Mask="255.255.0.0" Gateway="172.19.99.99" MAC="0c:f4:05:12:ff:f%d" SN="PMB-1UT-LS1301415%d" Mode="\xd5\xfd\xb3\xa3\xc4\xa3\xca\xbd" WorkMode="\xc9\xfa\xb2\xfa\xc4\xa3\xca\xbd" DevVersion="3.1.0.1280" DevType="PM" Remark="Remark" PMTag="FA" PMMainSN="NULL" RetCode="0" RetMsg="OK">Probe</CmdName>\n</HvCmdRespond>\n'

host=''  
port=6666


def sendBroadcastBack(addr):
    #print strBo
    addrNew = ('<broadcast>', addr[1])
    sNew=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sNew.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
    for i in range(1,4):
        sNew.sendto(tempStrBo %(i,i,i),addr)
    
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)  
s.bind((host,port))  
while 1:  
    try:  
        data,addr=s.recvfrom(1024)  
        print "got data from",addr  
        #s.sendto("broadcasting",addr)  
        print  data.encode('hex')            
        if b"\x01\x01\x00\x00"== data:
            print "just do it", addr            
            sendBroadcastBack(addr)
            
    except KeyboardInterrupt:  
        raise  



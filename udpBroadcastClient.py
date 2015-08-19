#!/usr/bin/env python
import socket,sys
import time
addr=('<broadcast>',6666)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

while 1:
    s.sendto(b"\x01\x01\x00\x00",addr)
    data=s.recvfrom(1024)
    if not data:
        continue        
    print data
    time.sleep(3)

'''
('\x01\x01\x00\x00\x90\xbe\xe9\x17\xd0\xb6\x1d\xe6\x12\xac\x00\x00\xff\xff\x01\x01\x12\xacHVCAM-D01-LS11020294\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', ('172.18.230.29', 6666))
('<?xml version="1.0" encoding="GB2312" standalone="yes" ?>\n<HvCmdRespond Ver="3.0">\n    <CmdName IP="172.19.17.158" Mask="255.255.0.0" Gateway="172.19.1.1" MAC="0c:f4:05:12:70:3e" SN="VECAM-D01-LS13014158" Mode="\xd5\xfd\xb3\xa3\xc4\xa3\xca\xbd" WorkMode="\xbf\xa8\xbf\xda" DevVersion="3.1.0.1280" DevType="PCC200" Remark="Remark" RetCode="0" RetMsg="OK">Probe</CmdName>\n</HvCmdRespond>\n', ('172.19.17.158', 6666))
'''

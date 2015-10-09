# -*- coding: cp936 -*-
import time
import struct
from socket import *

SENDERIP = '172.18.11.123'#����ip
SENDERPORT = 1501#���ؽӿ�
MYPORT = 1234#�������ݵ��ö˿�
MYGROUP = '224.1.1.1'#�鲥��
MYTTL = 255 # �������ݵ�TTLֵ

def sender():
    s = socket(AF_INET, SOCK_DGRAM,IPPROTO_UDP)
    s.bind((SENDERIP,SENDERPORT))
    # Set Time-to-live (optional)
    ttl_bin = struct.pack('@i', MYTTL)
    s.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, ttl_bin)
    status = s.setsockopt(IPPROTO_IP,
        IP_ADD_MEMBERSHIP,
        inet_aton(MYGROUP) + inet_aton(SENDERIP))#���뵽�鲥��
    while True:
        data = 'cisco'
        s.sendto(data + '\0', (MYGROUP, MYPORT))
        print "send data ok !"
        time.sleep(10)

if __name__ == "__main__":
    sender()

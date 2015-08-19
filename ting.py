listSrc=[
"A successful WSAStartup call must occur before using this function. ",
"The network subsystem has failed. ",
"The requested address is a broadcast address, but the appropriate flag was not set. Call setsockopt with the SO_BROADCAST parameter to allow the use of the broadcast address. ",
"An unknown flag was specified, or MSG_OOB was specified for a socket with SO_OOBINLINE enabled. ",
"A blocking Windows Sockets 1.1 call was canceled through WSACancelBlockingCall. ",
"A blocking Windows Sockets 1.1 call is in progress, or the service provider is still processing a callback function. ",
"The buf or to parameters are not part of the user address space, or the tolen parameter is too small. ",
"The connection has been broken due to keep-alive activity detecting a failure while the operation was in progress. ",
"No buffer space is available. ",
"The socket is not connected (connection-oriented sockets only). ",
"The descriptor is not a socket. ",
"MSG_OOB was specified, but the socket is not stream-style such as type SOCK_STREAM, OOB data is not supported in the communication domain associated with this socket, or the socket is unidirectional and supports only receive operations. ",
"The socket has been shut down; it is not possible to sendto on a socket after shutdown has been invoked with how set to SD_SEND or SD_BOTH. ",
"The socket is marked as nonblocking and the requested operation would block. ",
"The socket is message oriented, and the message is larger than the maximum supported by the underlying transport. ",
"The remote host cannot be reached from this host at this time. ",
"The virtual circuit was terminated due to a time-out or other failure. The application should close the socket as it is no longer usable. ",
"The virtual circuit was reset by the remote side executing a hard or abortive close. For UPD sockets, the remote host was unable to deliver a previously sent UDP datagram and responded with a \"Port Unreachable\" ICMP packet. The application should close the socket as it is no longer usable. ",
"The remote address is not a valid address, for example, ADDR_ANY. ",
"Addresses in the specified family cannot be used with this socket. ",
"A destination address is required. ",
"The network cannot be reached from this host at this time. ",
"The connection has been dropped, because of a network failure or because the system on the other end went down without notice. ",
"Unknown socket error. ",
    ]

f = open(r"E:\HvDeviceNewLogForWinNaviNew.txt")
for item in f:
    for itemSrc in listSrc:
        if itemSrc in item:
            print item

f.close()

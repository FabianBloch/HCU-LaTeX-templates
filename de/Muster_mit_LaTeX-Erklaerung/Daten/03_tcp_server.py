# tcp: Transmission Control Protocol (Server)

import socket

# 0.0.0.0:   listen on all available network adapters in the computer
# 127.0.0.1: local loopback, it's only available for programs on the same computer
# <ip-addr>: listen only on the network adapter with the given IP address
TCP_IP = '0.0.0.0'

# local port, possible values between 0 and 65535
# ports between 0 and 1024 are typically reserved for system services
TCP_PORT = 8128

# The buffer size is usually 1024 bytes.
BUFFER_SIZE = 1024

conn = None
try:
    # create a TCP socket
    # SOCK_STREAM: Stream Socket (TCP) use the Internet Protocol (IP) for routing
    # AF_INET: Address family for IPv4
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the endpoint (IP address and port)
    # Note: The parameter is a tuple.
    s.bind( ( TCP_IP, TCP_PORT ) )
    
    print(f'bind to {TCP_IP}:{TCP_PORT}')
    print('Send EXIT to terminate the server!')
    
    while True:
        # Listen for connections made to the socket.
        # One connection allowed at the same time.
        # The maximum value of connections is system-dependent (usually 5).
        # The program is suspended while waiting for an incoming connection.
        # This is a synchronous TCP application.
        s.listen(1)
        
        # Accept the incoming connection.
        # The return value is a pair (conn, address) where conn is a new socket object
        # usable to send an receive3 data on the connection. And address is the address
        # bound to the socket on the other end of the connection.
        conn, addr = s.accept()
        
        print(f'Connection address: {addr}')
        
        # Receive data from the socket.
        # The return value  is a byte stream representing the data received. The maximum
        # amount of data to be received at once is specified by BUFFER_SIZE.
        data = conn.recv(BUFFER_SIZE).decode()
        
        # Print out the received data.
        print(data)
        
        if data == 'EXIT':
            break
        
        # Send data to the socket. The socket must be connected to a remote socket.
        # Echo the incoming data back to the client.
        conn.send(data.encode())
        
        # Close the socket.
        conn.close()
        
except socket.error as e:
    print(f'Error: {e}')

finally:
    if conn:
        conn.close()

        
        
        
        
        
        
        
    

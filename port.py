import socket

def port_scan(host, start_port, end_port):
    # Loop through the specified range of ports
    for port in range(start_port, end_port+1):
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        # Attempt to connect to the specified host and port
        result = sock.connect_ex((host, port))
        # If the connection was successful, print a message
        if result == 0:
            print(f"Port {port} is open")
        # Close the socket
        sock.close()

# Call the function with the desired parameters
port_scan("example.com", 1, 1000)

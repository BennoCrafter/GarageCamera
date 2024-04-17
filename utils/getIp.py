import socket


def get_ip_address():
    # Get the hostname of the machine
    hostname = socket.gethostname()
    # Get the IP address corresponding to the hostname
    ip_address = socket.gethostbyname(hostname)
    return ip_address


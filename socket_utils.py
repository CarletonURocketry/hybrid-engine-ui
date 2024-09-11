"""
socket_utils.py
This file contains utility functions for creating TCP sockets
"""
import socket

def create_tcp_socket_connection(ip_addr: str, port: str) -> socket.socket:
    """
    Creates a TCP socket and established a connection with the given IPv4 address
    and port
    """
    try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.connect((ip_addr, port))
    except socket.gaierror as e:
        print(f"Address-related error: {e}")
        raise Exception(f"Address-related error: {e}")
    except socket.herror as e:
        print(f"Host-related error: {e}")
        raise Exception(f"Host-related error: {e}")
    except TimeoutError:
        print("Socket operation timed out")
        raise Exception("Socket operation timed out")
    except OSError as e:
        print(f"OS error: {e}")
        raise Exception(f"OS error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise Exception(f"An unexpected error occurred: {e}")
    return tcp_socket

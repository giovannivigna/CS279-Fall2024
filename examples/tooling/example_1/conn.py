from pwn import *

host = 'localhost'
port = 12345


def main():
    conn = remote(host, port)

    filename = "flag.txt"
    conn.sendline(filename)

    response = conn.recvall().decode()

    print("Received from server:")
    print(response)

    conn.close()


if __name__ == "__main__":
    main()

import socket   
import threading


def receive_messages():
    while True:
        try:
            mss = client.recv(1024).decode('utf-8')

            if mss == "username":
                client.send(username.encode("utf-8"))
            else:
                print(mss)
        except:
            print("No se pudo")
            client.close()
            break


def write_messages():
    while True:
        try:
            mss = f"{username}: {input('')}"
            client.send(mss.encode('utf-8'))
        except:
            break


if __name__ == '__main__':
    username = input("Ingresa tu usuario: ")

    host = '192.168.3.95'
    port = 55555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))  # todo try exit

    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    write_thread = threading.Thread(target=write_messages)
    write_thread.start()

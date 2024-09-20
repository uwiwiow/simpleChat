import socket
import threading


def broadcast(mss, cc):
    for client in clients:
        if client != cc:
            client.send(mss)  # todo try


def handle_messages(client):
    while True:
        try:
            mss = client.recv(1024)
            broadcast(mss, client)
        except:
            index = clients.index(client)
            username = usernames[index]
            broadcast(f"ChatBot: {username} se desconecto".encode('utf-8'), client)
            clients.remove(client)
            usernames.remove(username)
            client.close()
            break


def receive_connections():
    while True:
        client, address = server.accept()  # todo try

        client.send("username".encode("utf-8"))
        username = client.recv(1024).decode('utf-8')

        clients.append(client)
        usernames.append(username)

        print(f"{username} conectado desde {str(address)}")

        mss = f"ChatBot: {username} si se pudo unir".encode("utf-8")
        broadcast(mss, client)
        client.send("Conectado :)".encode("utf-8"))

        thread = threading.Thread(target=handle_messages, args=(client,))
        thread.start()


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 55555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((host, port))  # todo try exit
    server.listen()
    print(f"Si sirve... {host}:{port}")

    clients = []
    usernames = []

    receive_connections()

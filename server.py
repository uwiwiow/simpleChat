import socket
import threading


class Server:
    def __init__(self):
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = 55555

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server.bind((self.host, self.port))
        self.server.listen()
        print(f"Si sirve... {self.host}:{self.port}")

        self.clients = []
        self.usernames = []


    def broadcast(self, mss, cc):
        for client in self.clients:
            if client != cc:
                client.send(mss)


    def handle_messages(self, client):
        while True:
            try:
                mss = client.recv(1024)
                self.broadcast(mss, client)
            except:
                index = self.clients.index(client)
                username = self.usernames[index]
                self.broadcast(f"ChatBot: {username} se desconecto\n".encode('utf-8'), client)
                self.clients.remove(client)
                self.usernames.remove(username)
                client.close()
                break


    def receive_connections(self):
        while True:
            client, address = self.server.accept()

            client.send("username".encode("utf-8"))
            username = client.recv(1024).decode('utf-8')

            self.clients.append(client)
            self.usernames.append(username)

            print(f"{username} conectado desde {str(address)}")

            mss = f"ChatBot: {username} si se pudo unir\n".encode("utf-8")
            self.broadcast(mss, client)
            client.send("Conectado :)\n".encode("utf-8"))

            thread = threading.Thread(target=self.handle_messages, args=(client,))
            thread.start()


if __name__ == '__main__':
    server = Server()
    server.receive_connections()

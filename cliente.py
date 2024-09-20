import socket   
import threading
from tkinter import scrolledtext
from ttkbootstrap import Entry
from ttkbootstrap.constants import *



class Cliente:
    def __init__(self, username: str, text_area: scrolledtext.ScrolledText):
        self.username = username
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = 55555

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client.connect((self.host, self.port))
        except Exception as e:
            print(f"Error: {str(e)}")
            if isinstance(e, socket.error):
                print(f"Error code: {e.errno}")

        self.running = True
        receive_thread = threading.Thread(target=self.receive_messages, args=(text_area,))
        receive_thread.start()

    def receive_messages(self, text_area: scrolledtext.ScrolledText):
        while self.running:
            try:
                mss = self.client.recv(1024).decode('utf-8')
                if mss == "username":
                    self.client.send(self.username.encode("utf-8"))
                else:
                    if mss.strip():
                        text_area.config(state='normal')
                        text_area.insert(INSERT, str(mss))
                        text_area.config(state='disabled')
                        text_area.see(END)

            except Exception as e:
                print(f"Error: {str(e)}")
                if isinstance(e, socket.error):
                    print(f"Error code: {e.errno}")

    def write_messages(self, entry_message: Entry, text_area: scrolledtext.ScrolledText):
        message = entry_message.get()
        if message.strip():
            text_area.config(state='normal')
            text_area.insert(INSERT, f"You: {message}\n")
            text_area.config(state='disabled')
            entry_message.delete(0, END)

        mss = f"{self.username}: {message}\n"
        self.client.send(mss.encode('utf-8'))

    def close_connection(self):
        self.running = False
        self.client.close()


if __name__ == '__main__':
    cliente = Cliente()
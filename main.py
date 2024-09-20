from socket import gethostname
import ttkbootstrap as ttk
from ttkbootstrap import Querybox
from ttkbootstrap.constants import *
from tkinter import scrolledtext
from cliente import Cliente

class SimpleChat:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple chat")

        self.text_area = scrolledtext.ScrolledText(root, wrap=WORD, width=50, height=10)
        self.text_area.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        self.text_area.insert(END, "This is the start of the chat\n")
        self.text_area.config(state='disabled')  # Make the text area read-only
        

        # Entry box to type messages
        self.entry_message = ttk.Entry(root, width=40)
        self.entry_message.grid(row=1, column=0, padx=10, pady=10)
        self.entry_message.bind('<Return>', self.send_message_event)

        # Send button
        self.send_button = ttk.Button(root, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        username = Querybox.get_string("Enter username", "Username", None, root)

        if username.strip():
            self.cliente = Cliente(username, self.text_area)
        else:
            self.cliente = Cliente(gethostname(), self.text_area)

        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def send_message_event(self, event):
        self.send_message()

    def send_message(self):
        self.cliente.write_messages(self.entry_message, self.text_area)
        self.text_area.see(END)

    def on_close(self):
        self.cliente.close_connection()  # Llama a un método para cerrar la conexión
        self.root.destroy()  # Cierra la ventana

if __name__ == '__main__':
    root = ttk.Window(themename="vapor")
    app = SimpleChat(root)
    root.mainloop()

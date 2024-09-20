import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import scrolledtext
from cliente import Cliente

class SimpleChat:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple chat")
        self.root.geometry('1600x900')

        # Text area to display messages
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

        self.cliente = Cliente("gael", self.text_area)  # dar nombre de usuario como input

    def send_message_event(self, event):
        self.send_message()

    def send_message(self):
        self.cliente.write_messages(self.entry_message, self.text_area)

if __name__ == '__main__':
    root = ttk.Window(themename="vapor")
    app = SimpleChat(root)
    root.mainloop()

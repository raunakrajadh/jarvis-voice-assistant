import tkinter as tk
from tkinter import scrolledtext
from dotenv import dotenv_values
import threading

from jarvis import jarvis

env_vars = dotenv_values(".env")
Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title(f"{Assistantname} AI")
        self.root.iconphoto(False, tk.PhotoImage(file="assets/jarvis.png"))
        self.root.configure(bg="#36393f")
        self.root.state('zoomed')

        # Top navbar
        self.navbar = tk.Frame(self.root, bg="#202225")
        self.navbar.pack(fill=tk.X)

        self.navbar_label = tk.Label(
            self.navbar, 
            text="JARVIS AI", 
            bg="#202225", 
            fg="#ffffff", 
            font=("Helvetica", 14, "bold")
        )
        self.navbar_label.pack(pady=5)

        # Frame for chat display
        self.chat_frame = tk.Frame(self.root, bg="#2f3136")
        self.chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # ScrolledText widget to display chat messages
        self.chat_display = scrolledtext.ScrolledText(
            self.chat_frame,
            wrap=tk.WORD,
            bg="#2f3136",
            fg="#dcddde",
            font=("Helvetica", 12),
            insertbackground="#ffffff",  # Cursor color
            border=0,
            state=tk.DISABLED,  # Read-only
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)

        # Entry box for user input
        self.input_frame = tk.Frame(self.root, bg="#36393f")
        self.input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        self.input_box = tk.Entry(
            self.input_frame,
            bg="#40444b",
            fg="#ffffff",
            font=("Helvetica", 12),
            insertbackground="#ffffff",
            border=0,
        )
        self.input_box.pack(fill=tk.X, side=tk.LEFT, padx=(0, 10), pady=5, ipady=5, expand=True)
        self.input_box.bind("<Return>", self.handle_enter)

        # Send button
        self.send_button = tk.Button(
            self.input_frame,
            text="Send",
            bg="#5865f2",
            fg="#ffffff",
            font=("Helvetica", 12, "bold"),
            activebackground="#4752c4",
            activeforeground="#ffffff",
            border=0,
            command=self.send_message,
        )
        self.send_button.pack(side=tk.RIGHT, padx=(0, 0), pady=5)

    def printIt(self, text):
        """Dynamically adds text to the chat display."""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, text + "\n")
        self.chat_display.yview(tk.END)  # Auto-scroll to the bottom
        self.chat_display.config(state=tk.DISABLED)

    def send_message(self):
        """Handles sending a message from the input box."""
        user_message = self.input_box.get().strip()
        if user_message:

            def clearScreen():
                self.input_box.delete(0, tk.END)
            
            def jarvisTask():
                printIt(f"{Username}: {user_message}")
                bot = jarvis(user_message)
                printIt(f"{Assistantname}: {bot}")

            threading.Thread(target=clearScreen, daemon=True).start()
            threading.Thread(target=jarvisTask, daemon=True).start()

            

    def handle_enter(self, event):
        """Handles pressing Enter to send a message."""
        self.send_message()

root = tk.Tk()
app = ChatApp(root)

def start_tkinter():
    root.mainloop()

# Function to integrate with other files
def printIt(text):
    app.printIt(text)


if __name__ == "__main__":
    start_tkinter()
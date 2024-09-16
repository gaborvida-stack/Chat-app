try:
    import socket
    import threading
    import tkinter as tk
    from tkinter import scrolledtext
    from tkinter import simpledialog
except ImportError as err:
    print("error occured: {}".format(err))


class ChatClient:
    def __init__(self, host, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

        self.gui_done = False
        self.running = True

        self.nickname = simpledialog.askstring("Nickname", "Please choose a nickname")

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        self.root = tk.Tk()
        self.root.configure(bg="lightgray")

        self.chat_label = tk.Label(self.root, text="Chat:", bg="lightgray")
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = scrolledtext.ScrolledText(self.root)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state="disabled")

        self.msg_label = tk.Label(self.root, text="Message:", bg="lightgray")
        self.msg_label.pack(padx=20, pady=5)

        self.input_area = tk.Text(self.root, height=3)
        self.input_area.pack(padx=20, pady=5)

        self.send_button = tk.Button(self.root, text="Send", command=self.write)
        self.send_button.pack(padx=20, pady=5)

        self.gui_done = True
        self.root.protocol("WM_DELETE_WINDOW", self.stop)
        self.root.mainloop()

    def write(self):
        message = f"{self.nickname}: {self.input_area.get('1.0', 'end')}"
        self.client.send(message.encode("utf-8"))
        self.input_area.delete("1.0", "end")

    def stop(self):
        self.running = False
        self.root.destroy()
        self.client.close()
        exit(0)

    def receive(self):
        while self.running:
            try:
                message = self.client.recv(1024).decode("utf-8")
                if message == "NICK":
                    self.client.send(self.nickname.encode("utf-8"))
                else:
                    if self.gui_done:
                        self.text_area.config(state="normal")
                        self.text_area.insert("end", message + "\n")
                        self.text_area.yview("end")
                        self.text_area.config(state="disabled")
            except ConnectionAbortedError:
                break
            except:
                print("error occurred!")
                self.client.close()
                break


def main():
    host = "127.0.0.1"
    port = 12345
    client = ChatClient(host, port)

if __name__ == "__main__":
    main()
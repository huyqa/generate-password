from tkinter import *
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x450")
        self.root.resizable(0, 0)
        self.root.title("Password Generator")

        self.heading = Label(root, text='PASSWORD GENERATOR', font='arial 15 bold')
        self.heading.pack()

        self.label_length = Label(root, text='PASSWORD LENGTH', font='arial 10 bold')
        self.label_length.pack()

        self.pass_len = IntVar()
        self.length = Spinbox(root, from_=8, to_=32, textvariable=self.pass_len, width=15)
        self.length.pack()

        self.pass_str = StringVar()

        self.generate_button = Button(root, text="GENERATE PASSWORD", command=self.generate_password)
        self.generate_button.pack(pady=5)

        self.password_entry = Entry(root, textvariable=self.pass_str, state='readonly', font='arial 12 bold', bd=5,
                                    relief=SUNKEN)
        self.password_entry.pack()

        self.copy_button = Button(root, text='COPY TO CLIPBOARD', command=self.copy_password)
        self.copy_button.pack(pady=5)

    def generate_password(self):
        password = ''
        for _ in range(4):
            password += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
        for _ in range(self.pass_len.get() - 4):
            password += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
        self.pass_str.set(password)

    def copy_password(self):
        password = self.pass_str.get()
        if password:
            pyperclip.copy(password)
            self.show_copy_info_label()
        else:
            print("No password to copy.")

    def show_copy_info_label(self):
        copy_info_label = Label(self.root, text='Password copied to clipboard!', font='arial 10 italic', fg='green')
        copy_info_label.pack()

if __name__ == "__main__":
    root = Tk()
    app = PasswordGenerator(root)
    root.mainloop()

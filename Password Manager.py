import base64
import os
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def load_key():
    file = open("key.key","rb")
    key = file.read().strip()
    file.close()
    return key


master_pwd = input("Enter your password: ")
salt = load_key()
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=480000,
)

key = base64.urlsafe_b64encode(kdf.derive(master_pwd.encode()))
fer = Fernet(key) 



def view():
    try:
        with open('passwords.txt', "r") as f: # type: ignore
            for i in f.readlines():
                data = i.rstrip()
                ussr, pwds = data.split("|")
                print("User:",ussr,"\n","Password: ",fer.decrypt(pwds.encode()).decode())
    except InvalidToken:
        print("invalid password")



def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open('passwords.txt', "a") as f: # type: ignore
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        





while True:
    mode = input("would you like to add a new password or view existing ones? press q to quit(add/view): ").lower()

    if mode == "q":
        print("Thank you for using the manager")
        quit()

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode selected.")
        continue
    

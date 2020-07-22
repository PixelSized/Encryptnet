from cryptography.fernet import Fernet
import base64
import os
import time
from os import system, name
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

name = os.getlogin()
print(r"""
╔═══════════════════════════════════════════════════════════════════════════════════════════════════════╗
  
  /$$$$$$$$                                                     /$$                           /$$    
 | $$_____/                                                    | $$                          | $$    
 | $$       /$$$$$$$   /$$$$$$$  /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$   /$$$$$$$   /$$$$$$  /$$$$$$  
 | $$$$$   | $$__  $$ /$$_____/ /$$__  $$| $$  | $$ /$$__  $$|_  $$_/  | $$__  $$ /$$__  $$|_  $$_/  
 | $$__/   | $$  \ $$| $$      | $$  \__/| $$  | $$| $$  \ $$  | $$    | $$  \ $$| $$$$$$$$  | $$    
 | $$      | $$  | $$| $$      | $$      | $$  | $$| $$  | $$  | $$ /$$| $$  | $$| $$_____/  | $$ /$$
 | $$$$$$$$| $$  | $$|  $$$$$$$| $$      |  $$$$$$$| $$$$$$$/  |  $$$$/| $$  | $$|  $$$$$$$  |  $$$$/
 |________/|__/  |__/ \_______/|__/       \____  $$| $$____/    \___/  |__/  |__/ \_______/   \___/  
                                          /$$  | $$| $$                                              
                                         |  $$$$$$/| $$                                              
                                          \______/ |__/

╚═══════════════════════════════════════════════════════════════════════════════════════════════════════╝
""")
print("╭────────────────────────────────────╮")
print(f"    Welcome to Encryptnet {name}")
print("╰────────────────────────────────────╯")

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


password_provided = "password"
password = password_provided.encode() 
salt = b'salt_'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA512(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))

statement = input("Would you like to encrypt or decrypt? \n answer with (e/d) \n::")

if statement == "e":
    a = input("\n Message to encode: \n ::")
    message = a.encode()
    f = Fernet(key)
    encrypted = f.encrypt(message)
    print("\n Code generated for encryption: \n" + str(encrypted)[2:-1])

    menu = input("\n Enter any key to reset: \n ::")
    if menu != "penisjuice":
        os.system('cls')
    else: 
        print("\n\nWhy the fuck would you type penisjuice if i asked you to type any key...")
        time.sleep(20)

elif statement == "d":
    a = input("\n Message to decode: \n ::")

    try:
        f = Fernet(key)
        string = bytes(a, encoding='utf-8')
        decrypted = f.decrypt(string)
        print("\n Decryption complete;\n Code generated for encryption: \n\n\n   " + str(decrypted)[2:-1])
        menu = input("\n\n Enter any key to reset: \n ::")
        if menu != "penisjuice":
            os.system('cls')
        else:
            print("\n\nWhy the fuck would you type penisjuice if i asked you to type any key...")
            time.sleep(20)

    except:
        print(f"\n\nYour decryption token: \n\n    {a} \n\nis not valid; restarting")
        time.sleep(5)
        os.system('cls')

else: 
    print(f'please choose either "encrypt" (e) or "decrypt" (d)')
    time.sleep(5)
    os.system('cls')

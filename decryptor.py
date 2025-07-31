import os
from cryptography.fernet import Fernet

key = input("Enter your decryption key: ").encode()
fernet = Fernet(key)

folder_path = "demo_folder"
note_filename = "READ_ME.txt"

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if filename.endswith(".locked"):
        with open(file_path, "rb") as file:
            encrypted_data = file.read()

        try:
            decrypted_data = fernet.decrypt(encrypted_data)
        except:
            print(f"[!] Wrong key or tampered file: {filename}")
            continue

        original_name = filename.replace(".locked", "")
        original_path = os.path.join(folder_path, original_name)

        with open(original_path, "wb") as file:
            file.write(decrypted_data)

        os.remove(file_path)
        print(f"[+] Decrypted and restored: {original_name}")


note_path = os.path.join(folder_path, note_filename)
if os.path.exists(note_path):
    os.remove(note_path)
    print(f"[+] Ransom note removed: {note_filename}")

print("[+] Decryption complete!")

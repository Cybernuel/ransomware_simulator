
# 🔐 Python Ransomware Simulator (Educational Only)

**Disclaimer:** This project is for **educational purposes only**. It is designed to simulate how ransomware works in a **controlled environment** for learning cybersecurity and malware analysis. **Do not use this on systems you do not own.**

---

## 📌 Features

* Encrypts all files in a selected folder using **AES-based Fernet encryption**
* Adds a `.locked` extension to simulate real ransomware behavior
* Drops a **custom ransom note** in UTF-8 to handle all characters
* Includes a **decryption script** to safely restore files
* Automatically removes `.locked` extension after decryption
* Handles **special characters** in filenames and ransom notes

---

## ⚙️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Cybernuel/ransomware_simulator.git
   cd python-ransomware-simulator
   ```

2. **Install the required Python libraries:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Project structure example:**

   ```
   python-ransomware-simulator/
   ├── encryptor.py        # Encrypt files in a folder
   ├── decryptor.py        # Decrypt files and restore them
   ├── requirements.txt    # Required Python packages
   ├── README.md           # Project documentation
   ```

---

## 🚀 Usage

### 1️⃣ **Encrypt Files**

Run the `encryptor.py` script and provide the folder path you want to simulate encryption on:

```bash
python encryptor.py
```

* All files in the folder will be encrypted
* A `.locked` extension will be added
* A ransom note (`READ_ME.txt`) will appear in the folder

---

### 2️⃣ **Decrypt Files**

Use the `decryptor.py` script with the **encryption key generated** by the encryptor:

```bash
python decryptor.py
```

* Files will be decrypted
* `.locked` extension will be removed
* Ransom note will be deleted automatically

---

## 📂 Example Workflow

1. Start with a folder of test files:

   ```
   /test_folder/
   ├── doc.txt
   ├── image.png
   ├── report.pdf
   ```

2. After encryption:

   ```
   /test_folder/
   ├── doc.txt.locked
   ├── image.png.locked
   ├── report.pdf.locked
   ├── READ_ME.txt
   ```

3. After decryption:

   ```
   /test_folder/
   ├── doc.txt
   ├── image.png
   ├── report.pdf
   ```

---

## ⚠️ Legal Notice

* This project is strictly for **cybersecurity education and testing**.
* Running it on machines or data you **do not own or have permission to test** may be illegal.
* Use responsibly to **understand ransomware and defend against it**.


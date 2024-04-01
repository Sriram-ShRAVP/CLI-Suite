import os
import random
import string
from Crypto.Cipher import AES, DES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii

# Custom Transposition Cipher Implementation
def encrypt_transposition_cipher(message, key):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key
    return ''.join(ciphertext)

def decrypt_transposition_cipher(ciphertext, key):
    num_of_rows = int(len(ciphertext) / key)
    num_of_shaded_boxes = (key * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_rows
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[row] += symbol
        row += 1
        if (row == num_of_rows) or (row == num_of_rows - 1 and col >= key - num_of_shaded_boxes):
            row = 0
            col += 1
    return ''.join(plaintext)

# Basic educational content
def basic_cybersecurity_concepts():
    print("\nBasic Cybersecurity Concepts:")
    print("""
    1. Confidentiality, Integrity, Availability (CIA Triad): Fundamental principles guiding cybersecurity.
    2. Authentication vs. Authorization: Ensuring users are who they claim to be and have permission to access resources.
    3. Encryption: The process of encoding messages or information in such a way that only authorized parties can access it.
    4. Firewalls and Antivirus Software: Tools to protect against unauthorized access and malware.
    5. Social Engineering: Manipulating people into performing actions or divulging confidential information.
    """)

# Encryption/Decryption Algorithms Menu
def encryption_decryption_menu():
    print("\nSelect the encryption/decryption algorithm:")
    algorithms = ["Transposition Cipher", "DES", "AES", "RSA"]
    for i, algo in enumerate(algorithms, start=1):
        print(f"{i}. {algo}")
    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        transposition_cipher()
    elif choice == 2:
        des_encryption_decryption()
    elif choice == 3:
        aes_encryption_decryption()
    elif choice == 4:
        rsa_encryption_decryption()
    else:
        print("Invalid choice or not yet implemented.")

# Transposition Cipher Example
def transposition_cipher():
    message = input("Enter message: ")
    key = int(input("Enter key (integer): "))
    encrypted = encrypt_transposition_cipher(message, key)
    decrypted = decrypt_transposition_cipher(encrypted, key)
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

# DES Encryption/Decryption Example
def des_encryption_decryption():
    key = DES.new(get_random_bytes(8), DES.MODE_ECB)
    data = pad(input("Enter message: ").encode(), DES.block_size)
    encrypted = key.encrypt(data)
    decrypted = unpad(key.decrypt(encrypted), DES.block_size)
    print(f"Encrypted: {binascii.hexlify(encrypted)}")
    print(f"Decrypted: {decrypted.decode()}")

# AES Encryption/Decryption Example
def aes_encryption_decryption():
    key = AES.new(get_random_bytes(16), AES.MODE_ECB)
    data = pad(input("Enter message: ").encode(), AES.block_size)
    encrypted = key.encrypt(data)
    decrypted = unpad(key.decrypt(encrypted), AES.block_size)
    print(f"Encrypted: {binascii.hexlify(encrypted)}")
    print(f"Decrypted: {decrypted.decode()}")

# RSA Encryption/Decryption Example
def rsa_encryption_decryption():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    
    message = input("Enter message: ").encode()
    encryptor = PKCS1_OAEP.new(RSA.import_key(public_key))
    encrypted = encryptor.encrypt(message)
    
    decryptor = PKCS1_OAEP.new(RSA.import_key(private_key))
    decrypted = decryptor.decrypt(encrypted)
    print(f"Encrypted: {binascii.hexlify(encrypted)}")
    print(f"Decrypted: {decrypted.decode()}")

# Password Generator
def generate_password():
    print("\nPassword Security Tips:")
    print("""
    1. Use long passwords (12+ characters).
    2. Mix uppercase, lowercase, symbols, and numbers.
    3. Avoid common dictionary words or patterns.
    4. Use a unique password for each important account.
    5. Consider a password manager. 
    """)
    length = int(input("Enter password length: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    print(f"Generated password: {password}")

# Main menu
def main_menu():
    while True:
        print("\nCybersecurity Education Suite")
        print("1. Learn Basic Cybersecurity Concepts")
        print("2. Encryption/Decryption Algorithms")
        print("3. Generate Secure Password")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            basic_cybersecurity_concepts()
        elif choice == '2':
            encryption_decryption_menu()
        elif choice == '3':
            generate_password()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

from hashlib import sha256
from cryptography.fernet import Fernet
import socket
import getpass
from gvm.connections import UnixSocketConnection
from gvm.protocols.gmp import Gmp
from gvm.errors import GvmError

# Function definitions

def hash_password(password):
    hashed_pw = sha256(password.encode()).hexdigest()
    print(f"\nSHA-256 Hashed Password: {hashed_pw}\n")

def generate_key():
    key = Fernet.generate_key()
    print(f"\nGenerated Key: {key.decode()}\n")
    return key

def encrypt_data(data, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data.encode())
    print(f"\nEncrypted Data: {encrypted.decode()}\n")
    return encrypted

def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_data).decode()
    print(f"\nDecrypted Data: {decrypted}\n")

def test_firewall_rule(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            print(f"\nPort {port} is open (firewall rule might be allowing traffic).\n")
        else:
            print(f"\nPort {port} is closed (firewall rule might be blocking traffic).\n")
    except socket.error as err:
        print(f"\nSocket error: {err}\n")

# GVM operations
def gvm_operations():
    connection = UnixSocketConnection()
    with Gmp(connection) as gmp:
        # Hardcoded credentials for demonstration purposes
        gmp.authenticate('admin', '89382f2a-1ad0-4b3b-b2a7-0a8c314cf377')
        print("\nAuthenticated to GVM.\n")
        # Example operation: Listing tasks
        tasks_xml = gmp.get_tasks()
        print("Tasks listed. (Further implementation required to parse and display tasks)")

# Main menu for the toolkit
def main_menu():
    while True:
        print("Security Toolkit Main Menu:")
        print("1. Hash a Password")
        print("2. Encrypt Data")
        print("3. Decrypt Data")
        print("4. Test Firewall Rule")
        #print("5. GVM (OpenVAS) Operations")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            password = input("Enter a password to hash: ")
            hash_password(password)
        elif choice == '2':
            data = input("Enter data to encrypt: ")
            key = generate_key()
            encrypted_data = encrypt_data(data, key)
        elif choice == '3':
            encrypted_data = input("Enter data to decrypt: ").encode()
            key = input("Enter decryption key: ").encode()
            decrypt_data(encrypted_data, key)
        elif choice == '4':
            ip = input("Enter IP address to test: ")
            port = int(input("Enter port number: "))
            test_firewall_rule(ip, port)
        elif choice == '5':
            gvm_operations()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main_menu()

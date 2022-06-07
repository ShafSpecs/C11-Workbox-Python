import string
import sys

alphabet: str = string.ascii_lowercase

print("Cipher App 2.0")

choice: int = int(input("""
What do you want to do?
1. Encrypt message
2. Decrypt message
3. Bruteforce an encrypted message

> """))


def encrypt_message(msg: str, key: int) -> str:
  msg = msg.split()
  encrypted_msg = ""
  
  for i in msg:
    encrypt_word = i.lower().translate(i.maketrans(alphabet, alphabet[key:] + alphabet[:key]))
    encrypted_msg = encrypted_msg + " " + encrypt_word
  
  return encrypted_msg


def decrypt_message(msg: str, key: int) -> str:
  msg = msg.split()
  decrypted_msg = ""
  
  for i in msg:
    decrypt_word = i.lower().translate(i.maketrans(alphabet[key:] + alphabet[:key], alphabet))
    decrypted_msg = decrypted_msg + " " + decrypt_word
  
  return decrypted_msg


def bruteforce(msg: str) -> None:
  msg = msg.split()
  
  for i in range(1, 27):
    decrypted_msg = ""
    for j in msg:
      decrypt_word = j.lower().translate(j.maketrans(alphabet[i:] + alphabet[:i], alphabet))
      decrypted_msg = decrypted_msg + " " + decrypt_word
      print(decrypted_msg)


def choice_one() -> None:
  print()
  print("Enter that secret message you want to send to....")
  message: str = input("Enter the message you want to send: ")
  key: int = int(input("Enter the key for the Caesar's cipher: "))
  print(encrypt_message(message, key))


def choice_two() -> None:
  print()
  print("Decrypting message you want to break.")
  message: str = input("Enter the encrypted message to break: ")
  key: int = int(input("Enter the key used for encrypting the message: "))
  print(decrypt_message(message, key))


def choice_three() -> None:
  print()
  print("Bruteforce the encrypted message.")
  message: str = input("Enter the encrypted message to bruteforce: ")
  bruteforce(message)


if choice == 1:
  choice_one()
elif choice == 2:
  choice_two()
elif choice == 3:
  choice_three()
else:
  print("Wrong choice!")
  sys.exit(1)

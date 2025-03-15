# Example 44 - Encrypting program

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

plain_text = input("Enter your message: ")
cipher_text = ""
decipher_text = ""

# Encryption
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Encrypted message: {cipher_text}")

# Decrypt
for letter in cipher_text:
    index = key.index(letter)
    decipher_text += chars[index]

print(f"Decrypted message: {decipher_text}")

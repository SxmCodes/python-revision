# This is to show that ECB mode is insecure.
import os
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import ECB

# to make the plaintext a multiple of the block size (16 bytes for AES). Padding is used in cryptography to ensure that data fits the required block size for certain encryption algorithms (like AES in ECB mode). Block ciphers operate on fixed-size blocks (e.g., 16 bytes for AES). If your plaintext isn't a multiple of the block size, you must add extra bytes—this is called "padding."
from cryptography.hazmat.primitives import padding
__name__ = "__main__ "

# Plaintext to be kept confidential
# here the b"" prefix indicates a bytes literal in Python, not unicode.
plaintext = b"This is the data!"
# Keys (256-bit AES key) 
key= os.urandom(32)  # Generate a random 256-bit key. 32 because 1 byte = 8 bits, so 32 bytes * 8 = 256 bits
# Encrypt
# Here we will use cryptography library's AES in ECB mode, and will create AES Cipher object.
cipher_object = Cipher(AES(key), ECB())

ciphertext = cipher_object .encryptor().update(plaintext)
# Note: ECB mode does not require an IV (Initialization Vector) as it is not a chaining mode.
print(f"Ciphertext: {ciphertext.hex()}") # by default it will give byte text, with use of hex() it will conver that into hexadecimal format.

# Decrupt
decryptedtext = cipher_object.decryptor().update(ciphertext)
print(f"Decrypted text: {decryptedtext.decode()}") 

# Now this didn't work, and the output is the short text "This is the data". This is because ECB mode is insecure and does not provide confidentiality.  

# NOTE:- The reason of this is, in order to make it work. The plaintext must be a multiple of the block size (16 bytes for AES), or in the multiple of 128 bits or 16 bytes.
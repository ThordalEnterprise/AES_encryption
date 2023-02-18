from Crypto.Cipher import AES

# Secret key for encryption
key = b'Sixteen byte key'

# Input string to be encrypted
plaintext = "This is a secret message XOXO"

# Pad the plaintext to a multiple of 16 bytes
pad_length = 16 - (len(plaintext) % 16)
plaintext = plaintext + (chr(pad_length) * pad_length)

# Initialization vector
iv = b'This is an IV456'

# Create a new AES cipher
cipher = AES.new(key, AES.MODE_CBC, iv)

# Encrypt the plaintext
ciphertext = cipher.encrypt(plaintext)

# Print the encrypted message
print("Encrypted message: " + ciphertext.hex())

# Secret key for decryption
key = b'Sixteen byte key'

# Initialization vector
iv = b'This is an IV456'

# Convert hex string to bytes
ciphertext = bytes.fromhex(ciphertext.hex())

# Create a new AES cipher
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt the ciphertext
plaintext = cipher.decrypt(ciphertext)

# Convert to string
plaintext = plaintext.decode()

# Remove the padding
pad_length = ord(plaintext[-1])
plaintext = plaintext[:-pad_length]

# Print the original message
print("Decrypted message: " + plaintext)

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Secret key for encryption
key = b'Sixteen byte key'

# Input string to be encrypted
plaintext = "This is a secret message XOXO"

# Pad the plaintext to a multiple of 16 bytes
pad_length = 16 - (len(plaintext) % 16)
plaintext = plaintext + (chr(pad_length) * pad_length)

# Generate a random initialization vector
iv = get_random_bytes(16)

# Create a new AES cipher using CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

# Encrypt the plaintext
ciphertext = cipher.encrypt(plaintext.encode())

# Print the encrypted message
print("Encrypted message: " + ciphertext.hex())

# Create a new AES cipher using CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt the ciphertext
decrypted_plaintext = cipher.decrypt(ciphertext)

# Remove the padding
pad_length = ord(decrypted_plaintext[-1])
decrypted_plaintext = decrypted_plaintext[:-pad_length]

# Print the original message
print("Decrypted message: " + decrypted_plaintext.decode())

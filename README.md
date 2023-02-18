# AES_encryption

[Intro]

This code shows an example of how to use the AES encryption and decryption functions provided by the PyCryptodome library to encrypt and decrypt a message using the CBC (Cipher Block Chaining) mode.

The code first initializes a secret key for encryption, generates an initialization vector (IV), and creates a new AES cipher object with the key and IV. It then pads the input plaintext to a multiple of 16 bytes, encrypts the plaintext using the AES cipher, and prints the resulting ciphertext in hexadecimal format.

To decrypt the ciphertext, the code initializes a new AES cipher object with the same key and IV, and then decrypts the ciphertext to obtain the original plaintext. It then removes the padding from the decrypted plaintext and prints the original message.

Note that this code is provided for educational purposes only, and should not be used for actual encryption or decryption of sensitive information without appropriate security measures in place.

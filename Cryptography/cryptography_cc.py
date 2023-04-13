# Caesar Cipher Encryption

def caesar_cipher_encrypt(plaintext, shift):
    """
    Encrypts plaintext using a Caesar cipher with the given shift value.
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext

# Take input file name from user
input_file = input("Enter input file name: ")

# Take output file name from user
output_file = input("Enter output file name: ")

# Take shift value from user
shift = int(input("Enter shift value: "))

# Read input file and encrypt its contents
with open(input_file, "r") as f:
    plaintext = f.read()
ciphertext = caesar_cipher_encrypt(plaintext, shift)

# Write encrypted contents to output file
with open(output_file, "w") as f:
    f.write(ciphertext)

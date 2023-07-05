def caesar_encrypt(plain_text, shift):
    encrypted_text = ""
    
    for char in plain_text:
        if char.isalpha():  # Only encrypt alphabetical characters
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    return encrypted_text


def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    
    for char in encrypted_text:
        if char.isalpha():  # Only decrypt alphabetical characters
            if char.isupper():
                decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    return decrypted_text


# Letting user encrypt thier own values
plaintext = input("Enter the text to encrypt: ")
shift_value = int(input("Enter the shift value: "))

encrypted = caesar_encrypt(plaintext, shift_value)
print("Encrypted text:", encrypted)

decrypted = caesar_decrypt(encrypted, shift_value)
print("Decrypted text:", decrypted)


       



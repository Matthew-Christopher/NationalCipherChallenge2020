def encrypt(text, shift):
    text = text.upper()
    result = ""
    for letter in text:
        result += chr((ord(letter) - 65 + shift) % 26 + 65) if 65 <= ord(letter) and ord(letter) <= 90 else letter

    return result

def decrypt(text, shift):
    return encrypt(text, ((26 - shift) % 26 + 26) % 26).lower()

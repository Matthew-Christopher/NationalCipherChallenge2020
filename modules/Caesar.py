def Encrypt(text, shift):
    text = text.upper()
    result = ""
    for letter in text:
        result += chr((ord(letter) - 65 + shift) % 26 + 65) if 65 <= ord(letter) and ord(letter) <= 90 else letter

    return result

def Decrypt(text, shift):
    return encrypt(text, ((26 - shift) % 26 + 26) % 26).lower()

def CaesarAuto(text):
    decrypts = []
    for s in range(26):
        decrypts.append(Decrypt(text, s))

    return(Analyse(decrypts))

from modules.EnglishDetect import DictionaryAnalysis
from modules.Mathematics import MultiplicativeModularInverse

def Encrypt(text, key):
    text = text.upper()
    result = ""
    for letter in text:
        result += chr((key[0] * ord(letter) - 65 + key[1]) % 26 + 65) if 65 <= ord(letter) and ord(letter) <= 90 else letter

    return result

def Decrypt(text, key):
    text = text.upper()
    result = ""
    for letter in text:
        result += chr((MultiplicativeModularInverse(key[0], 26) * (ord(letter) + 65 - key[1])) % 26 + 65) if 65 <= ord(letter) and ord(letter) <= 90 else letter

    return result

def AffineAuto(text):
    keys = []
    decrypts = []
    for a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]: # Consider where a is coprime with 26 only.
        for b in range(0, 26):
            keys.append([a, b])

    for key in keys:
        decrypts.append(Decrypt(text, key))

    optimalFitIndex = DictionaryAnalysis(decrypts)
    print(f'Optimsed fit calculated with key {keys[optimalFitIndex]}')
    return(decrypts[optimalFitIndex])

def AtbashAuto(text):
    return Decrypt(text, [25, 25])

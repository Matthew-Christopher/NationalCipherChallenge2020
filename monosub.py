from modules.EnglishDetect import *
from modules.Caesar import *

ciphertext = input("Enter ciphertext: ").upper()

print("1: Caesar\n2: Atbash\n3: Keyword\n4: Brute force")

menuselection = 0
while True:
    menuselection = int(input())
    if 1 <= menuselection and menuselection <= 4:
        break

if menuselection == 1:
    for s in range(26):
        print(decrypt(ciphertext, s))

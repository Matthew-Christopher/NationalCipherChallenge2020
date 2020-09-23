from modules.Caesar import CaesarAuto

ciphertext = input("Enter ciphertext: ").upper()

print("1: Caesar\n2: Atbash\n3: Affine\n3: Keyword\n4: Brute force")

menuselection = 0
while True:
    menuselection = int(input())
    if 1 <= menuselection and menuselection <= 4:
        break

if menuselection == 1:
    print(CaesarAuto(ciphertext))

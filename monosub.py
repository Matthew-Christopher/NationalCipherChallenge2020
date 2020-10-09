from modules.SubmissionTools import CopyForSubmission

from modules.Caesar import CaesarAuto
from modules.Affine import AtbashAuto, AffineAuto
from modules.Monoalphabetic import BruteForce

ciphertext = input("Enter ciphertext: ").upper()

print("1: Caesar\n2: Atbash\n3: Affine\n4: Brute Force")

menuselection = 0
while True:
    menuSelection = int(input("Enter ciphertext type: "))
    if 1 <= menuSelection and menuSelection <= 4:
        break

if menuSelection == 1:
    answer = CaesarAuto(ciphertext)
elif menuSelection == 2:
    answer = AtbashAuto(ciphertext)
elif menuSelection == 3:
    answer = AffineAuto(ciphertext)
elif menuSelection == 4:
    answer = BruteForce(ciphertext)

print(f"\"{answer}\"")

CopyForSubmission(answer)
print('The answer has been copied to the clipboard and is ready for final submission.')

input('Press any key to quit.')

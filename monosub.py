from modules.SubmissionTools import CopyForSubmission

from modules.Caesar import CaesarAuto
from modules.Affine import AtbashAuto, AffineAuto
from modules.EnglishDetect import DictionaryAnalysis

ciphertext = input("Enter ciphertext: ").upper()

print("1: Caesar\n2: Atbash\n3: Affine\n4: Keyword\n5: Brute force")

menuselection = 0
while True:
    menuSelection = int(input("Enter ciphertext type: "))
    if 1 <= menuSelection and menuSelection <= 5:
        break

if menuSelection == 1:
    answer = CaesarAuto(ciphertext)
elif menuSelection == 2:
    answer = AtbashAuto(ciphertext)
elif menuSelection == 3:
    answer = AffineAuto(ciphertext)

print(f"\"{answer}\"")

CopyForSubmission(answer)
print('The answer has been copied to the clipboard and is ready for final submission.')

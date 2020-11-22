from modules.SubmissionTools import CopyForSubmission

ciphertext = input("Enter ciphertext: ").upper()

blockLength = 5;

perm = input("Enter blockwise permutation: ")

ciphertext = ciphertext.replace(" ", "");
answer = [""] * len(ciphertext);

i = 0
while i <= (len(ciphertext) - 4):
    for r in range(5):
        answer[r + i] = ciphertext[i + (ord(perm[r]) - 49)]
    i += 5

print("".join(answer))

CopyForSubmission("".join(answer))
print('The answer has been copied to the clipboard and is ready for final submission.')

input('Press any key to quit.')

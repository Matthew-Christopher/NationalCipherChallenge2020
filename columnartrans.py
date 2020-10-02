from modules.SubmissionTools import CopyForSubmission

from modules.Columnar import ColumnarAuto

ciphertext = input("Enter ciphertext: ").upper()

answer = ColumnarAuto(ciphertext)

print(f"\"{answer}\"")

CopyForSubmission(answer)
print('The answer has been copied to the clipboard and is ready for final submission.')

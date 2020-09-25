import os.path
import math

DICTIONARY_PATH = os.path.join(os.path.dirname(__file__), 'Dictionary.txt')

def DictionaryAnalysis(decrypts, weighting):
    decrypts = [x.replace(' ', '') for x in decrypts]

    dictionary = []

    if not os.path.isfile(DICTIONARY_PATH):
        print("Dictionary file not found, aborting.")
        return 0
    else:
        with open(DICTIONARY_PATH) as dictionaryFile:
            for wordEntry in dictionaryFile:
                dictionary.append(wordEntry.strip().lower())

    optimisedDecryptionIndex = 0
    optimisedDecryptionFit = 0

    print(f"Analysing candidate decryptions with weighting {weighting}")
    lengthToCheck = math.floor(float(len(decrypts[0])) * weighting)

    for currentIndex, decrypt in enumerate(decrypts):
        fitness = 0
        for i in range(lengthToCheck):
            for j in range(i + 3, lengthToCheck + 1):
                if decrypt[i:j] in dictionary:
                    fitness += 1

        if fitness > optimisedDecryptionFit:
            optimisedDecryptionIndex = currentIndex
            optimisedDecryptionFit = fitness

    return optimisedDecryptionIndex

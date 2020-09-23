import os.path

DICTIONARY_PATH = os.path.join(os.path.dirname(__file__), 'Dictionary.txt')

def SmallKeySpaceAnalyse(decrypts):
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

    for currentIndex, decrypt in enumerate(decrypts):
        fit = 0
        for word in decrypt.split(' '):
            if word.lower() in dictionary:
                fit += 1

        if fit > optimisedDecryptionFit:
            optimisedDecryptionIndex = currentIndex
            optimisedDecryptionFit = fit

    return optimisedDecryptionIndex

import os.path
import math
import re

from modules.trie3rdparty import Trie

DICTIONARY_PATH = os.path.join(os.path.dirname(__file__), 'Dictionary.txt')

def DictionaryAnalysis(decrypts):
    decrypts = [x.replace(' ', '') for x in decrypts]

    dictionary = []

    if not os.path.isfile(DICTIONARY_PATH):
        print("Dictionary file not found, aborting.")
        return 0
    else:
        with open(DICTIONARY_PATH) as dictionaryFile:
            dictionary = [word.strip().lower() for word in dictionaryFile if len(word.strip()) >= 3] # Match trigrams or longer only.

    optimisedDecryptionIndex = 0
    optimisedDecryptionFit = 0

    print(f"Analysing candidate decryptions")

    for currentIndex, decrypt in enumerate(decrypts):
        fitness = 0
        trie = Trie()
        for word in dictionary:
            trie.add(word)

        fitness = len(re.findall(trie.pattern(), decrypt))

        if fitness > optimisedDecryptionFit:
            optimisedDecryptionIndex = currentIndex
            optimisedDecryptionFit = fitness

    return optimisedDecryptionIndex

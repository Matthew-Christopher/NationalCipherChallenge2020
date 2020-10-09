import os.path
import re

from modules.Trie import Trie
from modules.Mathematics import SetLogProbabilities, BaseScore

DICTIONARY_PATH = os.path.join(os.path.dirname(__file__), 'Dictionary.txt')
QUADGRAM_PATH = os.path.join(os.path.dirname(__file__), 'Quadgrams.txt')

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

class QuadgramScorer:
    def __init__(self):
        self.quadgramFrequencies = {}

        with open(QUADGRAM_PATH) as quadgramFile:
            for line in quadgramFile:
                quadgram, frequency = line.split(' ')
                self.quadgramFrequencies[quadgram] = int(frequency)

        self.total = sum(self.quadgramFrequencies.values())

        SetLogProbabilities(self.quadgramFrequencies)

        self.baseScore = BaseScore(self.total)

    def QuadgramFitness(self, candidate):
        fitness = 0

        for i in range(len(candidate) - 3): # Stop before the end of the text.
            if candidate[i : i+4] in self.quadgramFrequencies:
                fitness += self.quadgramFrequencies[candidate[i : i+4]] # Add the associated log probability to the fitness.
            else:
                fitness += self.baseScore

        return fitness

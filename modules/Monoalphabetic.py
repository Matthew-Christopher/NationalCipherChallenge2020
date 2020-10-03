# Automatically decrypt any monoalphabetic substitution cipher with hill-climbing.

import random
import string
import re

from modules.EnglishDetect import QuadgramFitness

def BruteForce(ciphertext):
    key = list(string.ascii_uppercase) # Begin with a random key.
    random.shuffle(key)

    score = QuadgramFitness(Decrypt(ciphertext, key))

    iterationsBeforeComplete = 1000 # Wait for this many iterations without an improvement in quadgram fitness before we think the cipher has been broken.

    print("Attempting brute force decryption by quadgram fitness hill-climbing.\nThis may take some time, press CTRL+C to abort at any time.")

    iterations = 0
    while iterations < iterationsBeforeComplete:
        # Make a random key pair swap. If the quadgram fitness improves, assume this as the new key.
        index1 = random.randint(0, 25) # We do this so many times that we can ignore checking that these are not duplicates.
        index2 = random.randint(0, 25)
        newKey = key
        newKey[index1], newKey[index2] = newKey[index2], newKey[index1] # Perform the key pair swap.
        newScore = QuadgramFitness(Decrypt(ciphertext, newKey))
        iterations += 1

        if newScore < score:
            print(newKey)
            key = newKey
            score = newScore
            iterations = 0

    print(f"Best key: {key}")
    return Decrypt(ciphertext, key)

def Decrypt(ciphertext, key):

    if len(key) != 26:
        print("Malformed key. Aborting.")
        return

    return ''.join([string.ascii_uppercase[key.index(c)] for c in ciphertext if c.isalpha()])

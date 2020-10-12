# Automatically decrypt any monoalphabetic substitution cipher with hill-climbing.

import random
import string
import re

from modules.EnglishDetect import QuadgramScorer

def BruteForce(ciphertext):
    key = list(string.ascii_uppercase) # Begin with a random key.

    iterationsBeforeComplete = 1500 # Wait for this many iterations without an improvement in quadgram fitness before we think the cipher has been broken.

    print("Attempting brute force decryption by quadgram fitness hill-climbing.\nThis may take some time, press CTRL+C to abort at any time.")

    scorer = QuadgramScorer()

    maxScore = -1e99
    maxKey = ""

    maxRuns = 200

    runs = 0
    while runs < maxRuns:
        maxChangedThisRun = False
        runs += 1
        random.shuffle(key)
        score = scorer.QuadgramFitness(Decrypt(ciphertext, key))
        iterations = 0
        while iterations < iterationsBeforeComplete:
            # Make a random key pair swap. If the quadgram fitness improves, assume this as the new key.
            index1 = random.randint(0, 25) # We do this so many times that we can ignore checking that these are not duplicates.
            index2 = random.randint(0, 25)
            newKey = key[:]
            newKey[index1], newKey[index2] = newKey[index2], newKey[index1] # Perform the key pair swap.
            newScore = scorer.QuadgramFitness(Decrypt(ciphertext, newKey))
            iterations += 1

            if newScore > score:
                key = newKey[:]
                score = newScore
                iterations = 0
                if newScore > maxScore:
                    maxScore = newScore
                    maxKey = newKey
                    maxChangedThisRun = True

        if maxChangedThisRun:
            print(f"Run {runs}\nBest key: {''.join(maxKey)} with score {maxScore}")

            print(f"Best plaintext: \"{Decrypt(ciphertext, maxKey)[0:30]}...\"")
            if (input("Press enter to continue or type any text to use this decryption.") != ""): break

    return Decrypt(ciphertext, maxKey)

def Decrypt(ciphertext, key):

    if len(key) != 26:
        print("Malformed key. Aborting.")
        return

    return ''.join([string.ascii_uppercase[key.index(c)] if c.isalpha() else c for c in ciphertext])

import itertools
import datetime
import time

def generate_permutations(alphabet, length):
    permutations = itertools.product(alphabet, repeat=length)
    return [''.join(p) for p in permutations]

english_alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'
permutations = generate_permutations(english_alphabet, 8)

myPassword = "ab12cd45"

for passwd in permutations:
    timeTaken = datetime.datetime.now()
    print("Cracking...", passwd)
    if(passwd == myPassword):
        timeTaken = datetime.datetime.now() - timeTaken
        print("Password Cracked in ", timeTaken, " sec")
        break


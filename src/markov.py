"""Depois documento.
"""


import random
from operator import itemgetter


DATA_DIR = '../data/'


def readletters(filein):
    lines = filein.readlines()
    probs = dict()

    for line in lines:
        linelen = len(line)
        key = line[0]
        probs[key] = float(line[2 : linelen - 1])

    return probs

def generate(probs, numlines, linelen):
    text = ''

    probs = sorted(probs.items(), key=itemgetter(1))

    for _ in range(numlines):
        line = ''

        for _ in range(linelen):
            prob = random.random()  #between 0 and 1
            for (key, value) in probs:
                if prob <= value:
                    line = '%s%s' % (line, key)
                    break

        text = '%s%s\n' % (text, line)

    return text


if __name__ == '__main__':
    import sys

    numlines = 100
    linelen = 200

    if 'generate' in sys.argv:
        filein = open('%sshakespeare.letters' % DATA_DIR, 'r')
        probs = readletters(filein)
        text = generate(probs, numlines, linelen)

        fileout = open('%sgenerated.txt' % DATA_DIR, 'w')
        fileout.write(text)
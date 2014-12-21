"""Puts the content of file "shakespeare.txt" in a better format. Creates a base
of relative frequencies of letters (with space) and words.
"""


import re
import string


DATA_DIR = '../data/'


def prebase(filein, fileout):
    """Reads from filein and writes in fileout words composed of letters only.
    """
    lines = filein.readlines()

    for line in lines:
        line = line.strip(' ')
        words = line.split()
        newline = ''

        for word in words:
            word = word.strip(' ')
            word = re.sub('[^a-z ]', '', word)
            word = re.sub(' +', ' ', word)
            word = word.strip(' ')
            newline = '%s%s ' % (newline, word)

        newline = '%s' % newline.strip(' ')
        if newline != '':
            fileout.write('%s\n' % newline)

def countletters(filein, fileout):
    """Counts the letters from filein. By default its a "Markov" of order ZERO
    (zero-memory source).
    """
    alphabet = ' %s' % string.ascii_lowercase   #with empty space
    counts = dict()
    lines = filein.readlines()

    for line in lines:
        for letter in alphabet:
            count = line.count(letter)
            if letter in counts:
                counts[letter] = counts[letter] + count
            else:
                counts[letter] = count

    total = sum(counts.values())
    for letter in sorted(counts.keys()):
        prob = counts[letter] / total
        fileout.write('%s %f\n' % (letter, prob))


if __name__ == '__main__':
    import sys

    if 'prebase' in sys.argv:
        filein = open('%sshakespeare.txt' % DATA_DIR, 'r')
        fileout = open('%sshakespeare.dat' % DATA_DIR, 'w')
        prebase(filein, fileout)

    if 'countletters' in sys.argv:
        filein = open('%sshakespeare.dat' % DATA_DIR, 'r')
        fileout = open('%sshakespeare.letters' % DATA_DIR, 'w')
        countletters(filein, fileout)
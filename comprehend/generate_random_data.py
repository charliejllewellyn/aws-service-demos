from random import randint

with open('words.txt', 'r') as f:
    wordList = f.readlines()

with open('drugs.txt', 'r') as f:
    drugList = f.readlines()

# 330 25487
for _ in range(2000):
    startLength = randint(4, 9)
    endLength = randint(4, 9)
    sentence = []

    for _ in range(startLength):
        randomWord = randint(0, 25486)
        sentence.append(wordList[randomWord].rstrip())

    randomDrug = randint(0, 328)
    sentence.append(drugList[randomDrug].rstrip())

    startLength = randint(4, 9)
    endLength = randint(4, 9)
    for _ in range(startLength):
        randomWord = randint(0, 25486)
        sentence.append(wordList[randomWord].rstrip())

    print(' '.join(sentence))

import random

word_map = dict()

def get_start_word(words):
    start_word = False
    a = ord('A')
    z = ord('Z')
    while not start_word:
        word = random.choice(words)
        if ord(word[0]) in range(a, z) or (word[0] == '"' and ord(word[1]) in range(a, z)):
            start_word = word
    return start_word 

def is_stop_word(word):
    end_marks = '.?!'
    quotes = ['"', "'"]
    if word[-1] in end_marks:
        return True
    elif word[-1] in quotes and word[-2] in end_marks:
        return True
    else:
        return False

with open("input.txt") as f:
    words = f.read().split()
    for i, word in enumerate(words):
        if i == len(words)-1:
            break
        if word_map.get(word):
            word_map[word].append(words[i+1])
        else:
            word_map[word] = [words[i+1]]

sents = 0
stop_word = True
while sents < 5:
    if stop_word:
        word = get_start_word(words)
        stop_word = False
    else:
        word = random.choice(word_map[word])
    print(word, end=" ")
    if is_stop_word(word):
        sents += 1
        stop_word = True

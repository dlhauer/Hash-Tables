ignored_chars = [
        '"', ':', ';', ',', '.', '-', '+', '=', 
        '/', '\\', '|', '[', ']', '{', '}', '(',
         ')', '*', '^', '&'
    ]

histogram = dict()

with open("robin.txt") as f:
    words = f.read().split()
    max_length = 0
    for i, word in enumerate(words):
        word = word.lower()
        for char in ignored_chars:
            word = word.replace(char, '')
        if len(word) == 0:
            continue
        if len(word) > max_length:
            max_length = len(word)
        if histogram.get(word):
            histogram[word] += '#'
        else:
            histogram[word] = '#'

histogram = sorted(histogram.items(), 
                   key=lambda h: (-len(h[1]), h[0]))

for word, hashes in histogram:
    print(word + (' ' * (max_length-len(word))) + '  ' + hashes)

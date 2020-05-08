def word_count(s):
    ignored_chars = [
        '"', ':', ';', ',', '.', '-', '+', '=', 
        '/', '\\', '|', '[', ']', '{', '}', '(',
         ')', '*', '^', '&'
    ]
    counts = dict()
    for word in s.split():
        word = word.lower()
        for char in ignored_chars:
            word = word.replace(char, '')
        if len(word) == 0:
            return counts
        if counts.get(word):
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
        
        


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
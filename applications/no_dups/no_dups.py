def no_dups(s):
    unique_arr = []
    words = dict()
    for word in s.split():
        if word not in words:
            words[word] = True
            unique_arr.append(word)
    return ' '.join(unique_arr)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
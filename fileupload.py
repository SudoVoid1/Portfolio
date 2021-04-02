word = []
with open('MyFile.txt') as f:
    for line in f:
        word = [line.strip()]
        print(word)

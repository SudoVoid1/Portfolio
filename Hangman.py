import random

word = []
with open('MyFile.txt') as f:
    for line in f:
        word = [line.strip()]
        #print(word)

random.shuffle(word)

answer = list(word[0])

display = []

used = []

display.extend(answer)

used.extend(display)
#print(used) will show answer

for i in range (len(display)):
    display[i] = "_"
print(' '.join(display))
print()

count = 0
incorrect = 8

while count < len(answer) and incorrect > 0:
    guess = input("Please guess a letter:")
    guess = guess.lower()
    print(count)

    for i in range(len(answer)):
        if answer[i] == guess and guess in used :
            display[i] = guess
            count = count +1
            used.remove(guess)
    if guess not in display:
        incorrect = incorrect - 1
        print("Sorry, that letter is not in the word")
    print("You have guessed:",count, "correct letters.")
    print("You have:",incorrect, "guesses left.")

    print(' '.join(display))
    print()
if count == len(answer):
    print("You guessed the word!")
else:
    print("You ran out of guesses")
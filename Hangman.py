import random
from Hangman_Sources import logo
from Hangman_Sources import stages
from Hangman_Sources import words

print(logo)
choosen_word = random.choice(words)
print(choosen_word)
display = []
for i in range(len(choosen_word)):
    display.append("_")

char_positions = {}
for i, char in enumerate(choosen_word):
    if char not in char_positions:
        char_positions[char] = []
    char_positions[char].append(i)

num_random_letters = min(len(choosen_word) // 2, 3)
random_letters = random.sample(choosen_word, num_random_letters)

for letter in random_letters:
    positions = char_positions[letter]
    pos = random.choice(positions)
    display[pos] = letter

print(display)
level = 6
while "_" in display:
    guess = input("Guess a letter : ")
    guess = guess.lower()
    flag = False
    for i in range(len(choosen_word)):
        if choosen_word[i] == guess:
            display[i] = guess
            flag = True
    if not flag:
        print(f"You guessed {guess}, that's not in the word. You lose a life ")
        level = level - 1
    print(stages[level])
    print(display)
    if level == 0:
        print("You lose")
        break

if not level == 0:
    print("You win")

import random
words_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(words_list)
print(chosen_word)
display = []
for _ in chosen_word:
    display.append("_")
print(display)
end_game = False
lives = 6
while not end_game:
    user_guess = input("guess a letter: ").lower()
    for word in range(len(chosen_word)):
        letter = chosen_word[word]
        if letter == user_guess:
            display[word] = letter
    print(display)

    if user_guess not in chosen_word:
        lives -= 1
        print(f"you have {lives} left")
        if lives == 0:
            print("you lose")
            end_game = True
    print(f"{''.join(display)}")

    if "_" not in display:
        print("you won")
        end_game = True


import random
game_over = False
correct_letters= []
world_list= ["aardavak","racoon","camel"]
chosen_word = random.choice(world_list)
print(chosen_word)
placeholder = ""
wordlength = len(chosen_word)
for position in range(wordlength):
    placeholder += "_"
print(placeholder)
while not game_over:
    guess = input("guess a letter: ").lower()

    display= ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+= letter
        else:
            display += "_"
    print(display)
    if "_" not in display:
        game_over = True
        print("u won") 
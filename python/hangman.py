import random


def main():

    word_to_guess = random.choice(["alpha", "course", "onepiece", "why"])
    len_word_to_guess = len(word_to_guess)
    empty_word = len_word(len_word_to_guess)
    print(empty_word)
    life_point = 8
    while(empty_word != word_to_guess):
        print("lifes left:", life_point)
        letter = input("guess a letter:\n")

        old_word = empty_word

        if(len(letter) > 1 or letter.isnumeric() or letter.isupper()):
            print("Error plz enter one letter thet is lowercase\n")
            print(empty_word)
            continue
        for i in range(len_word_to_guess):
            if(letter in word_to_guess):
                empty_word = empty_word[:i] + letter + empty_word[i+1:]

        if(empty_word == old_word):
            life_point -= 1
            if(life_point < 0):
                break
        print("you update word is:", empty_word)

    if(life_point <= 0):
        print("you lost the game")
    else:
        print("you haved guess the word!!!!")


def len_word(word):
    new_word = ""
    for i in range(word):
        new_word += "_"
    return new_word


if (__name__ == "__main__"):
    main()

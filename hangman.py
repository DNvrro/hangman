import random

def hangman():
    word_list = ['love', 'Python', 'liam', 'computer']
    random_number = random.randint(0, 3)
    word = word_list[random_number]
    wrong_guesses = 0
    stages = ["",
              "_________        ",
              "                 ",
              "         |       ",
              "         0       ",
              "        /|\      ",
              "        / \      ",
              "                 "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong_guesses < len(stages) - 1:
        print("\n")
        guess = input("Guess a letter")

        if guess in rletters:
            cind = rletters.index(guess)
            board[cind] = guess
            rletters[cind] = '$'
        else:
            wrong_guesses += 1
        print((" ".join(board)))
        e = wrong_guesses + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win!!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong_guesses]))
        print("You Lose! The correct word was {}!".format(word))

hangman()

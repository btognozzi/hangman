import random


def hangman():
#game setup
    word_list = ["cat", "tree", "top", "magnet", "friend"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong = 0
    stages = ["",
             "________      ",
             "|             ",
             "|        |    ",
             "|        O    ",
             "|       /|\   ",
             "|       / \   ",
             "|             "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
#loop to keep game running
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
              print("You win!")
              print(" ".join(board))
              win = True
              break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))


hangman()

from random import choice


class RockPaperSci:
    combinations = []

    def __init__(self):
        self.name = ""
        self.exist = True
        rating_file = open("rating.txt", "r")
        self.lines = rating_file.readlines()
        rating_file.close()
        self.player_line = None
        self.rating = 0
        combinations_file = open("combinations.txt", "r")
        self.combinations = [x.replace("\n", "") for x in combinations_file.readlines()]
        self.game_settings = ["rock", "paper", "scissors"]

    def find_rating(self):
        for i in range(len(self.lines)):
            if self.name == self.lines[i].split()[0]:
                self.rating = int(self.lines[i].split()[1].replace("\n", ""))
                self.player_line = i
                break
        else:
            self.exist = False

    def set_game(self, settings):
        if len(settings) == 0:
            return
        else:
            self.game_settings = settings

    def game(self):
        self.name = input("Enter your name: ")
        print(f"Hello, {self.name}")
        self.find_rating()
        settings = input().split(",")
        print("Okay, let's start")
        while True:
            n = input()
            if n == "!exit":
                if self.exist:
                    file = open("rating.txt", "w")
                    self.lines[self.player_line] = f"{self.name} {self.rating}\n"
                    file.writelines(self.lines)
                    file.close()
                else:
                    file = open("rating.txt", "a")
                    file.write(f"{self.name} {self.rating}\n")
                    file.close()
                break
            elif n == "!rating":
                print(f"Your rating: {self.rating}")
            elif n not in self.combinations:
                print("Invalid input")
            else:
                self.one_round(n)
        print("Bye")

    def one_round(self, player_choice):
        cp = choice(self.game_settings)
        ind = self.combinations.index(cp)
        if ind + 8 <= 14:
            lt = start.combinations[ind + 1:ind + 8]
        else:
            lt = start.combinations[ind + 1:ind + 7]
            lt.extend(start.combinations[:ind + 7 - 14])
        if player_choice == cp:
            print(f"There is a draw ({cp})")
            self.rating += 50
        elif player_choice not in lt:
            print(f"Well done. The computer chose {cp} and failed")
            self.rating += 100

        else:
            print(f"Sorry, but the computer chose {cp}")


start = RockPaperSci()
start.game()

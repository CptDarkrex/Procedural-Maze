import random


class GuessingContainer:
    def __init__(self):
        self.number = 0
        self.max_num = 10
        self.min_num = 1
        self.tries = 1
        self.max_tries = 3

    def number_picker(self):
        self.number = random.randint(self.min_num, self.max_num)
        return self.number

    def print_game(self):
        try:
            plr_guess = int(input(f"Pick a number from {self.min_num} and {self.max_num}: "))

        except ValueError:
            print("Please choose a number")
            self.print_game()

        else:
            if plr_guess == self.number:
                print("Congratulations You Won!")
                self.tries = 1
                return

            elif self.tries != 3:
                self.tries += 1
                print("Wrong, ", f"Current Tries: {self.tries}/{self.max_tries}")
                if plr_guess < self.number:
                    print("Higher")
                else:
                    print("Lower")

                print("")
                self.print_game()

            else:
                print(f"You lose! the number was: {self.number}.")
                self.tries = 1
                return

    def run_game(self):
        self.number_picker()
        self.print_game()

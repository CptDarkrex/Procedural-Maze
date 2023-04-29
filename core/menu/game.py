from __future__ import annotations
from cogs import MazeContainer, GuessingContainer


class MainMenu:
    def __init__(self):
        self.maze = MazeContainer()
        self.guess_cont = GuessingContainer()

    def launch(self):
        choice = 0
        while choice != "4":

            print("*****************************************")
            print()
            print("Choose an option from the following menu: ")
            print()
            print("1 - Text-based Maze Game")
            print("2 - Guessing Game")
            print("3 - Quiz")
            print("4 - Exit")
            print()
            print("******************************************")
            print()
            choice = input("Enter 1, 2, 3 or 4: ")

            if choice == "1":
                self.maze_game()

            elif choice == "2":
                self.number_guesser()

            elif choice == "3":
                self.quiz()

            elif choice == "4":
                print("Thanks for using the program.")
                return exit(0)

            else:
                print("Please enter 1,2,3 or 4 only")

    def maze_game(self):
        print()
        print("Now running Maze game...")
        self.maze.run_game()
        self.launch()

    def number_guesser(self):
        print()
        print("Now running Guessing game")
        self.guess_cont.run_game()
        self.launch()

    def quiz(self):
        print()
        print("Now running Quiz")
        self.launch()

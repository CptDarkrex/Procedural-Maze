from __future__ import annotations
from cogs import MazeContainer, GuessingContainer,QuizContainer
from modules import Loader
from time import sleep


class MainMenu:
    def __init__(self):
        self.maze = MazeContainer()
        self.guess_cont = GuessingContainer()
        self.quiz_game = QuizContainer()

        self.loader = Loader()
        self.inst_loader = ''

        self.choices = []
        self.choice = None

        self.running = False

    def launch(self):
        while self.choice != 4:
            self.interactable_menu()

            if self.choice == 1:
                self.maze_game()

            elif self.choice == 2:
                self.number_guesser()

            elif self.choice == 3:
                self.quiz()

            elif self.choice == 4:
                print("Thanks for using the program.")
                return exit(0)

            else:
                print("Please enter 1,2,3 or 4 only")

    def interactable_menu(self):
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
        self.choice = int(input("Enter 1, 2, 3 or 4: "))

    def maze_game(self):
        print()
        self.load()
        print()

        # Core for launch
        print("Now running Maze game...")
        self.maze.run_game()
        self.launch()

    @staticmethod
    def load():
        loader = Loader("Loading object", "That was fast!", 0.3).start()
        for i in range(10):
            sleep(0.4)
        loader.stop()

    def number_guesser(self):
        print()
        self.load()
        print()
        print("Now running Guessing game")
        self.guess_cont.run_game()
        self.launch()

    def quiz(self):
        print()
        self.load()
        print()
        print("Now running Quiz...")
        # Read questions from the JSON file
        question_data = self.quiz_game.read_questions_from_json()

        # Start the quiz
        total_score = self.quiz_game.start_quiz(question_data)
        # Display final score
        print("\nQuiz Complete!")
        print("Total Score:", total_score)
        self.launch()

import random
import json


class QuizContainer:
    def __init__(self):
        # Path to the JSON file
        self.json_file_path = 'cogs/quiz_game/data.json'
    # Read questions from JSON file

    def read_questions_from_json(self):
        with open(self.json_file_path, 'r') as json_file:
            data = json.load(json_file)
            return data

    # Ask a question and check the answer
    def ask_question(self, question, answer):
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            return 1
        else:
            print("Incorrect!")
            return 0

    # Main Quiz Function
    def start_quiz(self, questions):
        score = 0
        for theme, theme_questions in questions.items():
            print("\nTheme:", theme)
            for i, question_data in enumerate(theme_questions):
                question = question_data['question']
                answer = question_data['answer']
                print("\nQuestion", i + 1)
                score += self.ask_question(question, answer)
        return score

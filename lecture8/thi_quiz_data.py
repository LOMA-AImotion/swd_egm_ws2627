# -*- coding: utf-8 -*-
"""
thi_quiz_data.py

Reads quiz data from a txt file like quiz_functions.txt
and returns a list of tuples of the form (question, answers, index of correct answer)

For example [("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 2), ...]

Created on Tue Nov 25 2026

@author: THI SWD EGM
"""

def read_quiz_data(file_path: str) -> list[tuple[str, list[str], int]]:
    """
    Reads quiz data from a txt file and returns a list of tuples of the form (question, answers, index of correct answer)
    
    Args:
        file_path (str): The path to the quiz data file.
        
    Returns:
        list[tuple[str, list[str], int]]: A list of tuples containing the question, answers, and index of the correct answer.
    """
    quiz_data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        question_count = int(lines[0].strip())
        line_index = 1

        for question_number in range(question_count):
            # Skip empty lines
            while line_index < len(lines) and not lines[line_index].strip():
                line_index += 1

            if line_index >= len(lines):
                raise ValueError(f"Missing question {question_number + 1}.")

            question = lines[line_index].strip()
            line_index += 1
            answers = []
            correct_index = None

            while line_index < len(lines):
                answer = lines[line_index].strip()
                line_index += 1
                # Skip empty lines
                if not answer:
                    continue

                if answer.startswith("CORRECT:"):
                    correct_index = len(answers)
                    answer = answer[len("CORRECT:"):].strip()

                answers.append(answer)
                if correct_index is not None:
                    break

            if correct_index is None:
                raise ValueError(f"Question {question_number + 1} has no marked correct answer.")

            quiz_data.append((question, answers, correct_index))
    return quiz_data


if __name__ == "__main__":
    from pathlib import Path

    quiz_file = Path(__file__).with_name("quiz_functions.txt")
    quiz_data = read_quiz_data(quiz_file)
    print(quiz_data)



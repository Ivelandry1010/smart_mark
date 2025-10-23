#Read answer sheet
import os

class AnswerSheetHandler:
    def __init__(self):
        self.answer_sheet = None

    def select_answer_sheet(self):
        while True:
            try:
                answer_sheet = input("Please enter the answer sheet file: ")

                # first we check if the file exists
                if not os.path.exists(answer_sheet):
                    raise FileNotFoundError(f"The file at '{answer_sheet}' does not exist.")

                # check if it is not a folder
                if os.path.isdir(answer_sheet):
                    raise IsADirectoryError("Answer sheet can't be a directory")

                # check if the program has permission to read the file
                if not os.access(answer_sheet, os.R_OK):
                    raise PermissionError(f"The program does not have permission to read the file '{answer_sheet}'")
                # all conditions passed
                print("Answer sheet loaded successfully")
                self.answer_sheet = answer_sheet
                break

            except FileNotFoundError as fnf_error:
                print(f"FileNotFoundError: {fnf_error}")
            except IsADirectoryError as dir_error:
                print(f"IsADirectoryError: {dir_error}")
            except PermissionError as perm_error:
                print(f"PermissionError: {perm_error}")
            except Exception as e:
                # Handle any other unexpected exception
                print(f"An unexpected error occurred: {e}")

    def read_answer_sheet(self):
        """Read answer sheet and create a dictionary of correct answers"""
        correct_answers = {}
        answer_sheet_answers = ""
        try:
            with open(self.answer_sheet, "r") as f:
                for line in f:
                    line = line.strip()
                    if ")" not in line:
                        answer_sheet_answers = line
                    if ")" in line:
                        key, value = line.split(")", 1)
                        correct_answers[key] = value
                print(answer_sheet_answers)
                for key, value in correct_answers.items():
                    print(f" {key}){value}")

        except Exception as e:
            print(f"Error while reading the answer sheet: {e}")
        return correct_answers
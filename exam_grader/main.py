import os
from file_selector import FileSelector
from answer_sheet import AnswerSheetHandler
from file_processor import FileProcessor
from csv_handler import CSVHandler
from tabulate import tabulate

class FileReader:
    def __init__(self):
        self.file_selector = FileSelector()
        self.answer_handler = AnswerSheetHandler()
        self.file_processor = FileProcessor()
        self.csv_handler = CSVHandler()
        self.executed_files = []
        self.results = []
        self.correct_answers = {}

    def _validate_match(self, sample_file_path, answer_sheet):
        """Validate if answer sheet keys match student question keys from sample file."""
        try:
            # Extract student_answer keys from sample file
            student_answer = {}
            with open(sample_file_path, "r") as file:
                for line in file:
                    line = line.strip()
                    if ")" in line:
                        key, _ = line.split(")", 1)
                        student_answer[key] = True  # Just need keys

            if not student_answer:
                raise ValueError("No questions found in sample student file.")

            # Read correct answers
            correct_answers = self.answer_handler.read_answer_sheet()

            # Compare sets of keys
            if set(student_answer.keys()) == set(correct_answers.keys()):
                self.correct_answers = correct_answers  # Store for later use
                return True
            else:
                print(f"Mismatch detected: Student questions: {sorted(student_answer.keys())}, Answer sheet: {sorted(correct_answers.keys())}")
                return False
        except Exception as e:
            print(f"Validation error: {e}")
            return False

    def run(self):
        # Select files
        self.file_selector.select_txt_files()
        file_list = self.file_selector.file_list

        if not file_list:
            print("No files to process.")
            return

        # Select and validate answer sheet
        while True:
            self.answer_handler.select_answer_sheet()
            if self._validate_match(file_list[0], self.answer_handler.answer_sheet):
                print("Answer sheet validated successfully.")
                break
            else:
                print("Question/answer sheet mismatch, try uploading the matching sheet...")

        # Select target directory
        self.file_processor.select_target_directory()

        # Process files
        print("\nProcessing files:")
        for file_path in file_list:
            self.file_processor.process_single_file(
                file_path, self.correct_answers, self.file_processor.target_directory
            )
            # Collect results
            self.results.extend(self.file_processor.results)
            self.executed_files.extend(self.file_processor.executed_files)
            # Reset processor lists for next file to avoid duplication
            self.file_processor.executed_files = []
            self.file_processor.results = []

        print(f"\nProcessed and saved files in: {self.file_processor.target_directory}")
        print(f"\nContent of processed files: {self.executed_files}")

        # Display table
        headers = ["No", "Name", "Student ID", "Score"]
        table_data = [
            [index, result["name"], result["student_ID"], result["score"]]
            for index, result in enumerate(sorted(self.results, key=lambda x: x["name"]), start=1)
        ]
        print("\n-------------------------------------------Exam Results---------------------------------------")
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

        # Save CSV
        self.csv_handler.save_as_csv(self.results)

if __name__ == "__main__":
    file_reader = FileReader()
    file_reader.run()
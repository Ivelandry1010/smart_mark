#Process and mark files
import os

class FileProcessor:
    def __init__(self):
        self.target_directory = None
        self.executed_files = []
        self.results = []

    def select_target_directory(self):
        while True:
            try:
                target_directory = input("Enter the target directory to save the modified files: ").strip()
                # Check if the input is empty
                if not target_directory:
                    raise ValueError("The directory path cannot be empty. Please enter a valid path.")

                # Check if the directory is valid
                if not os.path.isdir(target_directory):
                    raise ValueError("Invalid directory. Please try a valid directory")

                # Create the directory if it doesn't exist
                if not os.path.exists(target_directory):
                    os.makedirs(target_directory)
                    print(f"Directory '{target_directory}' created successfully.")

                # Check write permissions
                if not os.access(target_directory, os.W_OK):
                    raise PermissionError(f"You do not have write permissions for '{target_directory}'.")

                self.target_directory = target_directory
                break  # Exit the loop if the directory is valid

            except ValueError as ve:
                print(f"Input Error: {ve}")
            except OSError as oe:
                print(f"OS Error: {oe}")
            except Exception as e:
                print(f"Unexpected Error: {e}")

    def process_single_file(self, file_path, correct_answers, target_directory):
        try:
            # read the file
            with open(file_path, "r") as file:
                student_data = {}
                student_list_of_ans = ""
                student_answer = {}

                for line in file:
                    line = line.strip()
                    if ":" in line:
                        key, value = line.split(":", 1)
                        student_data[key] = value
                    elif ")" in line:
                        key, value = line.split(")", 1)
                        student_answer[key] = value
                    elif ":" not in line and ")" not in line:
                        student_list_of_ans = line

                for key, value in student_data.items():
                    print(f" {key:10}: {value}")
                print()
                print(student_list_of_ans)
                for key, value in student_answer.items():
                    print(f" {key}){value}")
                print()

            student_name = list(student_data.values())[0]
            student_identifier = list(student_data.values())[1]

            file_name = f"{student_name}_{student_identifier}.txt"
            new_file_path = os.path.join(target_directory, file_name)
            total_score = 0

            # compare and write
            with open(new_file_path, "w") as files:
                files.write("\n")
                for key, value in student_data.items():
                    files.write(f" {key:8}: {value}\n")
                correct = 0
                wrong = 0
                files.write(f"\n {student_list_of_ans} \n")
                for key, value in student_answer.items():
                    if value == correct_answers.get(key, ""):
                        files.write(f" {key}) {value} \u2714\n")
                        correct += 1
                    else:
                        files.write(f" {key}) {value} \u274C {correct_answers.get(key, '')}\n")
                        wrong += 1

                total_score = correct
                files.write("  ----------------------------------------------------------------------\n")
                files.write(f" Total Correct: {correct}\n")
                files.write(f" Total Wrong: {wrong}\n")
                files.write(f" You scored: {total_score} in {len(student_answer.keys())}\n")
                percentage = round(total_score / len(student_answer.keys()) * 100)
                files.write(f"{percentage}% - ")
                if percentage < 40:
                    files.write("BAD! You should dedicate more hours to studying this course")
                elif 40 <= percentage < 54:
                    files.write("FAIR! Your performance needs considerable improvement")
                elif 54 <= percentage < 64:
                    files.write("AVERAGE! With consistent effort and focus you can achieve greater success")
                elif 64 <= percentage < 72:
                    files.write("GOOD! Commendable performance, keep practicing to reach higher level of excellence")
                elif 72 <= percentage < 85:
                    files.write("VERY GOOD! Your efforts are paying off. Keep striving for excellence")
                else:
                    files.write("EXCELLENT! You have truly excelled and proven to be the best. Keep up the great work")

                files.write("\n*****************************************************************************")

            self.executed_files.append(file_name)
            self.results.append(
                {
                    "name": student_name,
                    "student_ID": student_identifier,
                    "score": total_score
                }
            )
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")
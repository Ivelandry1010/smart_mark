#Save results as a csv file
import csv
import os

class CSVHandler:
    def __init__(self):
        pass

    def save_as_csv(self, results):
        while True:
            try:
                # Prompt user for the directory to save the file
                exam_result = input("Enter the directory where you want to save the CSV result file: ").strip()

                # Validate the directory
                if not os.path.exists(exam_result):
                    os.makedirs(exam_result)  # Create the directory if it doesn't exist

                # Create the CSV file path
                csv_file_path = os.path.join(exam_result, "student_results.csv")

                # Write the results to a CSV file
                with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    # Write the headers
                    writer.writerow(["No", "Name", "Student ID", "Total Score"])
                    # Write the data
                    for index, result in enumerate(sorted(results, key=lambda x: x["name"]), start=1):  # Sort alphabetically by name
                        writer.writerow([index, result["name"], result["student_ID"], result["score"]])

                print(f"Exam results successfully saved to: {csv_file_path}")
                break

            except Exception as e:
                print(f"An error occurred while saving the file: {e}")
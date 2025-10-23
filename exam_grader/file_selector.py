#Get all text files from a folder
import glob
import os

class FileSelector:
    def __init__(self):
        self.file_list = []

    def select_txt_files(self):
        while True:
            try:
                # Prompt user for folder path
                folder_path = input("Please enter the folder path to the students answers: ")

                # Check if the folder exists
                if not os.path.isdir(folder_path):
                    raise FileNotFoundError(f"The folder at {folder_path} does not exist.")

                # Check if folder is accessible
                if not os.access(folder_path, os.R_OK):
                    raise PermissionError(f"You do not have permission to read from {folder_path}.")

                # Get list of .txt files in the folder
                self.file_list = glob.glob(os.path.join(folder_path, "*.txt"))

                # Check if any .txt files were found
                if not self.file_list:
                    raise FileNotFoundError(f"No .txt files found in the folder {folder_path}.")

                print(f"\nFound the following .txt files:")
                for file in self.file_list:
                    print(file)

                break  

            except (FileNotFoundError, PermissionError) as e:
                print(f"Error: {e}. Please try again.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}. Please try again.")
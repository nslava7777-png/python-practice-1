import os


class FileManager:
    def __init__(self, file):
        self.filename = file

    def check_file(self):
        print("\nChecking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        print(f"Error: {self.filename} not found.")
        return False

    def create_output_folder(self, folder='output'):
        print("\nChecking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")

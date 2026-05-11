import csv

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.students = []

    def load(self):
        with open(self.file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.students = list(reader)

    def preview(self):
        for row in self.students[:5]:
            print(row)
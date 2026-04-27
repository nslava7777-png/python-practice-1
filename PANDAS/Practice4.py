import os
import csv
import json

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

class DataLoader:
    def __init__(self, file):
        self.file = file
        self.students = []

    def load(self):
        print("\nLoading data...")
        try:
            with open(self.file, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.students = list(reader)
            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students
        except FileNotFoundError:
            print(f"Error: File '{self.file}' not found.")
            return None

    def preview(self, n=5):
        print(f"\nFirst {n} rows:")
        print("-" * 30)
        for row in self.students[:n]:
            print(f"{row['student_id']} | {row['age']} | {row['gender']} | {row['country']} | GPA: {row['GPA']}")
        print("-" * 30)

class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.results = {}

    def analyse(self, n=10):
        # Variant D: Top 10 students by exam score
        sorted_students = sorted(self.students, key=lambda x: float(x["final_exam_score"]), reverse=True)
        top_n = sorted_students[:n]

        #
        score_above_95 = list(filter(lambda x: float(x['final_exam_score']) > 95, self.students))
        assign_above_90 = list(filter(lambda x: float(x["assignment_score"]) > 90, self.students))
        gpas = list(map(lambda x: float(x["GPA"]), self.students))
        avg_gpa = sum(gpas) / len(gpas) if gpas else 0

        self.results = {
            "variant": "D",
            "top_students": top_n,
            "statistics": {
                "total_students": len(self.students),
                "avg_gpa": round(avg_gpa, 2),
                "score_above_95": len(score_above_95),
                "assign_above_90": len(assign_above_90)
            }
        }

    def print_results(self):
        print("-" * 30)
        print("Top 10 Students by Exam Score")
        print("-" * 30)
        for i, s in enumerate(self.results['top_students'], 1):
            print(f"{i}. {s['student_id']} | {s['country']} | {s['major']} | Score: {s['final_exam_score']} | GPA: {s['GPA']}")
        
        stats = self.results['statistics']
        print("-" * 30)
        print("Lambda / Map / Filter Statistics")
        print("-" * 30)
        print(f"Students with score > 95: {stats['score_above_95']}")
        print(f"Average GPA of all students: {stats['avg_gpa']}")
        print(f"Students with assignment score > 90: {stats['assign_above_90']}")
        print("-" * 30)

class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)
            print(f"Result saved to {self.output_path}")
        except Exception as e:
            print(f"Save error: {e}")

if __name__ == "__main__":
    FILE_NAME = 'students_data.csv'
    
    fm = FileManager(FILE_NAME)
    if fm.check_file():
        fm.create_output_folder()

        dl = DataLoader(FILE_NAME)
        if dl.load():
            dl.preview()

            analyser = DataAnalyser(dl.students)
            analyser.analyse(n=10)
            analyser.print_results()

            saver = ResultSaver(analyser.results, 'output/result.json')
            saver.save_json()
            
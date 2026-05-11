class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented: use a child class")

    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"

class TopStudentsAnalyser(DataAnalyser): # Твой вариант D
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        # Логика из практики 5
        sorted_s = sorted(self.students, key=lambda x: float(x["final_exam_score"]), reverse=True)
        self.result = {
            "total_students": len(self.students),
            "top_10": sorted_s[:10]
        }

    def print_results(self):
        print("\nTOP STUDENTS ANALYSIS REPORT")
        print("=" * 30)
        super().print_results() # Вызов метода родителя
        print("=" * 30)

    def __str__(self):
        return f"TopStudentsAnalyser: Top 10 Analysis, {len(self.students)} students"
from analytics import FileManager, DataLoader, ResultSaver, Report, TopStudentsAnalyser
from analytics.analyser import DataAnalyser 

def main():
    FILE = 'students_data.csv'
    
    fm = FileManager(FILE)
    if not fm.check_file():
        return
    fm.create_output_folder()

    dl = DataLoader(FILE)
    dl.load()

    # Демонстрация полиморфизма
    analysers = [
        TopStudentsAnalyser(dl.students),
        DataAnalyser(dl.students[:10])
    ]

    print('Running all analysers:')
    for a in analysers:
        print(a)
        a.analyse()
        a.print_results()

    # Работа через класс Report (Ассоциация)
    saver = ResultSaver(analysers[0].result, 'output/result.json')
    report = Report(analysers[0], saver)
    report.generate()

if __name__ == "__main__":
    main()
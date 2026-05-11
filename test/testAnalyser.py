#PS C:\python-practice-1> python -m unittest test/testAnalyser.py -v 
#test_analyse_twice (test.testAnalyser.TestAnalyser.test_analyse_twice) ... ok
#test_result_has_required_keys (test.testAnalyser.TestAnalyser.test_result_has_required_keys) ... ok
#test_result_is_not_empty (test.testAnalyser.TestAnalyser.test_result_is_not_empty) ... ok
#test_total_students (test.testAnalyser.TestAnalyser.test_total_students) ... ok

#----------------------------------------------------------------------
#Ran 4 tests in 0.003s

#OK

import unittest
from analytics.analyser import TopStudentsAnalyser

class TestAnalyser(unittest.TestCase):
    def setUp(self):
        self.sample = [
            {"student_id": "S1", "final_exam_score": "95", "GPA": "3.8"},
            {"student_id": "S2", "final_exam_score": "72", "GPA": "2.5"},
            {"student_id": "S3", "final_exam_score": "98", "GPA": "3.9"},
            {"student_id": "S4", "final_exam_score": "55", "GPA": "1.8"},
            {"student_id": "S5", "final_exam_score": "88", "GPA": "3.5"}
        ]

    def test_result_is_not_empty(self):
        analyser = TopStudentsAnalyser(self.sample)
        analyser.analyse()
        self.assertNotEqual(analyser.result, {})

    def test_total_students(self):
        analyser = TopStudentsAnalyser(self.sample)
        analyser.analyse()
        self.assertEqual(analyser.result["total_students"], 5)

    def test_result_has_required_keys(self):
        analyser = TopStudentsAnalyser(self.sample)
        analyser.analyse()
        self.assertIn("top_10", analyser.result)

    def test_analyse_twice(self):
        analyser = TopStudentsAnalyser(self.sample)
        analyser.analyse()
        res1 = analyser.result.copy()
        analyser.analyse()
        self.assertEqual(analyser.result, res1)

if __name__ == '__main__':
    unittest.main()

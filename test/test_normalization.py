import unittest
from course_selection.normalization import course_normalization

class TestNormalization(unittest.TestCase):

    def test_course_normalization(self):
        d = {'department': 'CS', 'course_number': 111, 'semester': 'Fall', 'year': 2016}
        self.assertDictEqual(course_normalization("CS111 2016 Fall"), d)
        self.assertDictEqual(course_normalization("CS-111 Fall 2016"), d)
        self.assertDictEqual(course_normalization("CS 111 F2016"), d)

if __name__ == "__main__":
    unittest.main()
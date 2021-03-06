'''
Created on July 9, 2015

@author: Kumar Sabyasachi Padhi
Contains unit test cases for kpgroupa module attributes 
mainly corner cases, use and misuse cases
'''
import unittest
import kpgroupa as kp


class TaskTest(unittest.TestCase):
    """
    unit test methods of testing of task attribute of module kp
    """
    def test_type_a(self):
        """ Type of inputs test for count"""
        actual = kp.take([1, 2, 3], 'a')
        expected = []
        self.assertEqual(expected, actual)

    def test_type_b(self):
        """ Type of input test for the list"""
        actual = kp.take((1, 2, 3, 4), 2)
        expected = []
        self.assertEqual(expected, actual)

    def test_type_c(self):
        """ Type of input test for the list elements"""
        actual = kp.take((1, '2', 3, 4), 2)
        expected = []
        self.assertEqual(expected, actual)

    def test_range_a(self):
        """ check for valid range in which count should exist"""
        actual = kp.take([1, 2, 3, 4], -5)
        expected = []
        self.assertEqual(expected, actual)

    def test_range_b(self):
        """ check for valid range in which count should exist"""
        actual = kp.take([1, 2, 3, 4], 10)
        expected = []
        self.assertEqual(expected, actual)

    def test_range_c(self):
        """ check for valid range in which count should exist"""
        actual = kp.take([], 0)
        expected = []
        self.assertEqual(expected, actual)

    def test_usecase(self):
        """ check for valid range in which count should exist"""
        actual = kp.take([5, 7, 3, 4, 10, -2]*10000, 1005)
        inputval = [5, 7, 3, 4, 10, -2]*10000
        expected = inputval[:1005]
        self.assertEqual(expected, actual)


class FlattenTest(unittest.TestCase):
    """
    unit test methods of testing of flatten attribute of module kp
    """
    def test_type_a(self):
        """ Type of inputs test for list"""
        actual = kp.flatten((1, 2, 3))
        expected = []
        self.assertEqual(expected, actual)

    def test_type_b(self):
        """ Type of inputs test for list"""
        actual = kp.flatten([1, [2, 3]])
        expected = []
        self.assertEqual(expected, actual)

    def test_type_c(self):
        """ Type of inputs test for inner list"""
        actual = kp.flatten([[1, 2], '3'])
        expected = []
        self.assertEqual(expected, actual)

    def test_type_d(self):
        """ Type of inputs test for inner list element"""
        actual = kp.flatten([[1, '2'], [3]])
        expected = []
        self.assertEqual(expected, actual)

    def test_dummy(self):
        """ use case and misuse case"""
        actual = kp.flatten([])
        expected = []
        self.assertEqual(expected, actual)

    def test_usecase(self):
        """ use case and misuse case"""
        actual = kp.flatten([[5, 1, 2], [6, 6], [9, 2, 7, 7, 7]])
        expected = [5, 1, 2, 6, 6, 9, 2, 7, 7, 7]
        self.assertEqual(expected, actual)


class IndexerTest(unittest.TestCase):
    """
    unit test methods of testing of indexer attribute of module kp
    """
    def test_type_a(self):
        """ type test case for a text file only input"""
        actual = kp.indexer("misuse.ods")
        expected = {}
        self.assertEqual(expected, actual)

    def test_type_b(self):
        """ type test case for non existing input file"""
        actual = kp.indexer("abc.txt")
        expected = {}
        self.assertEqual(expected, actual)

    def test_usecase(self):
        """ type test case for a working use case"""
        actual = kp.indexer("test.txt")
        expected = {"hello": [1, 2], "world": [1, 3], "universe": [2], "bye": [3]}
        self.assertEqual(expected, actual)


class CompressTest(unittest.TestCase):
    """
    unit test methods of testing of compress attribute of module kp
    """
    def test_type_a(self):
        """ type test case for list"""
        actual = kp.compress((1, 1, 2, 2, 3, 4))
        expected = []
        self.assertEqual(expected, actual)

    def test_type_b(self):
        """ type test case for list elements"""
        actual = kp.compress([1, 1, '2', 2, 3, 4])
        expected = []
        self.assertEqual(expected, actual)

    def test_is_sorted(self):
        """test case for list if not sorted"""
        actual = kp.compress([1, 1, 3, 4, 2, 2, 2])
        expected = []
        self.assertEqual(expected, actual)

    def test_usecase_a(self):
        """test case for corner case"""
        actual = kp.compress([32])
        expected = [(32, 1)]
        self.assertEqual(expected, actual)

    def test_usecase_b(self):
        """test case for corner case"""
        actual = kp.compress([23, 32])
        expected = [(23, 1), (32, 1)]
        self.assertEqual(expected, actual)

    def test_usecase_c(self):
        """test case for use case"""
        actual = kp.compress([3, 4, 4, 4, 7])
        expected = [(3, 1), (4, 3), (7, 1)]
        self.assertEqual(expected, actual)

    def test_usecase_d(self):
        """test case for corner case"""
        actual = kp.compress([3, 3, 3, 3, 5, 5, 8, 9, 9, 9])
        expected = [(3, 4), (5, 2), (8, 1), (9, 3)]
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

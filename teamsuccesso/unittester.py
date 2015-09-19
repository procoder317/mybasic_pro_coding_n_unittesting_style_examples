'''
Created on August 15, 2015

@author: Kumar Sabyasachi Padhi

Contains unit test cases for parceldelivery.py module attributes
consists of : corner cases, use and misuse cases
for some of the helper functions for toppostalcodes() attribute of
parceldelivery.py module
'''

import unittest
import parceldelivery as psd


class RanksetterTest(unittest.TestCase):
    """
    unit test methods of testing of "ranksetter()" attribute of module psd
    """
    def test_sortedranklist(self):
        """
        Type of inputs test for if input rank list is not sorted then output
        results in a unsorted
        MIS-USE CASE and use case
        """
        #misuse case
        actual = psd.ranksetter([('456098', 2), ('567789', 3),
                                ('560089', 1)], 5, "234561")
        expected = None
        self.assertEqual(expected, actual, "unsorted rank list as input")
        #use case
        actual = psd.ranksetter([('456098', 4), ('567789', 3),
                                ('560089', 2)], 5, "234561")
        expected = [('234561', 5), ('456098', 4), ('567789', 3)]
        self.assertEqual(expected, actual, "sorted rank list as input")

    def test_parameters(self):
        """
        test input parameter values lengths and types misuses
        """
        expected = None
        #type tests
        actual = psd.ranksetter((('456098', 4), ('567789', 3),
                                ('560089', 2)), 5, '234561')
        self.assertEqual(expected, actual, "rank list is of tuple type")
        actual = psd.ranksetter([('456098', 4), ('567789', 3),
                                ('560089', 2)], '5', '234561')
        self.assertEqual(expected, actual, "no_delivery is of type string")
        actual = psd.ranksetter([('456098', 4), ('567789', 3),
                                ('560089', 2)], 5, 234561)
        self.assertEqual(expected, actual, "postal code is of type integer")
        actual = psd.ranksetter([('456098', 4), ('567789', 3),
                                ('560089', 2)], 5, '23456a')
        self.assertEqual(expected, actual,
                         "postal code is not a string of type digit")
        #length tests
        actual = psd.ranksetter([('456098', 4), ('567789', 3),
                                ('560089', 2)], 5, '2345617')
        self.assertEqual(expected, actual, "postal code is more than 6 digits")
        actual = psd.ranksetter([('456098', 4), ('567789', 3)], 5, '234561')
        self.assertEqual(expected, actual, "rank list length is less than 3")
        #parameters value tests there can be even few more tests
        actual = psd.ranksetter([('456098', 4), ('567789', 3),
                                ('560089', 2)], -5, '234561')
        self.assertEqual(expected, actual, "no_delivery is < 0")


class WriteoutfileTest(unittest.TestCase):
    """
    unit test methods of testing of "write_outfile()" attribute of module psd
    """
    def test_generics(self):
        """
        test the general input and output types and IO tests
        """
        actual = psd.write_outfile((('456098', 4), ('567789', 3),
                                    ('560089', 2)))
        expected = "type mismatch"
        self.assertEquals(expected, actual, "type of rank list is a tuple")
        actual = psd.write_outfile([('456098', 4), ('567789', 3),
                                    ('560089', 2)], 'myout.csv')
        self.assertEquals(expected, actual, "type of file is *.csv")
        actual = psd.write_outfile([('456098', 4), ('567789', 3),
                                    ('560089', 2)], '')
        self.assertEquals(expected, actual, "empty file type passed")
        #use case
        actual = psd.write_outfile([('456098', 4), ('567789', 3),
                                    ('560089', 2)])
        self.assertEquals(None, actual, "correct usage")


class MatcherandextractorTest(unittest.TestCase):
    """
    all kinds of assertions are used here in the matcher_and_extractor()
    attribute of psd module. So I am not adding any tests as the assertions are
    sufficient for time being.
    """
    pass


if __name__ == "__main__":
    unittest.main()

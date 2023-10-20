import unittest
import problem1

class Problem1(unittest.TestCase):
    
    def test_number_of_matches_per_year(self):
        self.assertEqual(
            problem1.number_of_matches_per_year(),
            {'2008': 5, '2009': 5, '2010': 5, '2011': 5, '2012': 5, '2013': 5, '2014': 5, '2015': 5, '2016': 5, '2017': 5}
        )

if __name__ == '__main__':
    unittest.main()
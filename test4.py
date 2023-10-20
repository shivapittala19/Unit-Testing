import unittest
import problem4

class Problem4(unittest.TestCase):
    
    def test_top_economical_bowlers(self):
        self.assertEqual(
            problem4.top_economical_bowlers(),
            {
                'Bhuvneshwar Kumar': 6.0,
                'Harshal Patel': 6.0, 
                'Stuart Binny': 6.0, 
                'Pravin Tambe': 6.0, 
                'Umesh Yadav': 6.0
            }
        )

if __name__ == '__main__':
    unittest.main()
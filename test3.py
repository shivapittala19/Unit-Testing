import unittest,problem3

class Problem3(unittest.TestCase):
    
    def test_extra_runs_conceded_by_team(self):
        self.assertEqual(
            problem3.extra_runs_conceded_by_team(),
            {
                'Mumbai Indians': 1,
                'Rajasthan Royals': 1, 
                'Kolkata Knight Riders': 0,
                 'Kings XI Punjab': 1, 
                 'Royal Challengers Bangalore': 3, 
                 'Delhi Daredevils': 1}
        )

if __name__ == '__main__':
    unittest.main()
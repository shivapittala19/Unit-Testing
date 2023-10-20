import unittest 
import problem2

class Problem2(unittest.TestCase):
    
    def test_number_of_wins_by_team_in_each_season(self):
        self.assertEqual(
            problem2.number_of_wins_by_team_in_each_season(),
            {
                'Chennai Super Kings': [1, 1, 1, 2, 1, 1, 1, 1, 0, 1], 
                'Kings XI Punjab': [1, 1, 0, 0, 0, 1, 1, 1, 0, 1], 
                'Delhi Daredevils': [1, 1, 1, 0, 0, 1, 1, 1, 1, 1], 
                'Deccan Chargers': [1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
                'Rajasthan Royals': [1, 1, 1, 0, 1, 1, 1, 1, 1, 0], 
                'Royal Challengers Bangalore': [0, 1, 0, 0, 1, 0, 0, 1, 1, 1], 
                'Mumbai Indians': [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                'Kolkata Knight Riders': [0, 0, 1, 1, 1, 1, 1, 0, 1, 1], 
                'Sunrisers Hyderabad': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]}
        )

if __name__ == '__main__':
    unittest.main()
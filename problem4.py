from main import deliveries, matches

def top_economical_bowlers():
    season_id = {}
    for row in matches:
        if row['season'] == '2015' and row['id'] not in season_id:
            season_id[row['id']] = 1
    
    bowler_dict = {} 
    dict
    # {
    #     'bowler':['total_runs_conceded':'total_balls']
    # }
    for row in deliveries:
        if row['match_id'] in season_id:
            # ignoring wide balls and no_balls in the count of number of balls and adding the runs to the total runs conceded by a bowler
            bowler, runs  = row['bowler'], int(row['total_runs'])
            if row['wide_runs'] == '0' and row['noball_runs'] == '0':
                if bowler in bowler_dict:
                    bowler_dict[bowler][0] += runs
                    bowler_dict[bowler][1] += 1
                else:
                    bowler_dict[bowler] = [runs,1]
            else:
                if bowler in bowler_dict:
                    bowler_dict[bowler][0] += runs
                else:
                    bowler_dict[bowler] = [runs,0]
                
   
    for bowler in bowler_dict:
        bowler_dict[bowler] = round((bowler_dict[bowler][0] / bowler_dict[bowler][1]) * 6,2)
    
    top_five_bowlers = dict(sorted(bowler_dict.items(),key=lambda x: x[1])[:5])
    return top_five_bowlers




from main import matches

def number_of_wins_by_team_in_each_season():
    wins_by_team_and_season = {}

    for row in matches:
        season = row['season']
        winner = row['winner']
        if season in wins_by_team_and_season:
            if winner in wins_by_team_and_season[season]:
                wins_by_team_and_season[season][winner] += 1
            else:
                wins_by_team_and_season[season][winner] = 1
        else:
            wins_by_team_and_season[season] = {winner : 1}
            
    sorted_wins_by_season = dict(sorted(wins_by_team_and_season.items(),key=lambda x : x[0]))
    
    list_teams = []
    for season_data in sorted_wins_by_season.values():
        for team in season_data.keys():
            if team not in list_teams:
                list_teams.append(team)
        
    team_wins = {team: [year_data.get(team, 0) for year_data in sorted_wins_by_season.values()] for team in list_teams}

    return team_wins
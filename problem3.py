from main import deliveries, matches

def extra_runs_conceded_by_team():
    season_id = {}
    # retriving all id's of matches played in 2016
    for row in matches:
        if row['season'] == '2016' and row['id'] not in season_id:
            season_id[row['id']] = 1
      
    extra_runs_dict = {}
    # dict keys->bowling_team values->extra runs conceded
    for row in deliveries:
        if row['match_id'] in season_id:
            bowling_team, extra_runs = row['bowling_team'], int(row['extra_runs'])
            try:
                extra_runs_dict[bowling_team] += extra_runs
            except:
                extra_runs_dict[bowling_team] = extra_runs
    return extra_runs_dict


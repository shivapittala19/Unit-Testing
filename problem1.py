from main import matches

def number_of_matches_per_year():
    match_dict = {}
    # creating a dict with keys-> season and value -> number of matches played in that season
    for row in matches:
        try:
            match_dict[row['season']] += 1
        except:
            match_dict[row['season']] = 1
    sorted_match_dict = dict(sorted(match_dict.items(),key=lambda x: x[0]))
    return sorted_match_dict


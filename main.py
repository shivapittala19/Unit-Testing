import csv

#function to read the csv file 
def load_csv(file_name):
    file = open(file_name,'r')
    lines = csv.DictReader(file)
    
    return lines

#Reading the csv files
matches  = load_csv('mock_matches.csv')
deliveries = load_csv('mock_deliveries.csv')
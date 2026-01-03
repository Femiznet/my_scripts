import csv

census_path = input("Enter file path:")

try:
    census = open(census_path, encoding="utf-8").readlines()
except FileNotFoundError as e:
    print(e); exit()

field = input("Field columns separated by commas:").split(",")

with open("census.csv", "w", encoding="utf-8") as file:
    csv_file = csv.DictWriter(file, field); csv_file.writeheader()
    
    n = 0
    for lines in census:
        line = lines.split()

        if len(line) != len(field):
            n+=1; continue

        contact = {field[col]:line[col] for col in range(len(field))}
        csv_file.writerow(contact) 
            
    if n > 0:
        print("{0} lines were skipped due to unequal column lengths".format(n))





import csv

with open('dados.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['nome'], row['valor'])

print(row)
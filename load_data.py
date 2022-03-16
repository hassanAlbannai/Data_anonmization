import csv

dataset = []

with open('ipums.txt') as data:
    reader = csv.reader(data, delimiter='\t')
    for row in reader:
        dataset.append(row)

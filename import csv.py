import csv

with open('data_sewa.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

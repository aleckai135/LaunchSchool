import csv

with open('usageReport_1_b1f895ffa811415abe25ae768548e9c0.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines)

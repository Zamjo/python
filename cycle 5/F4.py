import csv
with open('xl.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 print("First_name Email ")
 print("---------------------------------")
 for row in data:
   print(row['First name'],'      ', row['Email'])
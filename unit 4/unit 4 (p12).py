import csv

row_count = 0

with open("Data2.csv","r") as f:
    z = csv.reader(f) 
    for row in z:
        row_count += 1 
    print(row_count)
    print(row)

with open("Data2.csv","w") as f:
    w = csv.writer(f)
    w.writerow(["\n Hello World "]) 


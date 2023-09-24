import csv
with open('places.csv','r',encoding='utf-8') as file:
    reader=csv.reader(file)

    header=next(reader)

    locations=set()
    for row in reader:
        if row[1]=="Not Found" or row[2]=="Not Found":
                locations.add(row[0][4:])

with open('notfound.csv','w',newline='',encoding='utf=8') as file:
     writer=csv.writer(file)
     for location in locations:
          writer.writerow([location])
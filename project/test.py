import csv


#Creating the 39 categories

categories = []
for i in range(40) :
    categories.append([])
print(categories)

#File reading and putting data in categories

with open('census-income-data.data', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        for elements in row:
            for i in range(40):
                 #print' '.join(row)
                 categories[i].append(elements)
                 break
            print(categories)
            









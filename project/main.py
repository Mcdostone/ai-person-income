import csv
from sklearn import tree

indice = 0
#Creating the 41 categories
categories = []
for i in range(42) :
    categories.append([])


#File reading and putting data in categories 

with open('census-income-data.data', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        for elements in row:
            #print' '.join(row)  
            categories[indice].append(elements)  
            indice+= 1
            if indice == 42 :
                indice = 0
           # print(categories)  category #41 is useless
            
#Tree creation

#X = [categories]
#Y = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41]
#clf = tree.DecisionTreeClassifier()
#clf = clf.fit(X,Y)

#Does not count strings in categories as viable variables -> everuthing is string
#Need for one-hot-encoding (changing strings wit) 

#...Or we could use https://pypi.python.org/pypi/DecisionTree/3.4.3


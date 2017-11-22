import csv


#Creating the 41 categories

categories = []
for i in range(42) :
    categories.append([])
print(categories)
indice = 0

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
            print(categories[0]) #return age, catgeory #41 is useless
            




#Voir pour le decision tree http://scikit-learn.org/stable/modules/tree.html
#Voir aussi si le prof accepte qu'on utilise ce genre de chose ou veut qu'on code tout ?




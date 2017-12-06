from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn import linear_model
from sklearn.svm import LinearSVC
from sklearn import preprocessing as pp
import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("census-income-data.data", skipinitialspace=True, usecols=list(range(0, 41)))
data = data.fillna('Missing value')#.apply(pp.LabelEncoder().fit_transform)

target = pd.read_csv("census-income-data.data", skipinitialspace=True, usecols=[41])

dataTest = pd.read_csv("census-income-test.test", skipinitialspace=True, usecols=list(range(0, 41)))
dataTest = dataTest.fillna('Missing value').apply(pp.LabelEncoder().fit_transform)

targetTest = pd.read_csv("census-income-test.test", skipinitialspace=True, usecols=[41])

'''
clfG = GaussianNB()
clfM = MultinomialNB()
clfB = BernoulliNB()
clfG.fit(data, target.target)
clfM.fit(data, target.target)
clfB.fit(data, target.target)
#result = clf.predict(data)
scoreG = clfG.score(data, target.target)
scoreM = clfM.score(data, target.target)
scoreB = clfB.score(data, target.target)

print("Taux d'erreur GaussianNB : %.1f" % ((1 - scoreG) * 100) + '%')
print("Taux d'erreur MultinomialNB : %.1f" % ((1 - scoreM) * 100) + '%')
print("Taux d'erreur BernoulliNB : %.1f" % ((1 - scoreB) * 100) + '%')
'''

'''
clfSGD = linear_model.SGDClassifier()
clfSGD.fit(data, target.target)
scoreSGD = clfSGD.score(data, target.target)
print("Taux d'erreur SGDClassifier : %.1f" % ((1 - scoreSGD) * 100) + '%')
'''

'''
clfSVC = LinearSVC(random_state=0)
clfSVC = clfSVC.fit(data, target.target)
scoreSVC = clfSVC.score(dataTest, targetTest.target)
print(clfSVC.coef_)
print("Taux d'erreur LinearSVC : %.1f" % ((1 - scoreSVC) * 100) + '%')
tree.export_graphviz(clfSVC, out_file='tree.dot')
'''

clfTree = DecisionTreeClassifier(random_state=0, max_depth=5)
clfTree = clfTree.fit(data, target.target)
scoreTree = clfTree.score(dataTest, targetTest.target)
print("Taux d'erreur DecisionTreeClassifier : %.1f" % ((1 - scoreTree) * 100) + '%')
tree.export_graphviz(clfTree, out_file='tree.dot')

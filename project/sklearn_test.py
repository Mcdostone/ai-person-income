from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn import preprocessing as pp
import pandas as pd

data = pd.read_csv("census-income-data.data", skipinitialspace=True, usecols=list(range(0, 41)))
data = data.fillna('Missing value').apply(pp.LabelEncoder().fit_transform)

target = pd.read_csv("census-income-data.data", skipinitialspace=True, usecols=[41])

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

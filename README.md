# ai-person-income

En 1995 le Bureau de Recensement des Etats-Unis lance une enquête sur la situation
démographique et sociale des adultes Américains et leur niveau de rémunération annuel.
Les analyses statistiques d’il y a vingt ans montrent une corrélation entre ces facteurs.
Aujourd’hui, les techniques d’apprentissage automatique et statistique devraient nous
permettre de gagner plus d’information à partir de ces donnees brutes.


## Our work

Le but du projet est de concevoir est entrainer un arbre de d´ecision pour classer le
niveau de rémunération des adultes Américains. Celui-ci dépend de plusieurs variables
démographiques et sociales.
Le choix de la plate-forme de développement et du langage de programmation est libre


## Installation

We decided to develop our solution thanks to pythons programming language. First of all, check if you have python installed on your machine. We will maybe need some python packages, so pip is also needed. We work with **Python3.6** and **Pip3** ! 
    
    
``` bash
    python --version
    # Python 3.6.3
    pip --version
    # pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)
```

**If you install Python3.6 and pip3, python2.6 and pip are kept. In this case,
you have to use python3 and pip3 in your shell.**

``` bash
    python3 --version
    pip3 --version
```

Install all dependancies and start working:
``` bash
    pip install -r requirements.txt
```


## Execution
``` bash
    python main.py -f census-income-data.data
```


## authors

  - [@Sqrtcc](), Claire Crapanzano
  - [@Minious](https://github.com/minious), Eliot Godard
  - [@Mcdostone](https://github.com/Mcdostone), Yann Prono

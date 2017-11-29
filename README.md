# ai-person-income

En 1995 le Bureau de Recensement des Etats-Unis lance une enquête sur la situation
démographique et sociale des adultes Américains et leur niveau de rémunération annuel.
Les analyses statistiques d’il y a vingt ans montrent une corrélation entre ces facteurs.
Aujourd’hui, les techniques d’apprentissage automatique et statistique devraient nous
permettre de gagner plus d’information à partir de ces donnees brutes.


## Our work

Le but du projet est de concevoir est entrainer un arbre de décision pour classer le
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

**If you install Python3.6 and pip3, python2.6 and pip are kept. In this case, you have to use python3 and pip3 in your shell.** 

``` bash
    python3 --version
    pip3 --version
```

If you have some trouble to switch between these 2 versions, juste create aliases:


``` bash
    # ~/.bash_aliases
    alias python='python3'
    alias pip='pip3'
    # Save and restart your terminal to apply new aliases
```

Install all dependancies and start working:
``` bash
    pip install -r requirements.txt
```


## Execution
``` bash
    # If you want to work a subset of data
    python project/main.py -f project/census-income-sample.data # or make
    python project/main.py -f project/census-income-data.data # or make run -full    
```


## About the data

Extract of the first line of the *`census-income-data.data`*

| Index   | Example of value                             | Description                                  | To ignore |
|:-------:|:---------------------------------------------|:---------------------------------------------|:----------|
|    0    |   73                                         |   age                                        |           |
|    1    |   Not in universe                            |   class of worker                            |           |
|    2    |   0                                          |   detailed industry recode                   |           |
|    3    |   0                                          |   detailed occupation recode                 |           |
|    4    |   High school graduate                       |   education                                  |           |
|    5    |   0                                          |   wage per hour                              |           |
|    6    |   Not in universe                            |   enroll in edu inst last wk                 |           |
|    7    |   Widowed                                    |   marital stat                               |           |
|    8    |   Not in universe or children                |   major industry code                        |           |
|    9    |   Not in universe                            |   major occupation code                      |           |
|   10    |   White                                      |   race                                       |           |
|   11    |   All other                                  |   hispanic origin                            |           |
|   12    |   Female                                     |   sex                                        |           |
|   13    |   Not in universe                            |   member of a labor union                    |           |
|   14    |   Not in universe                            |   reason for unemployment                    |           |
|   15    |   Not in labor force                         |   full or part time employment stat          |           |
|   16    |   0                                          |   capital gains                              |           |
|   17    |   0                                          |   capital losses                             |           |
|   18    |   0                                          |   dividends from stocks                      |           |
|   19    |   Nonfiler                                   |   tax filer stat                             |           |
|   20    |   Not in universe                            |   region of previous residence               |           |
|   21    |   Not in universe                            |   state of previous residence                |           |
|   22    |   Other Rel 18+ ever marr not in subfamily   |   detailed household and family stat         |           |
|   23    |   Other relative of householder              |   detailed household summary in household    |           |
|   *24*  |   *1700.09*                                  |   *instance weight*                            | **True**  |
|   *25*  |   *?*                                        |   *instance weight*                            | **True**  |
|   26    |   ?                                          |   migration code-change in msa               |           |
|   27    |   ?                                          |   migration code-change in reg               |           |
|   28    |   Not in universe under 1 year old           |   migration code-move within reg             |           |
|   29    |   ?                                          |   live in this house 1 year ago              |           |
|   30    |   0                                          |   migration prev res in sunbelt              |           |
|   31    |   Not in universe                            |   num persons worked for employer            |           |
|   32    |   United-States                              |   family members under 18                    |           |
|   33    |   United-States                              |   country of birth father                    |           |
|   34    |   United-States                              |   country of birth mother                    |           |
|   35    |   Native- Born in the United States          |   country of birth self                      |           |
|   36    |   0                                          |   citizenship                                |           |
|   37    |   Not in universe                            |   own business or self employed              |           |
|   38    |   2                                          |   fill inc questionnaire for veteran's admin |           |
|   39    |   0                                          |   veterans benefits                          |           |
|   40    |   95                                         |   weeks worked in year                       |           |
|   41    |   - 50000                                    |   year                                       |           |

The value to determine is the last one. There are 2 possibles values:
 - -50000
 - 50000+


## authors

  - [@Sqrtcc](https://github.com/sqrtcc)Claire Crapanzano
  - [@Minious](https://github.com/minious), Eliot Godard
  - [@Mcdostone](https://github.com/Mcdostone), Yann Prono

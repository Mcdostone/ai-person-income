"""
    Main script of our IA algorithm,
    developed by Claire Crapanzano, Eliot Godard, Yann Prono
"""
import os
import sys
import getopt
import logging
import argparse
import csv
import coloredlogs
from sklearn import tree
import graphviz
import pandas
from sklearn.datasets import load_iris

# Setup logger
LOGGER = logging.getLogger(__name__)
coloredlogs.install(logger=LOGGER, fmt='%(asctime)s %(name)s %(levelname)s %(message)s')


def import_data_file(filename):
    if os.path.exists(filename):
        return pandas.read_csv(filename, delimiter=',', skipinitialspace=True)
    else:
        raise Exception(f'Cannot find {filename}')


def read_data_file(filename):
    """
    Read the CSV file and prepare the data to make the decision tree.
    """
    categories = []
    for i in range(42):
        categories.append([])
    indice = 0
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', encoding='us-ascii')
        for row in reader:
            for elements in row:
                categories[indice].append(elements)
                indice += 1
                if indice == 42:
                    indice = 0


def main(argv):
    """ Main function, fetch the filename of data file and process the tree decision algorithm.
        :param argv: args passed by the shell
    """
    datafile = ''
    try:
        opts, _ = getopt.getopt(argv, 'f:', ['file='])
        if len(opts) == 0:
            print_help()
            sys.exit(1)
    except getopt.GetoptError:
        print_help()
        sys.exit(1)

    for opt, arg in opts:
        if opt == '-h':
            print_help()
        if opt in ('-f', '--file'):
            datafile = arg
        LOGGER.info(f'Reading the datafile {datafile}')
        df = import_data_file(datafile)
        print('Income types:', df["INCOME"].unique(), sep="\n")
        LOGGER.info(f'Datafile {datafile} read with success')

def print_help():
    """
    Print some help for the user
    """
    parser = argparse.ArgumentParser(
        description='''Run the algorithm to create the decision tree. ''',
        epilog=f'You can follow this example: python {__file__} -f census-income-data.data'
    )
    parser.add_argument('-f', '--file', type=str, nargs=1, help='data file to use to build the decision tree', required=True)
    parser.parse_args()



if __name__ == "__main__":
    main(sys.argv[1:])

#X = [categories]
#Y = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41]
#clf = tree.DecisionTreeClassifier()
#clf = clf.fit(X,Y)

#Does not count strings in categories as viable variables -> everuthing is string
#Need for one-hot-encoding (changing strings wit) 

#...Or we could use https://pypi.python.org/pypi/DecisionTree/3.4.3


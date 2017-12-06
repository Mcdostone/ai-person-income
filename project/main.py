"""
    Main script of our IA algorithm,
    developed by Claire Crapanzano, Eliot Godard, Yann Prono
"""
from sklearn.datasets import load_iris
import os
import sys
import getopt
import logging
import argparse
import csv
from sklearn.externals.six import StringIO
import numpy as np
import coloredlogs
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.preprocessing import LabelEncoder
import graphviz
import pandas

# Setup logger
LOGGER = logging.getLogger(__name__)
coloredlogs.install(logger=LOGGER, fmt='%(asctime)s %(name)s %(levelname)s %(message)s')


def import_data_file(filename):
    if os.path.exists(filename):
        return pandas.read_csv(filename, delimiter=',', skipinitialspace=True)
    else:
        raise Exception(f'Cannot find {filename}')

def normalize_target(df, column='target'):
    df[column] = df[column].replace('- 50000.', -1)
    df[column] = df[column].replace('50000+.', 1)
    return df

def save_to_svg(classifier, categories, classes):
    dot_data = tree.export_graphviz(
        classifier,
        out_file=None,  
        feature_names=categories,
        class_names=classes,  
        filled=True,
        rounded=True,  
        special_characters=True
    )
    graph = graphviz.Source(dot_data) 
    graph.render('income') 
    #graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    #SVG(graph.create(format='svg'))


def make_decision_tree(filename, target_column = 'target'):
    LOGGER.info(f'Reading the datafile {filename}')
    df = import_data_file(filename)                
    
    ###################################
    ### GET INFORMATION ABOUT DATA ####
    ###################################
    LOGGER.info(f'Data are loaded into memory: {df.shape[0]} x {df.shape[1]} table') 
    categories = list(df.columns.values)
    categories.remove(target_column)
    
    ##################################
    ### TRANSFORM STRING INTO INT ####
    ##################################
    for col in categories:
        df[col] = pandas.factorize(df[col])[0]
    
    #################################
    ### FORMAT OUR TARGET VALUE  ####
    #################################
    df = normalize_target(df)
    classifier = DecisionTreeClassifier(max_depth=4)
    
    ################################
    ### BUILD THE TREE DECISION ####
    ################################
    classifier = classifier.fit(df[categories], df[target_column])
    
    ################################
    ### SAVE FOR VISUAL RESULTS ####
    ################################
    save_to_svg(classifier, np.array(categories), ['Poor', 'Rich'])


def main(argv):
    """ Main function, fetch the filename of data file and process the tree decision algorithm.
        :param argv: args passed by the shell
    """
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
            make_decision_tree(arg)

        
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
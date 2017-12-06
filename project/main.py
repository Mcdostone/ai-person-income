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
from encoder import Encoder
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


class DecisionTreeBuilder:
    
    def __init__(self, dataframe, target):
        self.df = dataframe
        self.categories = list(dataframe.columns.values)
        self.target = target
        self.categories.remove(self.target)

    def save_to_pdf(self, filename, classifier, classes):
        filename = filename.replace('.pdf', '')
        dot_data = tree.export_graphviz(
            classifier,
            out_file=None,  
            feature_names=np.array(self.categories),
            class_names=classes,  
            filled=True,
            rounded=True,  
            special_characters=True
        )
        graph = graphviz.Source(dot_data) 
        graph.render(filename) 

    def encode(self):
        encoder = Encoder(self.df)
        self.df = encoder.encode() 
        self.normalize_target()

    def get_data(self):
        return self.df[self.categories]
    
    def get_target(self):
        return self.df[self.target]

    def normalize_target(self):
        self.df[self.target] = self.df[self.target].replace('- 50000.', -1)
        self.df[self.target] = self.df[self.target].replace('50000+.', 1)
        return self.df
    
    def export_current_df(self, filename):
        self.df.to_csv(filename, index=False)
    
    def print_dataframe(self):
        print(self.df.head())



######################
#### Util methods ####
######################
def import_data_file(filename):
    if os.path.exists(filename):
        return pandas.read_csv(filename, delimiter=',', skipinitialspace=True)
    else:
        raise Exception(f'Cannot find {filename}')
 

def main(argv):
    """ Main function, fetch the filename of data file and process the tree decision algorithm.
        :param argv: args passed by the shell
    """
    datafile = ''
    testfile = ''
    exportfile = ''
    savefile = None
    try:
        opts, _ = getopt.getopt(argv, 'f:t:s:e:', ['file=', 'test=', 'save=', 'export='])
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
        if opt in ('-t', '--test'):
            testfile = arg
        if opt in ('-s', '--save'):
            savefile = arg
        if opt in ('-e', '--export'):
            exportfile = arg

    if len(opts) >= 2:
        df = import_data_file(datafile)
        builderData = DecisionTreeBuilder(df, 'target') 
        LOGGER.info(f'Data are loaded into memory: {df.shape[0]} x {df.shape[1]} table') 

        
        ################################
        ### BUILD THE TREE DECISION ####
        ################################
        #builderData.encode()
        builderData.encode()

        if exportfile:
            LOGGER.info(f'Export the encoded dataframe into {exportfile}')
            builderData.export_current_df(exportfile)

        clf = DecisionTreeClassifier(max_depth=4)
        clf = clf.fit(builderData.get_data(), builderData.get_target())
        ################################
        ### SAVE FOR VISUAL RESULTS ####
        ################################

        if savefile:
            LOGGER.info(f'Save tree decision into {savefile}') 
            builderData.save_to_pdf(savefile, clf, ['Poor', 'Rich'])
        
        dfTest = import_data_file(testfile)
        builderTest = DecisionTreeBuilder(df, 'target') 
        scoreTree = clf.score(builderTest.get_data(), builderTest.get_target())
        print("Taux d'erreur: %.1f" % ((1 - scoreTree) * 100) + '%')
    else:
        print_help()

        
def print_help():
    """
    Print some help for the user
    """
    parser = argparse.ArgumentParser(
        description='''Run the algorithm to create the decision tree. ''',
        epilog=f'You can follow this example: python {__file__} -f census-income-data.data'
    )
    parser.add_argument('-f', '--file', type=str, nargs=1, help='data file to use to build the decision tree', required=True)
    parser.add_argument('-t', '--test', type=str, nargs=1, help='test file to use for the evaluation of the decision tree', required=True)
    parser.add_argument('-s', '--save', type=str, nargs=1, help='Save the decision tree in a PDF file')
    parser.add_argument('-e', '--export', type=str, nargs=1, help='Export the encoded file')
    parser.parse_args()


if __name__ == "__main__":
    main(sys.argv[1:])
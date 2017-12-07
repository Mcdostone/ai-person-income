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
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import math

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
    
    def get_categories(self):
        return self.categories

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

        class_weight = {0: 1, 1: 100}
        
        clf = DecisionTreeClassifier(random_state=0, max_depth=7, class_weight='balanced')
        clf = clf.fit(builderData.get_data(), builderData.get_target())
        features_importances = list(zip(builderData.get_categories(), ((math.ceil(x * 10000) / 100) for x in clf.feature_importances_)))
        sorted_features_importances = sorted(features_importances, key=lambda x: x[1], reverse=True)
        for i in sorted_features_importances:
            print(i)
        
        ################################
        ### SAVE FOR VISUAL RESULTS ####
        ################################

        if savefile:
            LOGGER.info(f'Save tree decision into {savefile}') 
            builderData.save_to_pdf(savefile, clf, ['Poor', 'Rich'])
        
        dfTest = import_data_file(testfile)
        builderTest = DecisionTreeBuilder(dfTest, 'target') 
        builderTest.encode()
        scoreTree = clf.score(builderTest.get_data(), builderTest.get_target())
        print("Taux d'erreur: %.1f" % ((1 - scoreTree) * 100) + '%')
        
        y_true = builderTest.get_target()
        y_pred = clf.predict(builderTest.get_data())
        conf = confusion_matrix(y_true, y_pred)
        #print(conf)
        sns.heatmap(conf, square=True, annot=True, fmt='g', cbar=False, xticklabels=['-50000', '+50000'], yticklabels=['-50000', '+50000'])
        plt.xlabel('valeurs prédites')
        plt.ylabel('valeurs réelles')

        average_precision_poor = precision_score(y_true, y_pred, pos_label=0)
        average_precision_rich = precision_score(y_true, y_pred, pos_label=1)
        average_recall_poor = recall_score(y_true, y_pred, pos_label=0)
        average_recall_rich = recall_score(y_true, y_pred, pos_label=1)
        print('-50000 precision score: {0:0.2f}'.format(average_precision_poor))
        print('+50000 precision score: {0:0.2f}'.format(average_precision_rich))
        print('-50000 recall score: {0:0.2f}'.format(average_recall_poor))
        print('+50000 recall score: {0:0.2f}'.format(average_recall_rich))
        
        plt.show()
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

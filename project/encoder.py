from pandas.api.types import is_numeric_dtype
import pandas
import logging
import operator
import coloredlogs

LOGGER = logging.getLogger(__name__)
coloredlogs.install(logger=LOGGER, fmt='%(asctime)s %(name)s %(levelname)s %(message)s')


class Encoder:

    def __init__(self, df):
        self.df = df

    def encode(self):
        categories = list(self.df.columns.values)
        LOGGER.info('Following categories will be not encoded because these data are numeric:')
        numeric_categories = [col for col in categories if is_numeric_dtype(self.df[col])]
        for col in numeric_categories:
            if is_numeric_dtype(self.df[col]):
                print(f'\t - {col}')
        LOGGER.info('Other categories will be encoded!')

        for col in list(self.df.columns.values):
            if not is_numeric_dtype(self.df[col]):
                self.df[col] = pandas.factorize(self.df[col])[0]

        return self.df
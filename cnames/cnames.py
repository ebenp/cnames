'''
cnames module containing one function to autocomplete column names in a pandas DataFrame in IPython
modified from the following answer for DataFrame class monkey patching
https://stackoverflow.com/a/25418058

written 11/17/18 by Eben Pendleton
'''
from collections import namedtuple

def cnames(self):
    list_of_names = self.columns.values
    list_of_names_dict = {x:x for x in list_of_names}

    varnames = namedtuple('varnames', list_of_names)
    return varnames(**list_of_names_dict)


# tester
if __name__ == "__main__":
    import pandas as pd
    import numpy as np

    # monkey-patch the DataFrame class
    pd.DataFrame.cnames = cnames

    df = pd.DataFrame({'variable_1': np.arange(5), 'variable_2': np.arange(5)})
    print('done')




"""
This script provides utility functions that support
input/output, parsing of the data used in the assignment.
"""
import simplejson as js

def clean_string(string):
    """
    Turn to lower case, remove non-alphanumerics
    """
    return re.sub(r'\W+', ' ', string).lower()

def load_jsonl(inputfile):
    """
    This function loads a jsonl file.
    """
    D = []
    with open(inputfile) as f:
        for line in f.readlines():
            D.append(js.loads(line))
    return D

def get_date(datetime):
    """
    Get the date part of a datetime in the format
    of "DD-MM-YYYYThh:mm:ssZ".
    """
    return datetime.split('T')[0] 

def load_txt(inputfile):
    """
    This function loads a text file. 
    """
    T = ''
    with open(inputfile) as f:
        T = f.read()
    return T

if __name__ == '__main__':
    import doctest
    doctest.testmode()


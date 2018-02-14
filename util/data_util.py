"""
This script provides utility functions that support
input/output, parsing of the data used in the assignment.
"""
import simplejson as js
import itertools as it

def group_count(array, field=None):
    """
    Count occurrence of elements in an array
    array: array-like
    field: None(default): group by element values and count occurrence;
           str: group by field and count occurrence.
    >>> group_count([1, 1, 0, 3, 5, 3])
    [(0, 1), (1, 2), (3, 2), (5, 1)]
    >>> group_count([])
    []
    >>> group_count([{'a': 1, 'b': 2}, {'a': 1, 'b': 3}, {'a': 2, 'b': 2}], field="a")
    [(1, 2), (2, 1)]
    """
    # Tested outside doctest:
    # >>> group_count([{'a': 1}, {'b': 1}], field='a')
    # ValueError
    # >>> group_count([{'a': 1, 'b': 2}, {'a': 1, 'b': 3}, {'a': 2, 'b': 2}])
    # ValueError
    if len(array) == 0:
        return  []
    counts = []
    if field == None:
        if type(array[0]) == dict:
            raise ValueError('When input array contains dict, field should be specified.')
        array.sort()
        for k, g in it.groupby(array):
            counts.append((k, len(list(g))))
    else:
        # Check if field exists in all elements of the array
        if sum([field in x for x in array]) < len(array):
            raise ValueError('Field %s does not exist in every element in the array'%field)
        array.sort(key=lambda x: x[field])
        for k, g in it.groupby(array, lambda x: x[field]):
            counts.append((k, len(list(g))))
    return counts

def load_jsonl(inputfile):
    """
    This function loads a jsonl file.
    """
    D = []
    with open(inputfile) as f:
        for line in f.readlines():
            D.append(js.loads(line))
    return D

def load_txt(inputfile):
    """
    This function loads a text file. 
    """
    T = ''
    with open(inputfile) as f:
        T = f.read()
    return T

def clean_string(string):
    """
    Turn to lower case, remove non-alphanumerics
    """
    return re.sub(r'\W+', ' ', string).lower()


def get_date(datetime):
    """
    Get the date part of a datetime in the format
    of "YYYY-MM-DDThh:mm:ssZ".
    >>> get_date('2015-09-03T03:02:01Z')
    '2015-09-03'
    """
    return datetime.split('T')[0] 

def get_date_noyear(datetime):
    """
    Get the month-day part of a datetime in the format
    of "YYYY-MM-DDThh:mm:ssZ".
    >>> get_date_noyear('2015-09-03T03:02:01Z')
    '09-03'
    """
    return datetime.split("T")[0].split('-', 1)[1]

def add_date_noyear(data):
    for d in data:
        d['date'] = get_date_noyear(d['published'])
    return data


if __name__ == '__main__':
    import doctest
    doctest.testmod()


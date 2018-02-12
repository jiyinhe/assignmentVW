import simplejson as js

def load_jsonl(inputfile):
    D = []
    with open(inputfile) as f:
        for line in f.readlines():
            D.append(js.loads(line))
    return D

def get_date(datetime):
    return datetime.split('T')[0] 

def load_txt(inputfile):
    T = ''
    with open(inputfile) as f:
        T = f.read()
    return T

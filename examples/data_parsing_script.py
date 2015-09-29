'''One-line description of what this script/module does

    Paragraph description of what this script/module does.
'''

# standard modules
import os
import os.path
import re
from collections import namedtuple
from StringIO import StringIO

def main():
    # make a few random .csv files
    
    # grab all of the .csv files we can find
    csv_files = find_files(pattern=r'\.csv$', r=True)
    for file_name in csv_files:
        csv_to_double_list(file_name)

def csv_to_double_list(file_name):
    '''Parse a CSV file into a double list
    
    Args:
        file_name (str)
    Return:
        [['item1', 'item2', 'item3'], [...], [...], ...]
    '''
    
    rows = []
    with open(file_name) as f:
        for line in f:
            rows.append(line.split(','))
    return rows

class LabeledTable():
    '''Rectangular data table with column labels
    
    Instantiation Args:
        col_labels (list(str)): Sequence of string lablels for the columns.
            Note that the length of this argument sets the width of the table.
        double_iterable (list(list)): Sequence of sequences that will be used
            to fill the table.
    '''
    
    def __init__(self, col_labels, double_iterable=[[]]):
        self._rtype = namedtuple('TableRow', col_labels)
        self._rows = [self._rtype(row) for row in double_iterable]
    
    @classmethod
    def from_csv(cls, file_name):
        '''Create a LabeledTable (or sub-class) from a csv-formated file
        
        Args:
            file_name (str)
        Return:
            (LabeledTable)
        '''
        
        rows = []
        with open(file_name) as f:
            for line in f:
                rows.append(line.split(','))
        return cls(rows[0], rows[:1])
    
    @property
    def cols(self):
        return self._rtype._fields
    
    @property
    def row_type(self):
        return self._rtype
    
    @property
    def shape(self):
        return tuple(len(self._rows), len(self._rtype._fields))
    
    def __iter__(self):
        for row in self._rows:
            yield row
    
    def __len__(self):
        return len(self._rows)
    
    def __getitem__(self, i):
        return self._rows[i]
    
    def __setitem__(self, i, seq):
        self.M[i] = self._rtype(seq)
    
    def append_row(self, new_row):
        self._rows.append(self._rtype(new_row))
    
    def insert_row(self, i, new_row):
        self._rows.insert(i, self._rtype(new_row))
    
    def pop_row(self, i=-1):
        return self._rows.pop(i)
    
    def to_tuple(self):
        return tuple(self._rtype._fields + tuple(tuple(r) for r in self._rows))
    
    def write_csv(self, save_path):
        ftxt = StringIO()
        ftxt.write(','.join(self._rtype._fields))
        ftxt.write('\n')
        for row in self._rows:
            ftxt.write(','.join(row))
            ftxt.write('\n')
        
        with open(save_path, 'w') as f:
            f.write(ftxt.getvalue())

def find_files(cwd='.', pattern='.*', r=True):
    '''Find files with matching names
    
    This function will search for files who's path matches the given regular
    expression (default is '.*'). There is an optional flag to do a depth-
    first search of all sub-directories.
    
    Args:
        cwd (str): current working directory
        pattern (str): regex pattern used to match the file names
        r (bool): flag for recursive search
    Returns:
        (list) ['./file.ext', './file.ext', './file.ext', ...]
    '''
    
    work_stack = [cwd]
    matching_files = []
    while work_stack:
        path = work_stack.pop()
        if os.path.isdir(path) and r:
            work_stack.extend([os.join(path, item) for item in os.listdir(path)])
        elif re.search(pattern, path):
            matching_files.append(path)
    return matching_files

if __name__ == '__main__':
    main()

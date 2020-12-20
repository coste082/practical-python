# fileparse.py
#
# Exercise 3.3
import csv
import gzip

def parse_csv(lines,select=None,types=None,has_headers=True,delimiter=','):
    '''
    Opens csv and return as dictionary if headers are available, else tuple. Correctly converts to type.
    '''
    rows = csv.reader(lines,delimiter=delimiter)
    type_dict = {'name':str,'price':float,'shares':int,'date':str,'time':str}
    if select and has_headers==False:
        raise RuntimeError('Select argument requires columns headers')
    if types and not has_headers:
        records = [tuple([types[i](r) for i,r in enumerate(row)]) for row in rows]
        return records
    headers = next(rows)
    records = []
    if select:
        for i in select:
            if i not in headers:
                raise RuntimeError('{} not in header row.'.format(i))
        headers_select = [headers[i] for i,r in enumerate(headers) if r in select]
    else:
        select = headers
        headers_select = headers
    type_conversions = [type_dict[i] for i in headers_select]
    indices = [headers.index(i) for i in headers if i in select]
    for row in rows:
        if not row:
            continue
        row_select=[r for i,r in enumerate(row) if i in indices]
        row_select = [type_conversions[i](r) for i,r in enumerate(row_select)]
        record = dict(zip(headers_select,row_select))
        records.append(record)
    return records

with gzip.open('Data/portfolio.csv.gz','rt') as file:
    parse_csv(file)
# pcost.py
#
# Exercise 1.27

import csv
def portfolio_cost(datafile='Work/Data/portfolio.csv'):
    total = 0
    with open(datafile, 'rt') as f:
        headers = [i.rstrip() for i in next(f).split(',')]
        for rowno,row in enumerate(f):
            row = [i.rstrip() for i in row.split(',')]
            record = dict(zip(headers,row))
            try:
                total += int(record['shares'])*float(record['price'].rstrip())
            except ValueError:
                print(f'Row  {rowno}: Bad row: {row}',end='')
    print("\nTotal cost: ${:.2f}".format(total))

portfolio_cost('Work/Data/portfoliodate.csv')
# report.py
#
# Exercise 2.4
import pprint

def read_portfolio_to_tuples(datafile='Data/portfolio.csv'):
    portfolio = []
    with open(datafile, 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            holding = (row[0].strip('"'),int(row[1]),float(row[2]))
            portfolio.append(holding)
    return portfolio

def read_portfolio_to_dicts(datafile='Data/portfolio.csv'):
    '''
    Reads csv to a list of dictionaries. Can be used with variable column inputs.
    '''
    portfolio = []
    type_conversions = {'name':str,'price':float,'shares':int,'date':str,'time':str}
    with open(datafile, 'rt') as f:
        headers = [i.strip('"').rstrip() for i in next(f).split(',')]
        type_conversions = {i:type_conversions[i] for i in headers}
        indices = [headers.index(i) for i in type_conversions.keys() if i in type_conversions.keys()]
        for line in f:
            line = line.split(',')
            holding = {}
            for j,item in enumerate(line):
                try:
                    holding[headers[j]] = type_conversions[headers[j]](item).strip('"')
                except:
                    holding[headers[j]] = type_conversions[headers[j]](item)
            portfolio.append(holding)
    return portfolio

def read_prices(datafile:str='Data/prices.csv') -> dict:
    '''
    Reads csv of current stock prices and returns dictionary.
    '''
    price_dict = {}
    with open(datafile, 'rt') as f:
        for line in f:
            row = line.split(',')
            if len(row) == 2:
                price_dict[row[0].strip('"')] = float(row[1])
    return price_dict

def make_report(potfolio,prices,print_report='n'):
    '''
    Generate report to add current stock prices to portfolio.
    '''
    stocks = []
    headers = [i.rstrip() for i in portfolio[0].keys()]
    for h in portfolio:
        stocks.append([i for i in h.values()])
    if print_report == 'y':
        for i,d in enumerate(headers):
            print('{:>10s}'.format(d),end=' ')
        print('')
        for i in enumerate(headers):
            print('{:->10s}'.format('-'),end=' ')
        print('')
        for i,r in enumerate(stocks):
            for j in r:
                if isinstance(j,str):
                    print('{:>10s}'.format(j),end = ' ')
                elif isinstance(j,int):
                    print('{:>10d}'.format(j),end = ' ')
                elif isinstance(j,float):
                    print('{:>10.2f}'.format(j),end = ' ')
            print('')
    return stocks

portfolio = read_portfolio_to_dicts('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio,prices,print_report='y')
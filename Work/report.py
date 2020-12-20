# report.py
#
# Exercise 2.4
import pprint
import csv
from fileparse import parse_csv

def print_portfolio(portfolio):
    '''
    Prints portfolio of stocks in nice-looking format.
    '''
    headers = [i.rstrip() for i in portfolio[0].keys()]
    for i,d in enumerate(headers):
        print('{:>12s}'.format(d),end=' ')
    print('')
    for i in enumerate(headers):
        print('{:->12s}'.format('-'),end=' ')
    print('')
    for i,r in enumerate(portfolio):
        for j in r.values():
            if isinstance(j,str):
                print('{:>12s}'.format(j),end = ' ')
            elif isinstance(j,int):
                print('{:>12d}'.format(j),end = ' ')
            elif isinstance(j,float):
                print('{:>12.2f}'.format(j),end = ' ')
        print('')

def read_portfolio_to_tuples(datafile='Data/portfolio.csv'):
    '''
    Reads csv file to list of tuples.
    '''
    portfolio = []
    with open(datafile, 'rt') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for line in f:
            holding = (row[0],int(row[1]),float(row[2]))
            portfolio.append(holding)
    return portfolio

def read_portfolio_to_dicts(datafile='Data/portfolio.csv',print_data='n'):
    '''
    Reads csv to a list of dictionaries. Can be used with variable column inputs.
    '''
    with open(datafile,'rt') as file:
        portfolio = parse_csv(file)
        if print_data == 'y':
            print_portfolio(portfolio)
        return portfolio

def read_prices(datafile:str='Data/prices.csv') -> dict:
    '''
    Reads csv of current stock prices and returns dictionary.
    '''
    with open(datafile,'rt') as file:    
        price_tuples = parse_csv(file,types=[str,float],has_headers=False)
        price_dict = {}         #can I make this dictionary population a one liner?
        for i in price_tuples:
            if i:
                price_dict[i[0]] = i[1]
        return price_dict

def portfolio_report(potfolio_file,prices_file,print_data='n'):
    '''
    Add current stock prices to portfolio and calculate price change
    '''
    portfolio = read_portfolio_to_dicts(potfolio_file)
    prices = read_prices(prices_file)
    for i in portfolio:
        i['current_price'] = prices[i['name']]
        i['price_change'] = prices[i['name']] - i['price']
    if print_data == 'y':
        print_portfolio(portfolio)
    return portfolio

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: {} portfoliofile pricefile'.format(sys.argv[0]))
    portfolio_report(args[1],args[2],print_data='y')

if __name__ == '__main__':
    import sys
    main(sys.argv)
# report.py
#
# Exercise 2.4
import pprint
import csv
from fileparse import parse_csv
from stock import Stock
from portfolio import Portfolio
import tableformat

def print_portfolio(portfolio,formatter):
    '''
    Prints portfolio of stocks in nice-looking format.
    '''
    headers = [i for i in dir(portfolio[0]) if str(i) in ['name','price','shares',
                                                          'current_price','change']]
    if len(headers) == 5:
        headers = [headers[i] for i in [2,4,3,1,0]]
    else:
        headers = [headers[i] for i in [0,2,1]]
    formatter.headings(headers)
    for row in portfolio:
        formatter.row([getattr(row,k) for k in headers])

def read_portfolio_to_tuples(datafile='Data/portfolio.csv'):
    '''
    Reads csv file to list of tuples.
    '''
    with open(datafile, 'rt') as f:
        port = Portfolio.from_csv(lines)
    return portfolio

def read_portfolio(datafile='Data/portfolio.csv',print_data='n',**opts):
    '''
    Reads csv to a list of dictionaries. Can be used with variable column inputs.
    '''
    with open(datafile) as lines:
        return Portfolio.from_csv(lines, **opts)

def read_prices(datafile:str='Data/prices.csv') -> dict:
    '''
    Reads csv of current stock prices and returns dictionary.
    '''
    with open(datafile,'rt') as file:    
        price_tuples = parse_csv(file,types=[str,float],has_headers=False)
        price_dict = {}  
        for i in price_tuples:
            if i:
                price_dict[i[0]] = i[1]
        return price_dict


def portfolio_report(potfolio_file,prices_file,print_data='n',fmt='txt'):
    '''
    Add current stock prices to portfolio and calculate price change
    '''
    portfolio = read_portfolio(potfolio_file)
    prices = read_prices(prices_file)
    for s in portfolio:
        s.update_prices(prices[s.name])
    if print_data == 'y':
        formatter = tableformat.create_formatter(fmt)
        print_portfolio(portfolio,formatter)
    return portfolio

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: {} portfoliofile pricefile format'.format(sys.argv[0]))
    portfolio_report(args[1],args[2],print_data='y',fmt=args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)
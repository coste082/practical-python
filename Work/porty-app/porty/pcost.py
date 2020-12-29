# pcost.py
#
# Exercise 1.27

from .fileparse import parse_csv
from .stock import Stock
from . import report

def portfolio_cost(datafile='Data/portfolio.csv'):
    with open(datafile,'rt') as f:
        portfolio = report.read_portfolio(datafile)
        return portfolio.total_cost

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: {} portfoliofile pricefile'.format(sys.argv[0]))
    portfolio_cost(args[1])

if __name__ == '__main__':
    import sys
    main(sys.argv)
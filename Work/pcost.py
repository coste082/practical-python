# pcost.py
#
# Exercise 1.27

from fileparse import parse_csv

def portfolio_cost(datafile='Data/portfolio.csv'):
    portfolio = parse_csv(datafile)
    total = sum([i['shares']*i['price'] for i in portfolio])
    print("\nTotal cost: ${:.2f}".format(total))

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: {} portfoliofile pricefile'.format(sys.argv[0]))
    portfolio_cost(args[1])

if __name__ == '__main__':
    import sys
    main(sys.argv)
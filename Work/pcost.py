# pcost.py
#
# Exercise 1.27
total = 0
with open('Work/Data/portfolio.csv', 'rt') as f:
    for line in f:
        l = line.split(',')
        if l[0] != 'name':
            total += int(l[1])*float(l[2])

print(total)
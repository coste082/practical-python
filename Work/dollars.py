bill_thickness = 0.11 * 0.001 #meters
sears_height = 442 #meters
num_bills = 1
day = 1

while bill_thickness < sears_height:
    num_bills *= 2
    bill_thickness *= 2
    day += 1

print('''\nOn day {} the stack of {:,} bills will be thicker than the tower.\n'''.format(day,num_bills))
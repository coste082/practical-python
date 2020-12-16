# mortgage.py
#
# Exercise 1.7


###
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
###
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1


while principal > 0:
    if extra_payment_start_month <= month <= extra_payment_end_month:
        total_paid += (payment + extra_payment)
        principal = principal * (1+rate/12) - payment - extra_payment
    else:
        total_paid += payment
        principal = principal * (1+rate/12) - payment
    print(month, total_paid, principal)
    month += 1
    
print('\nTotal paid: ${:,.2f} over {:.1f} years\n'.format(total_paid, month/12))
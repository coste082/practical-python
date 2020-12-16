# bounce.py
#
# Exercise 1.5
bounce_height = 100 # meters

for i in range(10):
    bounce_height *= 3/5
    print(i, round(bounce_height,4))
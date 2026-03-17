# Import libraries
from matplotlib import pyplot as plt


# Creating dataset
cars = ['AUDI', 'BMW', 'FORD',
        'TESLA', 'JAGUAR', 'MERCEDES', 'TEST OPTION']

data = [23, 17, 35, 29, 12, 42, 36]

# Creating plot
fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=cars)

# show plot
plt.show()
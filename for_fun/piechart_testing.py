# Import libraries
from matplotlib import pyplot as plt


# Creating dataset

cars = ['SAVINGS', 'EMERGENCY', 'BILLS', 'FOOD', 'GAS']

data = [1000, 500, 2000, 200, 300]

# Creating plot
fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=cars)

# show plot
plt.show()
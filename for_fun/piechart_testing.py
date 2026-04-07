# Import libraries
from matplotlib import pyplot as plt
from faker import Faker
import random

fake = Faker()

# Creating dataset


def piechart(categories, data):
    total = sum(data)
    t_categories = []

    for i in data:
        print(i)
    
    print(total)

    for x in range(0, len(categories)):
        t_categories.append(f"{categories[x]} ({round((data[x] / total)*100, 2)}%)")

    fig = plt.figure(figsize=(10, 7))
    plt.pie(data, labels=t_categories)
    plt.show()


items = [str(fake.word()), str(fake.word()), str(fake.word()), str(fake.word()), str(fake.word())]
data = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]

piechart(items, data)
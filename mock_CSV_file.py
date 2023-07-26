import pandas as pd
import numpy as np
from random import randint, choice
from faker import Faker

# Initialize a faker generator
fake = Faker()

# Define some products
products = ['Laptop', 'Headphones', 'TV', 'Phone', 'Monitor', 'Keyboard', 'Mouse', 'Speaker', 'Charger', 'Tablet']

# Create a dataframe
df = pd.DataFrame({
    'OrderID': [fake.unique.random_number(digits=5) for _ in range(100)],
    'Product': [choice(products) for _ in range(100)],
    'Quantity': [randint(1, 10) for _ in range(100)],
    'PriceEach': [round(np.random.uniform(10.5, 500.5), 2) for _ in range(100)],
    'OrderDate': [fake.date_between(start_date='-1y', end_date='today') for _ in range(100)]
})

# Save the dataframe to a CSV file
df.to_csv('sales_data.csv', index=False)

print("CSV file 'sales_data.csv' has been created.")

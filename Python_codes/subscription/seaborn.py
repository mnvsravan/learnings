import pandas as pd
import numpy as np
import re
import seaborn as sns

# Question-1:
# The dataset is based on NFTs. This is quite large. So, when you will read the dataset, you have to wait. The link of the dataset: https://tinyurl.com/2pfhncqw

# Your task is to make a pivot table by using the columns "verification_status", "contract_type", "rarity_score" and "last_sale_price" to find out the total values.
df = pd.read_csv('https://tinyurl.com/2pfhncqw')
print(df.shape)
print(df.head())
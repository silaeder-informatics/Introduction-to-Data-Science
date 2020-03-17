import pandas as pd

filename = 'friends_data.csv'
data = pd.read_csv(filename)
print(len(data.Date))
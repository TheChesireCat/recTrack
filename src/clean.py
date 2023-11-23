import pandas as pd

# Read CSV file
data = pd.read_csv("output.csv")

# Convert the 'updated' column to datetime
data['updated'] = pd.to_datetime(data['updated'])

# Sort the data by 'updated' column
data_sorted = data.sort_values(by='updated')

# Save the sorted data to the same CSV file
data_sorted.to_csv("output.csv", index=False)

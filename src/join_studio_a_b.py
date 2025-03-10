import pandas as pd

# Read CSV file
data = pd.read_csv("output.csv")

# Convert the 'updated' column to datetime
data['updated'] = pd.to_datetime(data['updated'])

# Update location_name values for Studio A and Studio B with 'Marino Center' prefix
data['location_name'] = data['location_name'].replace({
    'Studio A': 'Marino Center - Studio A',
    'Studio B': 'Marino Center - Studio B'
})

# Save updated data to CSV
data.to_csv("output.csv", index=False)

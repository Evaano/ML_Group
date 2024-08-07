import pandas as pd
import numpy as np

# Function to create variations
def create_variation(value):
    # Ensure the value is not negative
    variation = max(0, int(value + np.random.normal(0, 2)))
    return variation

# Read the original CSV file
df = pd.read_csv('original_data.csv')

# List of monthly columns
monthly_columns = [col for col in df.columns if col.startswith(('JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER'))]

# Apply variations to each monthly column
for col in monthly_columns:
    df[col] = df[col].apply(create_variation)

# Write the modified data to a new CSV file
df.to_csv('modified_data3.csv', index=False)

print('Variations created and saved to modified_data.csv')

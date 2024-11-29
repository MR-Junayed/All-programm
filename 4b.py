import pandas as pd

# Correcting the dictionary (using lists for 'Name' and 'City')
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [23, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Filter rows where Age is greater than 25
filtered_df = df[df['Age'] > 25]

# Display the filtered DataFrame
print("\nFiltered DataFrame (Age > 25):")
print(filtered_df)
import pandas as pd

# Load dataset
df = pd.read_csv('archive/m_custom.csv')

# Dataset overview
print("Shape:", df.shape)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicates
print("\nDuplicates:", df.duplicated().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Standardize column names
df.columns = df.columns.str.lower()

# Statistics
print("\nStatistics:")
print(df.describe(include='all'))

# Save cleaned data
df.to_csv("cleaned_customers.csv", index=False)

print("\nData Cleaning Completed!")
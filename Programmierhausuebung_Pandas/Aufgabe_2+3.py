import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset into a pandas DataFrame
df = pd.read_csv('./Programmierhausuebung_Pandas/data/husbandwife_raw.csv')

# Inspect the columns HHght (husband's height) and WHght (wife's height)
print(df[['HHght', 'WHght']].head())

# Check for any issues in the columns
print(df[['HHght', 'WHght']].describe())

# Fix any issues if necessary (e.g., handling missing values or incorrect data types)
df['HHght'] = pd.to_numeric(df['HHght'], errors='coerce')
df['WHght'] = pd.to_numeric(df['WHght'], errors='coerce')

# Filter out rows with missing values in HHght and WHght
df = df.dropna(subset=['HHght', 'WHght'])

# Remove heights with a value of 0 (A height of 0 is not possible)
df = df[(df['HHght'] != 0) & (df['WHght'] != 0)]

# Check the summary statistics of the cleaned data
print(df[['HHght', 'WHght']].describe())

# Calculate the mean value of the men's height
mean_husband_height = df['HHght'].mean()
print(f"The mean value of the men's height is: {mean_husband_height}")

# Create a histogram for the heights of husbands and wives
sns.histplot(df['HHght'], color='blue', label='Husbands', kde=True, bins=30)
sns.histplot(df['WHght'], color='red', label='Wives', kde=True, bins=30)

# Add labels and legend
plt.xlabel('Height (mm)')
plt.ylabel('Count')
plt.legend()

# Save the plot as a PNG image
plt.savefig('./heights_histogram.png')

# Show the plot
plt.show()
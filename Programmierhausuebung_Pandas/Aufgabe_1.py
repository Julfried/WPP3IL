import pandas as pd

import matplotlib.pyplot as plt


# Load the CSV file into a DataFrame
df = pd.read_csv('./Programmierhausuebung_Pandas/data/StudyDegrees.csv')

# Filter the data for Engineering graduates
engineering_graduates = df['Engineering']
years = df['Year']

# Plot the number of Engineering graduates over the years
plt.figure(figsize=(10, 6))
plt.plot(years, engineering_graduates)
plt.title('Number of Engineering Graduates Over the Years')
plt.xlabel('Year')
plt.ylabel('Students')

# Add legend to top right
plt.legend(['Engineering Graduates'])

# Save the plot as a PNG file
plt.savefig('engineering_graduates.png')

# Show the plot
plt.show()
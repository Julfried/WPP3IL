import pandas as pd

# Load the dataset
df = pd.read_csv("./Programmierhausuebung_Pandas/data/opsd_austria_data_daily.csv", parse_dates=['Date'], index_col='Date')

# Filter the data for the years 2012 to 2015 and the months October, November, and December
filtered_data = df.loc['2012-10':'2015-12']
filtered_data.index = pd.to_datetime(filtered_data.index) # Convert the index to a datetime object
filtered_data = filtered_data[filtered_data.index.month.isin([10, 11, 12])]

filtered_data.to_csv("test.csv")

# Calculate the mean temperature
mean_temperature = filtered_data['Temperature_CEL'].mean()

print(f"The mean temperature for October, November, and December from 2012 to 2015 is: {mean_temperature:.2f}°C")
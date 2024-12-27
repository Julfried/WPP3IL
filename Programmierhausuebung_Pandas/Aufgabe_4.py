import pandas as pd

# Load the dataset
df = pd.read_csv("./Programmierhausuebung_Pandas/data/opsd_austria_data_daily.csv", parse_dates=['Date'], index_col='Date')

# Filter the data for the years 2012 to 2015 and the months October, November, and December
filtered_data = df.loc['2012-10':'2015-12']
filtered_data.index = pd.to_datetime(filtered_data.index) # Convert the index to a datetime object
filtered_data = filtered_data[filtered_data.index.month.isin([10, 11, 12])]

# Calculate the mean temperature
mean_temperature = filtered_data['Temperature_CEL'].mean()

print(f"The mean temperature for October, November, and December from 2012 to 2015 is: {mean_temperature:.2f}°C")

# Filter the data for the hours between 8:00 and 18:00 (18:00 not included)
filtered_data_daytime = filtered_data.between_time('08:00', '18:00', inclusive="left")

# Calculate the mean temperature for the specified daytime
mean_temperature_daytime = filtered_data_daytime['Temperature_CEL'].mean()

print(f"The mean temperature for October, November, and December from 2012 to 2015 between 8:00 and 18:00 is: {mean_temperature_daytime:.2f}°C")
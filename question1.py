import pandas as pd

# Read in CSV of data to dataframe
df = pd.read_csv("2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv")

print('First, we show the simple mean and median order_amount of all orders:')
# Simple mean and media of order_amount
mean = df['order_amount'].mean()
median = df['order_amount'].median()
print('Mean of order_amount:', mean)
print('The mean yields suspicious results, clearly skewed by outliers.')
print('The median is a bit better.')
print('Median of order_amount:', median)
print()

print('Next, we calculate and show the simple mean and median order_amount but by each shop:')
# Simple mean and median of order_amount but by each shop_id
dfmean = df.groupby('shop_id', as_index=False)['order_amount'].mean()
dfmedian = df.groupby('shop_id', as_index=False)['order_amount'].median()
print("Mean by each shop_id's mean:", dfmean['order_amount'].mean())
print("Median by each shop_id's median:", dfmedian['order_amount'].median())
print('The results are similar as before. Median still seems to more accurately describe the data but this could be improved.')
print()

print("Finally, let's look at the standard deviation of data by order_amount:")
# Calculate standard deviation
std = df['order_amount'].std()
print('Standard deviation of order_amount:', std)
print("With the standard deviation being so high, this shows that the order_amount's have a very wide range and are thus less reliable.")
print()

print("Finally, let's calculate the interquartile range in order to get the middle 50% of values.")
# Calculate IQR
Q1 = df['order_amount'].quantile(0.25)
Q3 = df['order_amount'].quantile(0.75)
IQR = Q3 - Q1
print('And from there, calculate the mean and median again, from this new range of values.')
# Filter skewed values (values that fall between Q1 - 1.5IQR and Q3 + 1.5IQR)
dfq = df.query('(@Q1-1.5*@IQR) <= order_amount <= (@Q3+1.5*@IQR)')
print('IQR mean:', dfq['order_amount'].mean())
print('IQR median:', dfq['order_amount'].median())
print('The IQR mean and median are quite similar, showing that we have found a more realistic "average" order_amount.')
print("It's also interesting to note that these values are very similar to the original simple median of all order_amount's.")
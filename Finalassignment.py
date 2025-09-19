import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('insurance.csv')

# Display the first 5 rows
print(df.head())

print(df.info())           # Shows data types and non-null counts
print(df.isnull().sum())   # Shows the number of missing values in each column

df = df.dropna()


df = df.fillna(df.mean(numeric_only=True))

df = pd.read_csv('insurance.csv')

print(df.describe())


grouped = df.groupby('region')['age'].mean()
print(grouped)


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('insurance.csv')

# 1. Line chart (example: charges over index, as there is no time column)
plt.figure(figsize=(8, 4))
plt.plot(df.index, df['charges'])
plt.title('Charges Trend Over Records')
plt.xlabel('Record Index')
plt.ylabel('Charges')
plt.show()

# 2. Bar chart: Average charges per region
avg_charges_region = df.groupby('region')['charges'].mean()
avg_charges_region.plot(kind='bar', color='skyblue')
plt.title('Average Charges by Region')
plt.xlabel('Region')
plt.ylabel('Average Charges')
plt.show()

# 3. Histogram: Distribution of age
df['age'].plot(kind='hist', bins=30, color='orange', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter plot: Age vs. Charges
plt.scatter(df['age'], df['charges'], alpha=0.5)
plt.title('Age vs. Charges')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Ahmedabad_real_Estate.csv')

#########-------  Understand data------ 
# print(df.head())
# print(df.columns)
# print(df.info())

#### ------------Data Cleaning----------
df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()  
print(df.columns.tolist())
df = df.drop_duplicates()

# Numerical Columns Cleaning

df['price_in_cr'] = df['price_in_cr'].astype(str).str.replace(",", "").astype(float)
print(df['price_in_cr'])

# Categorical Columns Cleaning
df['property_type'] = df['property_type'].str.strip().str.lower()
print(df['property_type'].tolist())

df = df.drop_duplicates()
# print(df.info())
# print(df)

# Question 1: Which is the costliest flat in the dataset?

costliest_flat = df.loc[df['price_in_cr'].idxmax()]
print(costliest_flat)

'''
lets make the output in sentance format

name              abhijyot harmony
location          abhijyot harmony
area_in_sqft                1750.0
area_type                    super
property_title    abhijyot harmony
property_type                 flat
bhk_type                         3
price_in_cr                  120.0
'''
print(
    f"The costliest property is a {costliest_flat['bhk_type']} BHK flat "
    f"located in {costliest_flat['location']}, priced at ₹{costliest_flat['price_in_cr']} Cr.\n"
    f"Property Title: {costliest_flat['property_title']}\n"
    f"Area Type: {costliest_flat['area_type']}\n"
    f"Owner Name: {costliest_flat['name']}"
)

# Question 2: Which locality has the highest average price ?
highest_avg_price_locality = df.groupby('location')['price_in_cr'].mean().idxmax()
print(f"The locality with the highest average price is {highest_avg_price_locality}.")
print(df.groupby('location')['price_in_cr'].mean().sort_values(ascending=False).head(10))

# Question 3: Which locality has the highest rate per square foot?
highest_rate_locality = df.groupby('location')['area_in_sqft'].mean().idxmax()
print(f"The location with the highest rate per square foot is {highest_rate_locality}.")

# Question 4: How does area impact price?
sns.scatterplot(data=df, x='location', y='price_in_cr')
plt.show()


# Question 5: Which BHK configuration is most expensive based on per sqft rate?
most_expensive_bhk = df.groupby('bhk_type')['area_in_sqft'].mean().idxmax()
print(f"The most expensive BHK configuration on average is {most_expensive_bhk} BHK.")



# # Question 6: Which property type is the costliest?
most_expensive_property_type = df.groupby('property_type')['area_in_sqft'].mean().idxmax()
print(f"The most expensive property type is {most_expensive_property_type}.")

# # Question 7: Do certain builders price higher?
print(df.groupby("name")["area_in_sqft"].mean().sort_values(ascending=False).head(5))
# print name of top 5 
print("The top 5 builders that price higher are:", end=" ")
top_5_builders = df.groupby("name")["area_in_sqft"].mean().sort_values(ascending=False).head(5)
for builder in top_5_builders.index:
    print(builder, end=", ")

# # Question 8: Are larger homes more expensive per sqft?
sns.scatterplot(data=df, x='bhk_type', y='area_in_sqft')
plt.show()
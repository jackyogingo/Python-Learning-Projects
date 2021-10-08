#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing libraries 
import numpy as np
import pandas as pd


# In[2]:


# create a list
list1 = [1,2,3,4]
list1


# In[3]:


# convert the list to array
array1 = np.array(list1)
print(array1)


# In[4]:


# operation on array
toyPrices = np.array([5,8,3,6])
print(toyPrices - 2)


# In[5]:


# Create a Series using a NumPy array of ages with the default numerical indices
ages = np.array([13,25,19])
series1 = pd.Series(ages)
print(series1)


# In[6]:


# Create a Series using a NumPy array of ages but customize the indices to be the names that correspond to each age
ages = np.array([13,25,19])
series1 = pd.Series(ages,index=['Emma', 'Swetha', 'Serajh'])
print(series1)


# In[7]:


# create table/dataframe using pd.DataFrame

dataf = pd.DataFrame([
    ['John Smith','123 Main St',34],
    ['Jane Doe', '456 Maple Ave',28],
    ['Joe Schmo', '789 Broadway',51]
    ],
    columns=['name','address','age'])
print(dataf)


# In[8]:


dataf.set_index('name')


# In[9]:


# Create a DataFrame 'df1'
# passing a dictionary in the dataframe

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name' : ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', 'red', 'black']
})

print(df1)


# In[10]:


# Create a DataFrame 'df2'
# passing a nested list in the dataframe

df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]
],
  columns=['Store ID','Location','Number of Employees']   
  )

print(df2)


# In[11]:


# Loading and reading data from a csv file 

# df.read_csv('file name.csv')


# In[13]:


# selecting a column from a dataframe

# df = dfname.column_name


# In[ ]:


# selecting dataframes using logical operators e.g

a = df[df.name == 'Jax']

b = df[df.age > 30]

c = df[(df.age < 10) | (df.age > 70)]

frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]   


# In[ ]:


# selecting several columns in a dataframe using 'isin' e.g

names = df[df.name.isin(['Jax', 'Adhis', 'Ogingo'])]

comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots', 'ballet flats'])]


# In[ ]:


# importing pandas package
import pandas as pd
  
# making data frame from csv file
data = pd.read_csv("employees.csv")
  
# creating a bool series from isin()
new = data["Gender"].isin(["Male"])
  
# displaying data with gender = male only
data[new]


# In[ ]:


# importing pandas package
import pandas as pd
  
# making data frame from csv file
data = pd.read_csv("employees.csv")
  
# creating filters of bool series from isin()
filter1 = data["Gender"].isin(["Female"])
filter2 = data["Team"].isin(["Engineering", "Distribution", "Finance" ])
  
# displaying data with both filter applied and mandatory 
data[filter1 & filter2]


# In[14]:


import pandas as pd
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])
df


# In[15]:


# select a single row 'March'

march = df.iloc[2]
march


# In[16]:


# select multiple rows 'april_may_june'

april_may_june = df.iloc[3:6]
april_may_june


# In[17]:


# select a single column

clinic_north = df.clinic_north
clinic_north


# In[18]:


# select multiple columns 

clinic_north_south = df[['clinic_north', 'clinic_south']]
clinic_north_south


# ### Modifying DataFrames

# In the previous lesson, you learned what a DataFrame is and how to select subsets of data from one.
# 
# In this lesson, you’ll learn how to modify an existing DataFrame. Some of the skills you’ll learn include:
# 
# Adding columns to a DataFrame,
# Using lambda functions to calculate complex quantities, and 
# Renaming columns

# In[19]:


# we need to import pandas
# and load our data
import pandas as pd

df = pd.read_csv(r'C:\Users\p\Downloads\Employees.csv', encoding = "ISO-8859-1")


# In[20]:


df.head(10)


# #### Adding a Column I
# Sometimes, we want to add a column to an existing DataFrame. We might want to add new information or perform a calculation based on the data that we already have.
# 
# One way that we can add a new column is by giving a list of the same length as the existing DataFrame.

# In[21]:


# e.g

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here

df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']

print(df)


# In[22]:


import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here

df['Is taxed?'] = 'Yes'

print(df)


# Finally, you can add a new column by performing a function on the existing columns.

# In[23]:


df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add column here

df['Margin'] = df['Price']- df['Cost to Manufacture']

print(df)


# In[24]:


import pandas as pd

df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
columns=['Name', 'Email'])

df


# In[25]:


# Add lowercase name column here

df['Lowercase Name'] = df['Name'].apply(str.lower)

print(df)


# In[26]:


# Add uppercase name column here

df['Uppercase Name'] = df['Name'].apply(str.upper)

print(df)


# #### Reviewing Lambda Function
# A lambda function is a way of defining a function in a single line of code. Usually, we would assign them to a variable.

# For example, the following lambda function multiplies a number by 2 and then adds 3:

# In[27]:


mylambda = lambda x: (x * 2) + 3
print(mylambda(5))


# Create a lambda function mylambda that returns the first and last letters of a string, assuming the string is at least 2 characters long. 

# In[28]:


mylambda = lambda x: x[0] + x[-1]
print(mylambda('This is a string'))


# #### Reviewing Lambda Function: If Statements
# We can make our lambdas more complex by using a modified form of an if statement.
# 
# Suppose we want to pay workers time-and-a-half for overtime (any work above 40 hours per week). The following function will convert the number of hours into time-and-a-half hours using an if statement:

# In[29]:


def myfunction(x):
    if x > 40:
        return 40 + (x - 40) * 1.50
    else:
        return x
myfunction(80)


# In[30]:


myfunction = lambda x: 40 + (x - 40) * 1.50 if x > 40 else x
print(myfunction(80))


# In general, the syntax for an if function in a lambda function is:
# 
# lambda x: [OUTCOME IF TRUE] if [CONDITIONAL] else [OUTCOME IF FALSE]

# Write a lambda function that takes an inputted age and either returns Welcome to BattleCity! if the user is 13 or older or You must be over 13 if they are younger than 13. Your lambda function should be called mylambda.

# In[31]:


mylambda = lambda age: 'Welcome to BattleCity!' if age >= 13 else 'You must be over 13'
print(mylambda(15))


# #### Applying a Lambda to a Column
# In Pandas, we often use lambda functions to perform complex operations on columns. For example, suppose that we want to create a column containing the email provider for each email address in the following table:

# In[32]:


df = pd.DataFrame([
                ['JOHN SMITH', 'john.smith@gmail.com'],
                ['Jane Doe', 'jdoe@yahoo.com'],
                ['joe schmo', 'joeschmo@hotmail.com']
                ],
                columns = ["Name", "Email"]
                               
                )
df


# In[33]:


df['Email Provider'] = df['Email'].apply(lambda x: x.split('@')[-1])
print(df)                                        


# Create a lambda function get_last_name which takes a string with someone’s first and last name (i.e., John Smith), and returns just the last name (i.e., Smith).

# In[34]:


get_last_name = lambda x: x.split()[-1]


# The DataFrame df represents the hours worked by different employees over the course of the week. It contains the following columns:
# 
# 'name': The employee’s name
# 'hourly_wage': The employee’s hourly wage
# 'hours_worked': The number of hours worked this week
# Use the lambda function get_last_name to create a new column last_name with only the employees’ last name.

# In[36]:


df['last_name'] = df['Name'].apply(get_last_name)
print(df)


# ### Applying a Lambda to a Row
# We can also operate on multiple columns at once. If we use apply without specifying a single column and add the argument axis=1, the input to our lambda function will be an entire row, not a column. To access particular values of the row, we use the syntax row.column_name or row[‘column_name’].

# Suppose we have a table representing a grocery list:

# In[67]:


df = pd.DataFrame([
                    ['Apple', '1.00', 'No'],
                    ['Milk', '4.20', 'No'],
                    ['Paper Towels', '5.00', 'Yes'],
                    ['Light Bulbs', '3.75', 'Yes']
                ],
    columns = ['Item', 'Price', 'Is_taxed']
    
)
df


# If we want to add in the price with tax for each line, we’ll need to look at two columns: Price and Is taxed?.
# 
# If Is taxed? is Yes, then we’ll want to multiply Price by 1.075 (for 7.5% sales tax).
# 
# If Is taxed? is No, we’ll just have Price without multiplying it.
# 
# We can create this column using a lambda function and the keyword axis=1:

# In[74]:


df['Price with Tax'] = df.apply(lambda row:
     row['Price'] * 1.075
     if row['Is_taxed'] == 'Yes'
     else row['Price'],
     axis=1
)


# e.g 2
# Consider the following employee table:

# In[40]:


df = pd.DataFrame ([
    
[10310,	'Lauren Durham',	19,	43],
[18656,	'Grace Sellers',	17,	40],
[61254,	'Shirley Rasmussen',	16,	30],
[16886,	'Brian Rojas',	18,	47],
[89010,	'Samantha Mosley',	11,	38],
[7246,	'Louis Guzman',	14,	39],
[20578,	'Denise Mcclure',	15,	40],
[12869,	'James Raymond',	15,	32],
[53461,	'Noah Collier',	18,	35],
[14746,	'Donna Frederick',	20,	41],

    ],
    
  columns =['id',	'name',	'hourly_wage',	'hours_worked']  
    )
df


# If an employee worked for more than 40 hours, she needs to be paid overtime (1.5 times the normal hourly wage).
# 
# For instance, if an employee worked for 43 hours and made $10/hour, she would receive $400 for the first 40 hours that she worked, and an additional $45 for the 3 hours of overtime, for a total for $445.
# 
# Create a lambda function total_earned that accepts an input row with keys hours_worked and hourly_wage and uses an if statement to calculate the hourly wage.

# In[60]:


total_earned = lambda row: (row['hourly_wage'] * 40) + ((row['hours_worked']-40) * (row['hourly_wage']) * 1.5) if row['hours_worked'] > 40 else row['hours_worked'] * row['hourly_wage'] 


# In[61]:


df['total_earned'] = df.apply(total_earned, axis=1)
df


# ### Renaming Columns

# When we get our data from other sources, we often want to change the column names. For example, we might want all of the column names to follow variable name rules, so that we can use df.column_name (which tab-completes) rather than df['column_name'] (which takes up extra space).
# 
# You can change all of the column names at once by setting the .columns property to a different list. This is great when you need to change all of the column names at once, but be careful! You can easily mislabel columns if you get the ordering wrong. Here’s an example:

# In[77]:


df = pd.DataFrame({
    'name': ['John', 'Jane', 'Sue', 'Fred'],
    'age': [23, 29, 21, 18]
})
df.columns = ['First Name', 'Age']
df


# You also can rename individual columns by using the .rename method. 
# Here’s an example:

# In[5]:


import pandas as pd
df = pd.DataFrame({
    'name': ['John', 'Jane', 'Sue', 'Fred'],
    'age': [23, 29, 21, 18]
})
df


# In[6]:


# using .rename() to rename the columns 

df.rename(columns={
    'name': 'First Name',
    'age': 'Age'},
    inplace=True)
df


# Once more, you’ll be the data analyst for ShoeFly.com, a fictional online shoe store.
# 
# More messy order data has been loaded into the variable orders. Examine the first 5 rows of the data using print and head.

# In[16]:


orders = pd.DataFrame({
    'id': [54792, 54350, 42115, 76543, 98213],
    'first_name': ['Rebecca', 'Emily', 'Joyce', 'Justin', 'Andrew'],
    'last_name': ['Lindsay', 'Joyce', 'Waller', 'Erickson', 'Banks'],
    'gender': ['female', 'female', 'female', 'male', 'male'],
    'shoe_material': ['faux leather','faux leather', 'fabric', 'faux leather', 'leather']
})
print(orders.head())


# Many of our customers want to buy vegan shoes (shoes made from materials that do not come from animals). Add a new column called shoe_source, which is vegan if the materials is not leather and animal otherwise.

# In[18]:


orders['shoe_source'] = orders.shoe_material.apply(lambda source: 'vegan' if source != 'leather' else 'animal')
orders


# Our marketing department wants to send out an email to each customer. Using the columns last_name and gender create a column called salutation which contains Dear Mr. <last_name> for men and Dear Ms. <last_name> for women.

# In[25]:


orders['salutation'] = orders.apply(lambda row: 'Dear Mr. ' + row['last_name'] 
                                    if row['gender'] == 'male' 
                                    else 'Dear Ms. ' + row['last_name'], axis=1)
orders                                   


#!/usr/bin/env python
# coding: utf-8

# ### Calculating Column Statistics
# Aggregate functions summarize many data points (i.e., a column of a dataframe) into a smaller set of values.

# The general syntax for these calculations is:
# 
# ##### df.column_name.command()

# The following table summarizes some common commands:

# In[2]:


import pandas as pd

df= pd.DataFrame([
    ['mean',	'Average of all values in column'],
    ['std',	'Standard deviation'],
    ['median',	'Median'],
    ['max',	'Maximum value in column'],
    ['min',	'Minimum value in column'],
    ['count',	'Number of values in column'],
    ['nunique',	'Number of unique values in column'],
    ['unique',	'List of unique values in column']
    
],
    columns = ['Command',	'Description'],
    
)

df



# In[6]:


# Creating our inventory table

inventory = pd.DataFrame([
    
['Staten Island','seeds','daisy',4,6.99],
['Staten Island','seeds','calla lily',46,19.99],
['Staten Island','seeds','tomato',85,13.99],
['Staten Island','garden tools','rake',4,13.99],
['Staten Island','garden tools','wheelbarrow',0,89.99],
['Staten Island','garden tools','spade',93,19.99],
['Staten Island','pest_control','insect killer',74,12.99],
['Staten Island','pest_control','weed killer',8,23.99],
['Staten Island','planter','20 inch terracotta planter',0,17.99],
['Staten Island','planter','8 inch plastic planter',53,3.99],
['Brooklyn','seeds','daisy',50,6.99],
['Brooklyn','seeds','calla lily',0,19.99],
['Brooklyn','seeds','tomato',0,13.99],
['Brooklyn','garden tools','rake',15,13.99],
['Brooklyn','garden tools','wheelbarrow',82,89.99],
['Brooklyn','garden tools','spade',36,19.99],
['Brooklyn','pest_control','insect killer',80,12.99],
['Brooklyn','pest_control','weed killer',76,23.99],
['Brooklyn','planter','20 inch terracotta planter',5,17.99],
['Brooklyn','planter','8 inch plastic planter',26,3.99],
['Queens','seeds','daisy',57,6.99],
['Queens','seeds','calla lily',95,19.99],
['Queens','seeds','tomato',45,13.99],
['Queens','garden tools','rake',21,13.99],
['Queens','garden tools','wheelbarrow',98,89.99],
['Queens','garden tools','spade',26,19.99],
['Queens','pest_control','insect killer',0,12.99],
['Queens','pest_control','weed killer',16,23.99],
['Queens','planter','20 inch terracotta planter',87,97.99] 
], 
 columns = ['location','product_type','product_description','quantity','price'],
    
)


# In[4]:


# displaying the first 10 rows

inventory.head(10)


# Our finance department wants to know the price of the most expensive product purchased. Save your answer to the variable most_expensive.

# In[8]:


# most expensive product

most_expensive = inventory.price.max()
most_expensive


# Our sales department wants to know how many different product types we are selling. Save your answer to the variable num_type.

# In[9]:


num_type = inventory.product_type.nunique()
num_type


# ### Calculating Aggregate Functions

# When we have a bunch of data, we often want to calculate aggregate statistics (mean, standard deviation, median, percentiles, etc.) over certain subsets of the data.

# In general, we use the following syntax to calculate aggregates:
# 
# ##### df.groupby('column1').column2.measurement()

# column1 is the column that we want to group by

# column2 is the column that we want to perform a measurement on

# measurement is the measurement function we want to apply

# #### example

# previously, our finance department wanted to know the most expensive product that we sold.
# Now, they want to know the most expensive product for each product_type (i.e., the most expensive seeds, the most expensive garden tools, etc.).
# 
# Save your answer to the variable pricey_product.
# 

# In[21]:


pricey_product = inventory.groupby('product_type').price.max()

pricey_product


# What type of object is pricey_product?

# In[16]:


# object type

print(type(pricey_product))


# After using groupby, we often need to clean our resulting data.

# The groupby function creates a new Series, not a DataFrame.

# For our inventory example, the indices of the Series were different values of product_type, and the name property was price.

# Usually, we’d prefer that those indices were actually a column. In order to get that, we can use reset_index(). This will transform our Series into a DataFrame and move the indices into their own column.
# 
# Generally, a groupby statement is followed by reset_index:
# 
# ##### df.groupby('column1').column2.measurement().reset_index()

# ##### example 

# Modify your code above so that it ends with reset_index, which will change pricey_product into a DataFrame.

# In[20]:


# change pricey_product into a DataFrame

pricey_product = inventory.groupby('product_type').price.max().reset_index()

pricey_product


# Now, what type of object is pricey_product?

# In[19]:


# object type

print(type(pricey_product))


# Sometimes, the operation that you want to perform is more complicated than mean or count. In those cases, you can use the apply method and lambda functions, just like we do for individual column operations. Note that the input to our lambda function will always be a list of values.
# 
# A great example of this is calculating percentiles.

# ##### example 

# Our Marketing team says that it’s important to have some affordably priced products available for every type of product that we sell.

# Let’s calculate the 25th percentile for product price for each product_type to help Marketing decide if we have enough cheap products on sale. Save the data to the variable cheap_products.

# In[25]:


import numpy as np
cheap_products = inventory.groupby('product_type').price.apply(lambda x:np.percentile(x,25)).reset_index()
cheap_products 


# Sometimes, we want to group by more than one column. We can easily do this by passing a list of column names into the groupby method.

# From our inventory, our Purchasing team thinks that certain product_types are particularly popular in certain locations.
# 
# Create a DataFrame with the total quantity of products of each locattion/product_type combination purchased. Perform the calculation on the product_description column. Save it to the variable product_counts.

# You should be able to do this using groupby and count().
# 
# Note: When we’re using count(), it doesn’t really matter which column we perform the calculation on.
#     
# Remember to use reset_index() at the end of your code!

# In[31]:


# DataFrame with the total quantity of products of each product_type/product_description combination purchased

product_counts = inventory.groupby(['location', 'product_type'])['product_description'].count().reset_index()

product_counts


# ### Pivot Tables

# When we perform a groupby across multiple columns, we often want to change how our data is stored.

# Reorganizing a table to make it easier to test our hypothesis is called pivoting.The new table is called a pivot table.

# In Pandas, the command for pivot is:

# ##### df.pivot(columns='ColumnToPivot', index='ColumnToBeRows',values='ColumnToBeValues')

# In[33]:


# First use the groupby statement:

product_counts = inventory.groupby(['location', 'product_type'])['product_description'].count().reset_index()

product_counts


# In[40]:


# Now pivot the table. 
#Just like with groupby, the output of a pivot command is a new DataFrame.
# But the indexing tends to be “weird”, so we usually follow up with .reset_index().

pivoted = product_counts.pivot(columns = 'product_type', index = 'location', values = 'product_description').reset_index()

pivoted


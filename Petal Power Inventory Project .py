#!/usr/bin/env python
# coding: utf-8

# You’re the lead data analyst for a chain of gardening stores called Petal Power. Help them analyze their inventory!

# In[2]:


# Data for all of the locations of Petal Power is in the file inventory.csv. 
# Create the data into a DataFrame called inventory.


# In[1]:


import pandas as pd

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
['Queens','planter','20 inch terracotta planter',87,17.99] 
], 
 columns = ['location','product_type','product_description','quantity','price'] 
    
)


# In[2]:


# Inspect the first 10 rows of inventory.

print(inventory.head(10))


# The first 10 rows represent data from your Staten Island location. Select these rows and save them to staten_island.

# In[5]:


# Select these rows and save them to staten_island

staten_island = inventory.head(10)


# A customer just emailed you asking what products are sold at your Staten Island location. Select the column product_description from staten_island and save it to the variable product_request.

# In[7]:


# Select the column product_description from staten_island and save it to the variable product_request

product_request = staten_island.product_description


# Another customer emails to ask what types of seeds are sold at the Brooklyn location.
# 
# Select all rows where location is equal to Brooklyn and product_type is equal to seeds and save them to the variable seed_request.

# In[19]:


seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]

print(seed_request)


# Add a column to inventory called in_stock which is True if quantity is greater than 0 and False if quantity equals 0.

# In[22]:


# Add a column to inventory called in_stock which is True if quantity is greater than 0 and False if quantity equals 0.

inventory['in_stock'] = inventory.apply(lambda row: 'True' if row.quantity > 0 else 'False', axis=1)
print(inventory.head(10))


# Petal Power wants to know how valuable their current inventory is.
# 
# Create a column called total_value that is equal to price multiplied by quantity.

# In[23]:


# Create a column called total_value that is equal to price multiplied by quantity

inventory['total_value'] = inventory.apply(lambda row: row.price * row.quantity, axis=1)
print(inventory.head(10))


# The Marketing department wants a complete description of each product for their catalog.
# 
# The following lambda function combines product_type and product_description into a single string:

# In[24]:


combine_lambda = lambda row:     '{} - {}'.format(row.product_type, row.product_description)


# Using combine_lambda, create a new column in inventory called full_description that has the complete description of each product.

# In[26]:


#  create a new column in inventory called full_description that has the complete description of each product

inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
print(inventory.head(10))


# In[ ]:





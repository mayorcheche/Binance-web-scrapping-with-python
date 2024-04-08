#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[7]:


url = 'https://www.binance.com/en-GB/markets/overview?p=1'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

print(soup)


# In[5]:





# In[ ]:





# In[9]:


##### i tried to locate the table i needed

table = soup.find('div', class_  = 'css-clre8k')


# In[118]:


##### i located the table title tag and named it 

table_title = soup.find_all('div', class_ ='whitespace-nowrap text-t-third')


# In[119]:


table_title


# In[ ]:





# In[120]:


##### i removed all the unwanted symbols and signs from the table headings

coin_table_title = [title.text.strip() for title in table_title]

print(coin_table_title)


# In[ ]:





# In[123]:


#### i located the row tag in the table

column_data = table.find_all('div', class_ = 'css-1ydqfmf', )


# In[ ]:





# In[133]:


#### i found a way to find the tag for each row data and inserted them in thier respective rows and columns

combined_data = []  # Initialize an empty list to store combined data for each row

for row in column_data:
    # Extract data for the first class 'css-1y4fqhd'
    row_data_1 = [data.text.strip() for data in row.find_all('div', class_='css-1y4fqhd')]
    
    # Extract data for the second class
    row_data_2 = [data.text.strip() for data in row.find_all('div', class_='body2 items-center css-18yakpx')]

      # Extract data for the third class
    row_data_3 = [data.text.strip() for data in row.find_all('div', class_='body2 css-191zdd8')]

  # Extract data for the fourth class
    row_data_4 = [data.text.strip() for data in row.find_all('div', class_='body2 text-t-primary css-18yakpx')]

    # Combine the extracted data into a single list for each row
    combined_row_data = row_data_1 + row_data_2 +  row_data_3 + row_data_4

    # Append the combined data for the row to the main list
    combined_data.append(combined_row_data)
    
  # Print or use the combined data as needed
for data in combined_data:
    print(data)



# In[ ]:





# In[134]:


import pandas as pd


# In[135]:


df = pd.DataFrame(combined_data, columns = coin_table_title)

df


# In[ ]:





# In[13]:


pip install nbconvert


# In[ ]:





# In[14]:


pip install nbconvert[webpdf]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





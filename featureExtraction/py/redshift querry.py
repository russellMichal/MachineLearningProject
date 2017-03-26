
# coding: utf-8

# In[1]:

import psycopg2
import pandas as pd
import time
import numpy as np


# In[2]:

#connect to Redshift (US-EAST-1) through psycopg2
conn = psycopg2.connect(
    host="d3s-stream.crwmixi2uq4g.us-east-1.redshift.amazonaws.com",
    user="rdii",
    port=5439,
    password='UIUCrdii5',
    dbname= 'streamd3s')


# In[ ]:

#Creat a cursor for executing queries
cur = conn.cursor()


# In[ ]:

# Database processing
query = 'SELECT * FROM redshift WHERE time > 1477517374-60*2'
query_max = 'SELECT MAX(time) FROM redshift;'
start_time = time.time()
data = pd.read_sql_query(query_max, conn)
time.time()-start_time
data.to_csv('temp.csv')


# In[ ]:

#Close the connection.
cur.close()
conn.close()


# In[4]:

#query all data in redshift and store as a pandas dataframe
query = 'SELECT * FROM redshift where time > 1488348000'
data = pd.read_sql_query(query, conn)


# In[6]:

data[1:]


# In[ ]:

#close connection
conn.close()


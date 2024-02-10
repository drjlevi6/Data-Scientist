#!/usr/bin/env python
# coding: utf-8

# ### Attempt to display .csv data

# In[62]:


import numpy as np
import matplotlib.pyplot as plt


# In[63]:


#get_ipython().system('pwd')


# In[64]:


ar = np.loadtxt("csv_file.csv", dtype='int', delimiter=',') # could also have been read as floats
ar


# In[66]:


plt.figure(figsize=(5,5))
plt.imshow(ar, cmap ='gray')
plt.show()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[25]:


'''Convert glucose levels from a screenshot to a comma-delimited string'''
'''
Convert the glucose levels to a comma-delimited string (adding  
screenshot's date) of integers to be incorporated into a CSV-formatted 
dataset, etc.
'''
None


# In[26]:


import os, re, sys
import pandas as pd
from pandas import DataFrame as DF, Series as Ser
import numpy as np
from matplotlib import pyplot as plt


# In[27]:


def get_image_path():
    '''Get path from user of image to be analyzed for glucose levels'''
    if len(sys.argv) == 2:  # using command line, user supplied path
        print(sys.argv[0] + ": Using file",sys.argv[1], file=sys.stderr)
        return sys.argv[1]
    elif len(sys.argv) > 2: # using notebook; prompt user for path
        print("Enter full or relative path of image to be analyzed:", file=sys.stderr)
        return input()
    else:                   # length == 1; command line w/o user-supplied path
        print(sys.argv[0] + ": Error:",
            "You must supply the path of the image file to be processed.",
            file=sys.stderr)
        quit()
#    return "./images/20240520-IMG_1973.PNG"
png_path = get_image_path()


# In[28]:


# Read the screenshot showing the monitor's glucose curve
from PIL import Image

png = np.asarray(Image.open(png_path))
csv_df = DF(png[:, :, 0])
csv_cropped = csv_df.iloc[508:1485, 88:748] # shape: (1015, 660)


# In[29]:


import numpy as np

# column_zeros_means is the mean height,in pixels, and for each 
# column, of the thick black line comprising the screenshot's graph.

shape0 = csv_cropped.shape[0]
column_zeros_means = Ser([])

for j_col in range(660):
    try:
        col_zeros = Ser([
            (i if csv_cropped.iloc[i,j_col] == 0 else np.nan)\
            for i in range(shape0)])
        column_zeros_means[j_col+1] = col_zeros.mean()
    except Exception:
        column_zeros_means[j_col+1] = np.nan
        
# get rid of nans
column_zeros_means.interpolate(inplace=True)

# Scale the column means from pixels to mg/Dl
mg_per_dl = (-0.34324 * column_zeros_means + 350).astype(int, errors='ignore')


# In[30]:


# Get date from screenshot; convert to string yyyymmdd
def get_screenshot_date(png_path):
    '''Extract, convert line containing date from screenshot text'''
    
    from pandas.io.clipboard import clipboard_get
    os.system("tesseract " + png_path + 
        " stdout --dpi 72 | sed -nE '/^<.*>$/p' | pbcopy")
    date_text_raw = clipboard_get()
    # convert date to eight-digit string
    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October","November", "December"]
    m = re.search("(\w+) (\d+),\ *(\d{4})", date_text_raw)
    month, day, year = m.group(1), int(m.group(2)), m.group(3)
    return f"{year:4s}{months.index(month)+1:02d}{day:02d}"


# In[31]:


comma_delimited = ','.join(np.char.mod('%d', mg_per_dl))


# In[32]:


# Prepend the date
comma_delimited = get_screenshot_date(png_path) + ',' + comma_delimited


# In[33]:


print(comma_delimited)


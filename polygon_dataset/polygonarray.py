#!/usr/bin/env python
# coding: utf-8

# In[1]:


from polygonsmall import PolygonSmall
import numpy as np
from matplotlib import pyplot as plt


# In[2]:


class PolygonArray():
    '''Array of polygons (PolygonSmall), plus array of their labels (nsides)'''
    def __init__(self, n):
        '''Create array "data" of n PolygonSmalls, plus array "labels" of n labels as above'''
        self.polys =  np.array([PolygonSmall() for i in range(n)])
        self.data = np.array([ps.img for ps in self.polys])
        self.labels = np.array([ps.nverts for ps in self.polys])
        self.n = n

    def show(self):
        fig, axs = plt.subplots(2, self.n, figsize=(9.5, 5), layout='tight')
        for i in range(self.n):
            ar.polys[i].draw(axs[0][i])
            ar.polys[i].draw_small(axs[1][i])
        plt.show()
        


# In[5]:


if __name__ == '__main__':
    ar = PolygonArray(4)
    ar.show()


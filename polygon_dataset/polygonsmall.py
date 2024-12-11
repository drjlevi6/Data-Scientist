#!/usr/bin/env python
# coding: utf-8

# In[1]:


import import_ipynb
#from polygon_dataset.polygon import Polygon
from polygon import Polygon
import numpy as np
from matplotlib import pyplot as plt


# In[2]:


class PolygonSmall(Polygon):
#    from polygon_dataset.polygon import Polygon
    from polygon import Polygon
    """A polygon made by setting the points of a self.edge x self.edge array"""
    
    def __init__(self):
        Polygon.__init__(self)
        self.edge = 50
        self.X_t = np.array([self.map_coords(x) for x in self.X])
        self.Y_t = np.array([int((self.edge-1) * (2-y)/4) for y in self.Y])
        self.img = np.ones([self.edge, self.edge])
       
        self.set_edges()
        self.set_vertices()

    def set_edges(self):
        '''draw the PolygonSmall's edges in its img'''
        for i0 in range(self.nverts):
            i1 = (i0+1) % self.nverts
            ex0, ex1, ey0, ey1 = self.X_t[i0], self.X_t[i1], \
                self.Y_t[i0], self.Y_t[i1]
            self.set_one_edge(ex0, ex1, ey0, ey1)

    def set_vertices(self): # put large dots representing vertices into self.img
        for i in range(self.nverts):
            x0 = self.X_t[i]
            y0 = self.Y_t[i]
            self.img[y0-1][x0-1] = self.img[y0-1][x0] = self.img[y0-1][x0+1] = 0
            self.img[y0][x0-1] = self.img[y0][x0] = self.img[y0][x0+1] = 0
            self.img[y0+1][x0-1] = self.img[y0+1][x0] = self.img[y0+1][x0+1] = 0

    def set_one_edge(self, ex0, ex1, ey0, ey1):
        """Need to consider whether 1) edge is vertical; 2) slope <= 1; 3) slope > 1"""
        #ex1 = ex0 # force vertical line
        if ex0 == ex1:
            xy_ranges = range((max(ey0, ey1)+1) - min(ey0, ey1))
            edges_x = [ex0 for i in xy_ranges] # coords of edge dots, y
            edges_y = [ey0 + i * np.sign(ey1-ey0) for i in xy_ranges] # coords of edge dots, y
        elif abs(ey1-ey0) / abs(ex1-ex0) > 1:
            xy_ranges = range((max(ey0, ey1)+1) - min(ey0, ey1))
            edges_y = [int(ey0 + (i * abs(ey1-ey0) / (ey1-ey0))) for i in xy_ranges] # coords of edge dots, y
            edges_x = [int(ex0 + (i * (ex1-ex0) / xy_ranges[-1])) for i in xy_ranges] # coords of edge dots, x            
        else:
            xy_ranges = range((max(ex0, ex1)+1) - min(ex0, ex1))
            edges_x = [int(ex0 + (i * abs(ex1-ex0) / (ex1-ex0))) for i in xy_ranges] # coords of edge dots, x
            edges_y = [int(ey0 + (i * (ey1-ey0) / xy_ranges[-1])) for i in xy_ranges] # coords of edge dots, y
        for i in range(len(edges_x)):
            self.img[edges_y[i]][edges_x[i]] = 0.5

    def draw_small(self, ax=None):
        if ax == None:
            fig = plt.figure()
            plt.grid()
            plt.imshow(self.img, cmap='gray')
            plt.show()
        else:
            ax.grid()
            ax.imshow(self.img, cmap='gray')
    def map_coords(self, x):
        """transfrom X- or Y-value linearly from super's [-halfedge, halfedge] to [0, self.edge-1]"""
        return int(x * (self.edge-1)/self.halfedge/2 + (self.edge-1)/2)


# In[6]:


if __name__ == '__main__':
    print(__name__)
    ps = PolygonSmall()
    print(ps.__dir__())


# In[ ]:





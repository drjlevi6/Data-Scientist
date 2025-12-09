#!/usr/bin/env python
# coding: utf-8

# # Generate random polygons
# 
# Generate a table whose samples are the vertices of randomly-generated polygons.
# The polygons have 3 through 8 sides, are contained in the square [-2, 2] x 
# [-2, 2], and have center (0, 0).

# In[1]:


import numpy as np
import pandas as pd
from pandas import DataFrame as DF, Series as Ser
import matplotlib.pyplot as plt
import random
from PIL import Image


# In[5]:


class Polygon():
    """A randomly generated polygon with 3 to 8 sides"""
    global g_halfedge
    g_halfedge = 2
    my_dpi = 144
    
    def __init__(self):
        """Generate the polygon's values immediately"""
        """ We start with the vertices in polar coordinates because
            it's conceptually simpler, but we subsequently convert to 
            Cartesian coordinates for drawing
        """
        self.halfedge = g_halfedge
        self.nverts = random.randint(3, 8) # number of vertices
                                           # this _does_ include the final 8
        ns = self.nverts                   # for convenience

        # Advance angle by at least d_theta_min with every vertex
        # (This def looks like final angles may be > 2pi, but they aren't!)
        self.d_theta_min = 2 * np.pi / ns
        th_min = self.d_theta_min          # for convenience
        self.base_angles = th_min * np.arange(0, ns)
        
        # Set vertices' angles: add random element to const. baseline
        self.angle_deltas = np.array(np.random.random(ns))
        self.angles = self.base_angles + (th_min * self.angle_deltas)

        # Set vertices' radii
        rng = np.random.default_rng()
        self.radii =  0.5 * rng.random(ns) + 0.75 # ensure 1 <= radii < 1.5

        # Convert to Cartesian coordinates
        self.X = self.radii * np.cos(self.angles)
        self.Y = self.radii * np.sin(self.angles)

    def draw(self, ax=None):
        import matplotlib as mpl

        """Draw the polygon"""
        """ draw() may be called by an outside function, if we're drawing
            multiple polygons; then the outside function supplies the Axes.
        """
        ax_ori = ax
        if ax_ori == None:
            fig = plt.figure()
            ax = plt.gca()

        X, Y = self.X, self.Y

        poly_color = '#808080'
        ax.set_xlim(-g_halfedge, g_halfedge)
        ax.set_ylim(-g_halfedge, g_halfedge)
        ax.plot(X, Y, color=poly_color)
        ax.plot([X[-1], X[0]], [Y[-1], Y[0]], color=poly_color, zorder=1)

        # draw vertices
        ax.scatter(X, Y, color='black', marker='s', zorder=2)
            
        # Add vertex numbers
        text_label_pad = 0.4   # add distance betw vertex and number
        for i in range(self.nverts):
            text_x = (self.radii[i] + text_label_pad) * np.cos(self.angles[i])
            text_y = (self.radii[i] + text_label_pad) * np.sin(self.angles[i])
            ax.text(text_x, text_y, str(i+1), fontsize=14, color='#404040',
                verticalalignment='center', horizontalalignment='center')
        if ax_ori == None:
            plt.show()

    def write_csv(self):
        """convert polygon's X, Y-values to comma-delimited values, zero-padded to 16 fields as needed"""
        csv = ""
        def add_x_or_y(xy, csv):
            for i in range(len(xy)):
                csv += f"{xy[i]:0.2f}" + ','
            return csv[1:]
            
        csv = add_x_or_y(self.X, csv)
        csv = add_x_or_y(self.Y, csv)

        if self.nverts < 8:
            csv += '0,' * 2 * (8-self.nverts)
        
        return csv[:-1]

    def to_numpy(self):
        return np.concatenate((self.X, self.Y, np.zeros(16-2*self.nverts)))


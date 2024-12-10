# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Show plot of four days' glucose levels, plus their original images

# +
import numpy as np
import pandas as pd
import matplotlib as mpl
from pandas import DataFrame as DF, Series as Ser
from matplotlib import pyplot as plt


# -

def display_or_print(data):
    '''Use print() instead of display(), in particular if running this as a module'''
    import sys
    try:
        display(data)
    except Exception:
        print("demo-glucose-plotter: using print() instad of display().", file=sys.stderr)
        print(data)


def png_to_csv(screenshot_path):
    '''Read screenshot of CGM, convert to numpy array'''
    from PIL import Image
    png = np.asarray(Image.open(screenshot_path))
    return png


def date_with_hyphens(yyyymmdd):
    ''' insert hyphens in a date string of form yyyymmdd'''
    import re
    hyphenated = re.sub(r'^(\d{4})(\d{2})(\d{2})$', r'\1-\2-\3', str(yyyymmdd))
    assert (hyphenated != yyyymmdd), "date_with_hyphens(): Invalid date string"
    return hyphenated


path = "/Users/jonathan/site-packages/glucose_management/all-glucose-values-sorted.csv"
screenshot_paths = [
    "./images/20240523-IMG_1970.PNG",
    "./images/20240524-IMG_1969.PNG",
    "./images/20240525-IMG_1968.PNG"
]
data = pd.read_csv(path)
data.columns = ["Date" ] + ["C" + str(i+1) for i in range(data.shape[1]-1)]
pd.set_option('display.max_rows', 6)
display_or_print(data)

# +
# Eventually, get start/end dates from user; create slice of data using the dates' indices
start_date, end_date = 20240523, 20240525 # ignore last date; need function to get these dates

data_dates = list(data["Date"])
# print(data_dates) # [20240329, 20240330, 20240331, 20240401, 
#    20240402, 20240403, 20240404, 20240405, 20240406, 20240407, 
#    20240408, 20240517, 20240518, 20240519, 20240520, 20240521, 
#    20240523, 20240524, 20240525, 20240526, 20240527]

start_index, end_index = (data_dates.index(start_date), \
        data_dates.index(end_date) + 1) # add 1 or iloc won't include last row
data_slice = data.iloc[start_index:end_index, :].copy()

data_2 = DF(data_slice.iloc[:, 1:])
data_2t = data_2.T
hours_even = ["12 AM"] + [str(i) + " AM" for i in range(2, 12, 2)] + \
    ["12 PM"] + [str(i) + " PM" for i in range(2, 12, 2)] + ["12 AM"]

print("Dates:", list(data_slice["Date"]))
display_or_print(data_2t.iloc[[0, 1, -2, -1], :])

# +
# Use GridSpec:
# Modified from https://matplotlib.org/stable/gallery/subplots_axes_and_figures/
# gridspec_multicolumn.html#sphx-glr-gallery-subplots-axes-and-figures-gridspec-multicolumn-py
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.pyplot import imshow
'''
class matplotlib.gridspec.GridSpec(nrows, ncols, figure=None, left=None, 
bottom=None, right=None, top=None, wspace=None, hspace=None, width_ratios=None, 
height_ratios=None)

matplotlib.pyplot.imshow(X, cmap=None, norm=None, *, aspect=None, 
interpolation=None, alpha=None, vmin=None, vmax=None, origin=None, extent=None, 
interpolation_stage=None, filternorm=True, filterrad=4.0, resample=None, 
url=None, data=None, **kwargs)
'''

def show_grid_items(fig):
    for i, ax in enumerate(fig.axes):
        if (i, ax) == (3, ax4):
            ax.plot(data_2t, linewidth=3)
            ax.legend(data_slice["Date"])
            ax.grid(color='black', alpha=0.25)
            ax.set_xticks(ticks=np.linspace(1, 660, len(hours_even)), labels=hours_even,
              fontsize=8, fontweight='bold')
            ax.set_xlabel("Time of Day", fontweight='bold', fontsize=10)
            ax.set_ylabel("Glucose (mg/dL)", fontweight='bold', fontsize=12)
            ax.set_title("\nGlucose Levels by Date", fontsize=14, fontweight='bold')
#            ax.set_title("\nCollected Glucose Values, " + date_with_hyphens(start_date) + \
#                 " — " + date_with_hyphens(end_date), fontsize=14, fontweight='bold')

        else:
            ax.imshow(png_to_csv(screenshot_paths[i]))
            ax.tick_params(labelbottom=False, labelleft=False)

fig = plt.figure(figsize=(12, 12), layout="constrained")
gs = GridSpec(2, 3, figure=fig)
fig.suptitle("Glucose Levels From CGM Screenshots\n",
                            fontweight='bold', fontsize=18)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[0, 2])
ax4 = fig.add_subplot(gs[1, :])

show_grid_items(fig)
plt.savefig("Screenshots-plotted.png")
plt.show()

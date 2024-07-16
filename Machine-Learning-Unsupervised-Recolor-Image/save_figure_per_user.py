'''Save a matplotlib figure if user desires'''
from matplotlib import pyplot as plt
import numpy as np
from date_time_string import date_time_string
from pandas import DataFrame as DF, Series as Ser
import os

def save_figure_per_user(title="Image"):
	'''This function must be called while user is doing a pyplot command'''
	if input("Save image? ('' = No, ~'' = Yes): ") != '':
		savestring = title + '-' + date_time_string() + ".png"
		plt.savefig(savestring)
		print("Image saved in", savestring)
		os.system("open .")

# Just do a test pyplot if this module is called independently
if __name__ == "__main__":
	data_xy = np.arange(3)
	plt.scatter(data_xy, data_xy)
	plt.show()

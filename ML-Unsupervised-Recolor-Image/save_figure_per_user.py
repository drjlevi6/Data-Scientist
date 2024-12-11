'''Save a matplotlib figure if user desires'''
from matplotlib import pyplot as plt
import numpy as np
from date_time_string import date_time_string
from pandas import DataFrame as DF, Series as Ser
import os
import platform

def save_figure_per_user(title="Image"):
	'''This function must be called while user is doing a pyplot command'''
	
	# If computer' s Mac and browser is Chrome, activate browser first
	if platform.system() == 'Darwin':
		os.system("osascript  -e 'beep' 2>&1")
		os.system("osascript -e 'tell application \"Chrome\" to activate' ; \
			osascript -e 'delay 1'")
		os.system("sleep 1")
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

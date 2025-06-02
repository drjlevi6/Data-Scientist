"""Make a string consisting of today's 8-digit date, a hyphen, and a 6-digit time"""

def date_time_string():
	from datetime import date
	import time, re
	
	now = time.localtime()
	
	return f"{int(now.tm_year):4d}{int(now.tm_mon):02d}" + \
		f"{int(now.tm_mday):02d}" + \
		f"-{int(now.tm_hour):02d}{int(now.tm_min):02d}" + \
		f"{int(now.tm_sec):02d}"
	
if __name__ == "__main__":
	print(date_time_string())
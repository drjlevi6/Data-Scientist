'''Convert triplet of RGB integers (0-255) to 6-digit hex string preceded by "#"'''
def rgb_to_hex(rgb):
	return f"#{hex(rgb[0])[2:]:0>2}{hex(rgb[1])[2:]:0>2}{hex(rgb[2])[2:]:0>2}"
	
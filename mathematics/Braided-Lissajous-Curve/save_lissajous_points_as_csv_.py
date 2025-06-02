""" Print points of a Lissajous curve in format compatible with CSV."""

import math

def L(t):
	return [ math.sin(5 * math.pi * t), math.sin( 4 * math.pi * t) ]

def print_points(points):
	'''print header then numeric data, fields delimited by commas'''
	print(points[0])
	for i in range(1, len(points)):
		pstr = points[i]
		p = [float(pstr[0]), float(pstr[1]), float(pstr[2])]
		print(f'{p[0]:.5f},{p[1]:.5f},{p[2]:.5f}')
	
#  Main  ######################################################################
"""Computes, prints locations of (maxpoints) dots"""
points = ['t,Lx(t),Ly(t)']		# headers of csv table
maxpoints = 600					# no. points to be calculated

for i in range(maxpoints + 1):
	t = 2 * i / maxpoints
	LxT, LyT = L(t)
	points.append([ t, LxT, LyT ])

print_points(points)

#!/usr/bin/env python

from operator import itemgetter
import sys

current_key = None
min = 0
max = 0

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	row = line.split("\t")
	(key,value) = row

	try: 
		value = int(value)
	except ValueError:
		continue

	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reducer
	if current_key == key:
		if value > max:
			max = value
		if value < min:
			min = value
		else:
			min = min
			max = max
	else:
		if current_key:
	 		# write result to STDOUT
			print(current_key, min, max)
		current_key = key
		min = value
		max = value

#Last key
if current_key == key:
	print(current_key, min, max)

#!/usr/bin/env python

import sys
import datetime
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	rows = line.split(",")
	(name1,phone1,name2,phone2,timestamp_ms,timestamp_str,duration_m) = tuple(rows)
	#print(rows)
	# write the results to STDOUT (standard output);
	# what we output here will be the input for the
	# Reduce step, i.e. the input for reducer.py
	try: 
		print('{}\t{}'.format(datetime.datetime.strptime(timestamp_str[:10], '%Y-%m-%d').strftime("%A"), int(duration_m)))
	except ValueError as e:
		continue

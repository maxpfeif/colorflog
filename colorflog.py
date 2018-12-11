#	Authored: Max Pfeiffer - 2018
#
#	Takes a passed .csv file with a CAN or LIN log in the "Time, ID, .." format 
# 	and applies a chromatic highlight to each row based on the ID. T
#
#	Colorflog allows you to visually idnetify patterns in log data more easily. 
#
#	Usage: 	python colorflog.py "inputfilename" where inputfilename.csv is a file of
#		the apropriate format mentioned above. Note the omission of the file extension in the argument
#
#	Output: "filename.html" 
#		an html file that displays the row data in a spectrum of colors	that is automatically
#		adjusted to the range of input data 
#
#
#!/usr/bin/python
import sys
import csv

filename = sys.argv[1]

cfile = open(filename + ".html", 'w')
message = """<html>
<head></head>
<body>
<p>
"""
cfile.write(message)

#process the input file 
control = open(filename + ".csv")
in_file = csv.reader(control, delimiter = ",")
header = 1

#track file statistics 
id_list = []
rows = []

for row in in_file:
	if header:
		header = 0
		message = "<ul>" + str(row) + "</ul>" + "\n"
		cfile.write(message)
	else: 
		# now we need to parse through the entire infile and generate a list of the ids 
		rows.append(row)
		ident = row.pop(1)
		if ident not in id_list:
			id_list.append(int(ident, 16))	
		row.insert(1,ident)	

# get the max and min from the range 
# higher numbers = more red, lower numbers = more blue 
# now using the span and offset we can scale the 255 x 3 = 765 to this. 
sf = 765 / float((int(max(id_list)) - int(min(id_list)))) 

for row in rows:
	row_data = list(row)
	ident = int(row.pop(1), 16)
	#srow_data.insert(1,ident)
	color = int ((ident - int(min(id_list))) * sf)
	hex_check = 0
	# classify the color 
	if color > 510: 
		style = color - 510
		hex_check = style
		style = list(hex(style))
		style.pop(0)
		style.pop(0)
		if(hex_check > 15):
			style = "#" + style.pop(0) + style.pop(0) + "0000"
		else: 
			style = "#0" + style.pop(0) + "0000"
	elif color > 255:
		style = color - 255 
		hex_check = style
		style = list(hex(style))
		style.pop(0)
		style.pop(0)

		if(hex_check > 15):
			style = "#00" + style.pop(0) + style.pop(0) + "00"
		else: 
			style = "#000" + style.pop(0) + "00"			
	else: 
		style = list(hex(color))
		hex_check = color
		style.pop(0)
		style.pop(0)
		if(hex_check > 15):
			style = "#0000" + style.pop(0) + style.pop(0)
		else: 
			style = "#00000" + style.pop(0)
	
	time = str(row_data.pop(0))
	ident = str(row_data.pop(0))
	data = row_data.pop(0)
	message = "<ul style=\"color:" + style + ";\">" + time + ", " +  ident + ", " + data + "</ul>" + "\n"
	cfile.write(message)


message = """
</p>
</body>
</html>
"""
cfile.write(message)
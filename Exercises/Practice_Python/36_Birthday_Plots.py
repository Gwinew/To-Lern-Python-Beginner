"""
In the previous exercise we counted how many birthdays
there are in each month in our dictionary of birthdays.

In this exercise, use the bokeh Python library to plot
a histogram of which months the scientists have birthdays in!
Because it would take a long time for you to input the months of various scientists,
you can use my scientist birthday JSON file.
Just parse out the months (if you don’t know how,
I suggest looking at the previous exercise or its solution) and draw your histogram.

If you are using a purely web-based interface for coding,
this exercise won’t work for you, since it requires installing the bokeh Python package.
Now might be a good time to install Python on your own computer.
"""

from collections import Counter

import json

from bokeh.plotting import figure, show, output_file


def number_of_month(name_dict):
	take_value = list(name_dict.values())
	count_of_value = len(take_value)
	for i in range(count_of_value):
		take_value[i] = take_value[i][:2]
	return take_value, count_of_value

def name_of_month(take_value, count_of_value):
	months_name = []
	for i in range(count_of_value):
		if take_value[i] == '01':
			months_name.append("January")
		elif take_value[i] == '02':
			months_name.append("February")
		elif take_value[i] == '03':
			months_name.append("March")
		elif take_value[i] == '04':
			months_name.append("April")
		elif take_value[i] == '05':
			months_name.append("May")
		elif take_value[i] == '06':
			months_name.append("June")
		elif take_value[i] == '07':
			months_name.append("July")
		elif take_value[i] == '08':
			months_name.append("August")
		elif take_value[i] == '09':
			months_name.append("September")
		elif take_value[i] == '10':
			months_name.append("October")
		elif take_value[i] == '11':
			months_name.append("November")
		elif take_value[i] == '12':
			months_name.append("December")
		else:
			months_name.append("No Month")
	return months_name


with open('info.json', 'r') as f:
	name_dict = json.load(f)

first_select = number_of_month(name_dict)
second_select = name_of_month(first_select[0], first_select[1])
count_dict = Counter(second_select)

output_file('plot_birth.html')
x_categories = ['January', 'February', 'March', 'April',
'May', 'June', 'July', 'August', 'September', 'October',
'November', 'December']
x = list(count_dict.keys())
y = list(count_dict.values())
p = figure(x_range=x_categories)
p.vbar(x=x, top=y, width=0.5, color='firebrick')
p.xaxis.major_label_orientation = 1
show(p)

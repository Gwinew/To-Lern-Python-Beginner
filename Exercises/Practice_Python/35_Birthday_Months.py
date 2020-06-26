"""
In the previous exercise we saved information
about famous scientists’ names and birthdays to disk.
In this exercise, load that JSON file from disk,
extract the months of all the birthdays,
and count how many scientists have a birthday in each month.

Your program should output something like:

{
	"May": 3,
	"November": 2,
	"December": 1
}
"""
from collections import Counter

import json


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

print(count_dict)

'''
Given a .txt file that has a list of a bunch on names, count how many
of each name there are in the file, and print out the results to the screen.
I have a .txt file for you, if you want to use it!

Extra:
    - Instead of using the .txt file from above (or instead of, if you want the challenge),
    take this .txt file, and count how many of each 'category' of each
    image there are. This text file is actually a list of files corresponding
    to the SUN database scene recognition database, and lists the file directiory
    hierarchy for the images. Once you take a look at the first line or two
    of the file, it will be clear which part represents the scene category.
    To do this, you're going to have to remember a biet about string parsing in
    Python 3. I talked a little bit about it in this post.
'''
from pprint import pprint as pp


with open('names.txt', 'r') as f:
    all_text = f.read()
list_of_names = all_text.strip().split('\n')
list_from_set_of_names = list(set(list_of_names))
count_list_of_names = {}
for i in range(len(list_from_set_of_names)):
#    count_list_of_names.append((list_from_set_of_names[i], list_of_names.count(list_from_set_of_names[i])))
    count_list_of_names[list_from_set_of_names[i]]=list_of_names.count(list_from_set_of_names[i])
for j, k in count_list_of_names.items():
    print(f'{j} is {k}')


with open('list_of_pictures.txt', 'r') as g:
    texts = g.read()

list_of_nam = texts.split('\n')
catalogs = []
for i in list_of_nam:
    a = i.split('/')
    catalogs.append(a[len(a)-2])
count_list_of_catalogs = {}
set_of_catalogs = list(set(catalogs))
for i in range(len(set_of_catalogs)):
    count_list_of_catalogs[set_of_catalogs[i]]=catalogs.count(set_of_catalogs[i])
for j, k in count_list_of_catalogs.items():
    pp(f'{j} is {k}')

counter_dict = {}
with open('names.txt') as f:
	line = f.readline()
	while line:
		line = line.strip()
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)

counter_dict = {}
with open('list_of_pictures.txt') as f:
	line = f.readline()
	while line:
		line = line[3:-26]
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)

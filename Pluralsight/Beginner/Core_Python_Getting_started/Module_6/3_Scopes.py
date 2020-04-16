# Scopes in Python:

# - Local - Inside the current function
# - Enclosing - Inside enclosing functions
# - Global - At the top level of the module
# - Built-in - In The special builtins module

# import sys                            # sys - G
# from urllib.request import urlopen    # urlopen - G

# def fetch_words(url):                 # fetch_words - G, url - L
    
#    story = urlopen(url)               # story -L
#    story_words = []                   # story_words -L
#    for line in story:                 # line -L
#        line_words=line.decode('utf8').split()     # line_words -L
#        for word in line_words:                    # words -L
#            story_words.append(word)
#    story.close()
#    return story_words
#
# def print_items(items):               # print_items -G
#    for item in items:
#        print(item)
#
#
#
# def main(url):                         # main - G
#     words = fetch_words(url)
#     print_items(words)
#
#
# if __name__ == '__main__':             # __name__ - G
#    main(sys.argv[1])
#
#
# Rebinding Global Names
count = 0
def show_count():
    print(count)

def set_count(c):
    count =c

show_count()        # result 0
set_count(5)
show_count()        # result 0 because any value is changing to 0 by the global values.

# We want to change this:

def set_count(c):
    global count
    count = c

show_count()        # result 0
set_count(5)
show_count()        # result 5

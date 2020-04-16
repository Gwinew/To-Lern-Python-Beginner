# Argument passing:

m= [9,15,24]
def modify(k):
    k.append(39)
    print('k=',k)
modify(m)       # This is work like print() after definition
print(m)        # The same value


# Replacing Argument Value:

f = [14,23,37]
def replace(g):
    g=[17,28,48]
    print('g =',g)

replace(f)      # 17,28,48
print(f)        # 14,23,37


# Mutable arguments:

def replace_contents(g):
    g[0] = 17
    g[1] = 28
    g[2] = 45
    print('g=',g)
f=[14,23,37]
replace_contents(f)     # 17,28,45
print(f)                # 17,28,48

# Return Semantics:

def f(d):
    return d
c=[6,10,1]
e=f(c)
print(c is e)

####################

# Defaul argument values:

def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)
banner("norwegian blue")
banner("Sun, Moon and Stars","*")
banner("Sun, Moon and Stars",border="*")
banner(border=".",message="Hello from hell")    # If we definined a value with specify argument then it is return a direction value without mistakes.

# Default Value Evaluation:
import time
print(time.ctime())

def show_default(arg=time.ctime()):
    print(arg)
show_default()

# - Remember That def is a statement executed at runtime.
# - Default arguments are evaluated when def is executed.
# - Immutable default values don't cause problems.
# - Mutable default values can cause confusing effects.

# Mutable Default Values:

def add_spam(menu=[]):
    menu.append("spam")
    return menu                 # If def doesn't print() than this definition don't show a returns, but when we use this definition in command line than it show a result.
breakfast = ['bacon','eggs']
print(add_spam(breakfast))
lunch=['baked beans']
print(add_spam(lunch))
print(add_spam(lunch))

# Immutable Default Value:

def add_spam(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu
print(add_spam())
print(add_spam())

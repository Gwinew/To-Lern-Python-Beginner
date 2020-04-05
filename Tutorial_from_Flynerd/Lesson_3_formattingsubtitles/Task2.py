# -*- coding: utf-8 -*-
#
# Create a investment script which will have information about:
# -Inital account status
# -Annual interest rate
# -The number of years in the deposit
#
# Result show using any formatting text.
#
enter=input("Hi! This is Investment script.\nI want to help you to count your money impact at the end of the deposit.\nPlease press \"Enter\" to continue")
name=input("Before we start, I would like to ask you, what\'s your name?\n")
rate=float(input("Hi {}. Write what interest rate you want to have. (in percentage)\n".format(name)))
inpu=float(input("Can you input initial account status? (in PLN)\n"))
time=int(input("Please enter, how long you want to keep your money in deposit? (in month)\n"))
ratep=rate/100
year=time/12
end=(inpu*time*ratep/12)+inpu
print("{} you will have {:.4f} PLN after {} months ({:.1f} years) in deposit".format(name,end,time,year))

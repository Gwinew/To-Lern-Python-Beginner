#First fun with the console
#The fundamental matematical operations is operations with (Int)eger and (Float)ing-point arithmetic
#Int example is 3+3 and the sum is 6, this is simple
#Float example is 8*3.5 and the sum is 28.0, even if we multiply float with float and the sum goes integer, the result is still float.
#Another way to save type of date is create (str)ing's. Str is tradicionally a sequence of characters and we can run what put the word between quotation marks (' or ").
#For example "Hello again", but this is the same type of writing like 'Hello again'.
#"..." is the same '...'
print("Int & str")
x=3+3 #This is Int - Important: We can using x or whatever we can imagion to save notice like x=y=z=Defxcve=Important
print("3+3="+str(x))    #This is Str

print()

#We can't write print("3+3="+x) because x is int not a str. That's why we change int to str by str(x).
#If we have possibility change str to int (for example x='3'), we can use int(x)
print("Str & int")
x='3'   #This is Str
y=int(x)+3  #This is Int
print(y)    #Int

print()

#We can write abbreviations of mathematical (and language) expressions using for exmaple y=.
print("Str")
y='We can fly away'
print(y)
print("We can fly away again")

print()

print("+ and ,")
print("We"+"can"+"fly"+"away")
print("We","can","fly","away")
#As can you see, another method of writing gives a different result.
#Signs '+' and ',' are add next individual data one by one, but "+" don't see empty space between data, the opposite is ',', where give next data with one empty space between.
print("We"+" can "+"fly "+"away"+" again")


#Special signs

#We can add special signs using "\". In python we have:
#\n - sign a new line, add "enter"
#\t - add tab
#\' - add apostrophe
#\" - add quotation marks
#\\ - add slash
print()
#\n example
print("\\n example")
print("We are\n","legion")  #When after entering data after "," we get a return data with empty space at the begining 
print("We are \n legion")   #The same result (but no, but more on that later) like before but with another notation
#They look similar, but unfortunately they are not the same. In second example is empty space after the last word in first line.
print()
    # The different way to notation the same result. But not necessarily...
print("We are","\nlegion")  #Have empty space after the last word in first line
print("We are\nlegion") #Don't have empty space
print("We are \nlegion")    #Have empty space after the last word in first line
    # A few example...maybe one
print("\n"+"After")
print("Before","\n","After")    #Have empty space before "Before" and after "After"
print("Befote"+"\n"+"After")

print()

print("\\t example")
#\t example
print("\tTabular expexticus")
print("\t Tabular expexticus")  #Have empty space between tab and firs sentence
print("Tabular\n\tWhy\n\tExpexticus")
print("Tabular","\n"+"\t"+"After")  #Have empty space after first sentence

print()

print("\\' example")    #It's necessary remember "..." and '...' is the same, but we can use "...'..." or '..."...'
#\' exmaple
print("Don't")
print("Don\'t")
print('Don\'t')

print()
#\" example
print("\\\" example") #This is funny :P
print("I said:\n\"No more!\"")
print("I said:\n"+"\"No more!\"")
print("\"+\" isn\'t \",\"")

print()
#\\ example
print("\\\\ example")
print("3\\3=1") # this is no true, because \ is not / ;)
print("\\Say whaaat?")

print()
#PS. Fundamental algebra equuations is +,-,*,**,/ and %(this is modulo)


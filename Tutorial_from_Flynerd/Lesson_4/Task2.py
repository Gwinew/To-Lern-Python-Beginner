# Make a list with serial movie
#
# Every serial movie should have assigned rate in scale 1-10.
# Asking users what they serial movie want to see.
# In answer give they rate value.
# Asking user if they want to add another serial movie and rate.
# Add new serial movie to the list.

# -*- coding: utf-8 -*-

dictserial={"Soprano":6,"Dark":9,"Rick and Morty":8}
listserial=list(dictserial.keys())
name=input("Hi! Welcome to serial movie data base.\n{}\nWhat serial movie want to see?\n".format(listserial))
enter=input("{} have {} in rating.\nPress Enter to continue".format(name, dictserial[name]))
newserial=input("If you want to add a new serial to the list, write the name\n")
newserialrate=input("Write a rate\n")
dictserial[newserial]=newserialrate
print("This is a new list with rates:\n{}".format(dictserial))

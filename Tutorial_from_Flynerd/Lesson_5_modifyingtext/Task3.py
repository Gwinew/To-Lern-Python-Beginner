# DNA Analize
#
# We have code DNA with Adenine (A), Cytosine (C), Guanine (G) and Thymine (T).
# Perfect code is looking on:
# TGCACGATCATGTCTACTATCCTCTCTATGGTGGGGTT
#
# Sometimes codes have lowerletter and upperletter. Another problem is sequence machine, it isn't free for error. Depend from machine, sequence errors have change to sign "-" or "N".
#
# In which way you recognize thaht your code DNA have errors?
#
# You have code in "DNA.txt."
#
# Count how many times is exist all nitrogen-containing nuclebases (A, C, G, T).
#
# From documentation we know if we have "-" that we have missing information - bad cell. If we have "N" that the next sign is correct value.
#
# 1. Count "GAGA" and change to "AGAG".
# 2. Find index in sign chain where is 7 G close to each other.
# 3. Find index from ending where is 6 C
# 4. How many times is show sequence "CTGAAA"
# 5. Sometimes in "CTGAAA" sequence the last value "A" is mutating. How many time is show this sequence if the last "A" is equivocal?
# 6. Clen DNA from all errors. From clear DNA create RNA - RNA in place thymins have Uracyl (U).
#
DNA=open("DNA.txt").read()
DNA=DNA.upper()
print("Adenina {}\nCytosine {}\nGuanine {}\nThymine {}".format(DNA.count("A"),DNA.count("C"),DNA.count("G"),DNA.count("T")))
# Ad.1
print("GAGA {}".format(DNA.count("GAGA")))
DNA=DNA.replace("GAGA","AGAG")
# Ad.2
print("GGGGGGG is in posion {}".format(DNA.find("GGGGGGG")))
# Ad.3
print("CCCCCC is in position {} from the ending".format(DNA.rfind("CCCCCC")))
# Ad.4
print("CTGAAA is {}".format(DNA.count("CTGAAA")))
# Ad.5
x=DNA.count("CTGAAA")+DNA.count("CTGAA-")+DNA.count("CTGAANA")
print("CTGAAA with equivocal \"A\" is {}".format(x))
# Ad.6
DNA=DNA.replace("-","")
DNA=DNA.replace("N","")
RNA=DNA.replace("T","U")
print(RNA)

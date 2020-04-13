# Make variable which have integer number and real number.
inscription="hello"
real=float(10)
integer=20
if inscription == "hello":
    print("Inscription: {}".format(inscription))
if isinstance(real,float) and real == 10.0:
    print("Real number: {}".format(real))
if isinstance(integer,int) and integer == 20:
    print("Integer number: {}".format(integer))

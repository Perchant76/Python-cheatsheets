import time
import math
from typing import Optional
# this will firstly apper on your screen and it will show how it works
io_or_2V = input("* (use: *)  or  ² (use: 2): ")
# if just first number is inserted and we want to do: ² or √
if io_or_2V == ("*"):
    first_number = input("Insert first number: ")
    if io_or_2V == ("2"):
        first_number1 = input("Insert number you want to exponent ")
# these are the functions that you can use when you used the * 1
if io_or_2V == ("*"):
    io = input("+,-,*,/")
# if just first number is inserted and we want to do: +,-,*,/
if io == ("+"):
    second_number = input("Insert third number: ")
elif io == ("-"):
    second_number = input("Insert third number: ")
elif io == ("*"):
    second_number = input("Insert third number: ")
elif io == ("/"):
    second_number = input("Insert third number: ")
# these are the functions that you can use when you used the * 2
if io_or_2V == ("*"):
    io1 = input("+,-,*,/")
# this is part when you can find if third number was or wasnt inserted
if io1 == ("+"):
    thirt_number = input("Insert third number: ")
elif io1 == ("-"):
    thirt_number = input("Instert third number: ")
elif io1 == ("*"):
    thirt_number = input("Instert third number: ")
elif io1 == ("/"):
    thirt_number = input("Instert third number: ")
# if all numbers are inserted this will happen
if io+io1 == ("+")+("+"):
    Sum = float(first_number) + float(second_number) - float(thirt_number)
elif io+io1 == ("+")+("-"):
    Sum = float(first_number) + float(second_number) + float(thirt_number)
elif io+io1 == ("+")+("*"):
    Sum = float(first_number) + float(second_number) * float(thirt_number)
elif io+io1 == ("+")+("/"):
    Sum = float(first_number) + float(second_number) / float(thirt_number)
elif io+io1 == ("-")+("-"):
    Sum = float(first_number) - float(second_number) - float(thirt_number)
elif io+io1 == ("-")+("+"):
    Sum = float(first_number) - float(second_number) + float(thirt_number)
elif io+io1 == ("-")+("*"):
    Sum = float(first_number) - float(second_number) * float(thirt_number)
elif io+io1 == ("-")+("/"):
    Sum = float(first_number) - float(second_number) / float(thirt_number)
elif io+io1 == ("*")+("*"):
    Sum = float(first_number) * float(second_number) * float(thirt_number)
elif io+io1 == ("*")+("+"):
    Sum = float(first_number) * float(second_number) + float(thirt_number)
elif io+io1 == ("*")+("-"):
    Sum = float(first_number) * float(second_number) - float(thirt_number)
elif io+io1 == ("*")+("/"):
    Sum = float(first_number) * float(second_number) / float(thirt_number)
elif io+io1 == ("/")+("/"):
    Sum = float(first_number) / float(second_number) / float(thirt_number)
elif io+io1 == ("/")+("+"):
    Sum = float(first_number) / float(second_number) + float(thirt_number)
elif io+io1 == ("/")+("-"):
    Sum = float(first_number) / float(second_number) - float(thirt_number)
elif io+io1 == ("/")+("*"):
    Sum = float(first_number) / float(second_number) * float(thirt_number)
# if io=+,-,*,/ and io1="[nothing] "
if io+io1 == ("+")+(""):
    Sum = float(first_number) + float(second_number)
elif io+io1 == ("-")+(""):
    Sum = float(first_number) - float(second_number)
elif io+io1 == ("*")+(""):
    Sum = float(first_number) * float(second_number)
elif io+io1 == ("/")+(""):
    Sum = float(first_number) / float(second_number)
# if we used the second thing in beggining this will appear:
if io_or_2V == ("2"):
    insertnumber = input("Insert number: ")
elif io_or_2V == ("2"):
    io2V = input("²(2) or √(V): ")
if io2V == (2):
    Sum = float(insertnumber) * float(insertnumber)
elif io2V == ("v"):
    Sum = math.sqrt(insertnumber)
elif io2V == ("V"):
    Sum = math.sqrt(insertnumber)
print(Sum)

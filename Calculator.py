import time
first_number = input("Insert first number: ")
second_number = input("Insert second number: ")
third_number = input("Insert third number: ")
forth_number = input("Insert forth number: ")
whickoperation = input("1-+ 2-- 3-* 4-/: ")
if whickoperation == ("1"):
    Sum = float(first_number) + float(second_number) + \
        float(third_number) + float(forth_number)
    print("Equals:  " + str(Sum))
elif whickoperation == ("2"):
    Sum1 = float(first_number) - float(second_number) - \
        float(third_number) - float(forth_number)
    print("Equals: " + str(Sum1))
elif whickoperation == ("3"):
    Sum2 = float(first_number) * float(second_number) * \
        float(third_number) * float(forth_number)
    print("Equals: " + str(Sum2))
elif whickoperation == ("4"):
    Sum3 = float(first_number) / float(second_number) / \
        float(third_number) / float(forth_number)
    print("Equals: " + str(Sum3))
time.sleep(20)

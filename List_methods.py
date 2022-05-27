number = (1, 2, 3, 4, 5,)
# we can add new things to end of these lists with .append
number.append(20)
# if we want add number on specific index we can use .insert(index,number that we want to add)
number.insert(0, 10)
# if we want to remove we can use .remove(number)
number.remove(5)
# if we want to remove whole list we use .clear()
number.clear()
# if we want to remove last number from list we can use .pop()
number.pop()
# if we want to print index of given number we use .index(number)
number.index(2)
# we can count how many same numbers are in the list with .count(number)
number.count(1)
# if we want to sort these numbers from LOW TO MAX we use .sort() and then we need to use print
number.sort()
print(number)
# if we want to sort these numbers from MAX TO LOW we use .reverse() and then we need to use print
number.reverse()
print(number)
# we can create copy of some list
number2 = number.copy()

for item in number:
    print(item)
i = 0

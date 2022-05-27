has_high_income = True
has_good_credit = True
# we can use "and" so all things should be true
# if we use "or" that means that at least one of them should be true
# if non of them is true we can use "not"
if has_high_income and has_good_credit:
    print("Eligible for loan")
elif has_good_credit or has_high_income:
    print("Eligible for loan")
elif not has_high_income and not has_good_credit:
    print("Not eligible for loan")

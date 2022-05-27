import time
weight = input("Instert Weight(KG/LBS): ")
lg_lbs = input("(K)g or (L)bs: ")
if lg_lbs == ("K"):
    sum = float(weight) * 2.205
    print("Your weight is: "+str(sum) + " Lbs")
elif lg_lbs == ("L"):
    sum1 = float(weight) / 2.205
    print("Your weight in Kgs is: "+str(sum1), " Kg")
elif lg_lbs == ("l"):
    sum1 = float(weight) / 2.205
    print("Your weight is: "+str(sum1)+" Kg")
elif lg_lbs == ("k"):
    sum = float(weight) * 2.205
    print("Your weight is: "+str(sum)+" Lbs")
time.sleep(10)

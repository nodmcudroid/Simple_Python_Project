while True:
    try:
        p = float(input("Enter principal amount: "))
        if p <= 0:
            print("Enter valid number")
        else:
            pass

        r = float(input ("Enter interest rate amount: "))
        if p <= 0:
            print("Enter valid number")
        else:
            pass

        t = int(input("Enter  time duration "))
        if p <= 0:
            print("Enter valid number")
        else:
            pass
        c = p * pow((1 + r /100)  , t)

        a = round(c)
        print(a)
    except ValueError:
        print("Enter Correct Thing")
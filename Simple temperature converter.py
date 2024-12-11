while True:
    try :
        unit = input("Enter (C or F):")
        num = float(input("Enter Number"))
        if unit == 'C':
            d = round((num * 9/5) +32 , 1)
            print(d)
            print("------------------------")
        elif unit == 'F':
            d = round((num -32)* 5/9 , 1)
            print(d)
            print("------------------------")
    except ValueError :
        print("Enter number")

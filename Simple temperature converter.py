while True:
    try :
        unit = input("Enter (C or F):")
        num = float(input("Enter Number"))
        if unit == 'C':
            d = num * 2
            print(d)
            print("------------------------")
        elif unit == 'F':
            d = num + 3
            print(d)
            print("------------------------")
    except ValueError :
        print("Enter number")
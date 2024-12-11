def cal():
    while True:
        try :
            a = int(input("1st Number"))
            b = int(input("2nd Number"))
            choice = input("Operator [ + , - , * , / , #]")
            if choice=='+':
                d = a + b
                print("is Equal to" , d)
            elif choice == '-':
                if b <0:
                    print("Enter Big Number")
                else :
                    d = a -b
                    print(b)
            elif choice == '*':
                d = a * b
                print("is Equal to" , d)
            elif choice == '/':
                if b < 0:
                    print("Cannot divide by zero")
                else:
                    d = a / b
                    print("is Equal to" , d)

            elif choice == "#":
                print("Have a nice ")
                break
        except :
            print( "Enter Correct Number")


cal()

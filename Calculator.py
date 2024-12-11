def cal():
    while True:
        try :
            print("[to exist press #]")
            choice = input("Operator ( +  -  *  /  #)")
            a = int(input("1st Number"))
            b = int(input("2nd Number"))

            if choice=='+':
                d = a + b
                print("is Equal to" , d)
                print("-------------------------")
                print("Enter new math")
            elif choice == '-':
                if b <0:
                    print("Enter Big Number")
                else :
                    d = a -b
                    print("is Equal to" , d)
                    print("-------------------------")
                    print("Enter new math")

            elif choice == '*':
                d = a * b
                print("is Equal to" , d )
                print("-------------------------")
                print("Enter new math")

            elif choice == '/':
                if b < 0:
                    print("Cannot divide by zero")
                else:
                    d = a / b
                    print("is Equal to" , d)
                    print("-------------------------")
                    print("Enter new math")

            elif choice == "#":
                break

        except :
            print( "Enter Correct Number")


cal()

a = True
while a:
    try:
        email = input("Enter Your Email: ")
        if email == 'exit':
            a = False
            print("Have a nice day")
            break
        index = email.index('@')
        username = email[:index]
        domain = email[index + 1:]
        print(f"this is your username {username} and this is your domain {domain}")
        print("--------------------------")
        print("Enter new email id to slice it")
        print("--------------------------")
    except ValueError:
        print("Enter valid Email i'd")
        print("--------------------------")
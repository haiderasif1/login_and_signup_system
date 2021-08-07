from data import DATA


class system(DATA):
    pass


condition = "yes"
while condition == "yes":
    print("\t Login and signup system\n")
    print("1: To Register\n")
    print("2: To Login\n")
    choice = int(input("Enter your option: "))
    if choice == 1:
        file=open("C:/Users/haide/PycharmProjects/login_and_signup_system/file.txt","w")
        id=input("Enter your id: ")
        password=input("Enter your password: ")
        file.write(id)
        file.write("\n")
        file.write(password)
        file.close()
    elif choice == 2:
        file=open("C:/Users/haide/PycharmProjects/login_and_signup_system/file.txt").read().split('\n')
        s=system(file[0],file[1])
        id1=input("Enter your id:")
        password1=input("Enter your password:")
        if id1 == s.id and password1==s.password:
            print("Logged in sucessfully")
        else:
            print("Failed to login")
    else:
        print("Wrong input")
    condition=input("Press yes to try again:")


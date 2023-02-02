import second

granted = False


def grant():
    global granted
    granted = True


def login(name, password):
    success = False
    file = open("accounts.txt", "r")
    for i in file:
        if i.strip() == "":
            continue
        a, b = i.split(" ")
        b = b.strip()
        if (a == name and b == password):
            success = True
            break
    file.close()
    if (success):
        print("Logged in.")
        grant()
    else:
        print("Wrong Username or Password")


def register(name, password):
    file = open("accounts.txt", "a")
    file.write("\n" + name + " " + password)
    file.close()
    print("Registered.")
    grant()


def access(option):
    global name
    if (option == "login"):
        name = input("Enter your username: ")
        password = input("Enter your password: ")
        login(name, password)
    else:
        print("Enter your name and password to register")
        name = input("Enter your username: ")
        wanna_gen = input("Do you want a generated password? yes/no")
        if wanna_gen.lower() == "yes":
            password = second.get_random_pw()
        else:
            password = input("Enter your password: ")
        register(name, password)


def start():
    global option
    print("Simple Login Application")
    option = input("Login or Register (Type 'login' or 'register'): ")
    if (option != "login" and option != "register"):
        print("Please Choose Login or Register")
        start()


start()
access(option)
if (granted):
    print("Welcome")
    print(name)

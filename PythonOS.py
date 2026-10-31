# Okay i want to create this mini 'PythonOS'
print("Welcome to PythonOS v0.1!")

command = input("/ > ")

if command == "help":
    print("help - shows all the commands")
    print("uname - shows the operating system")
    print("addition - does addition with 2 numbers")
if command == "uname":
    # I'm using variables instead of just printing PythonOS because it's cool LOL!
    os = "PythonOS"
    print(os)
if command == "addition":
    number1 = int(input("What should be number 1?"))
    number2 = int(input("What should be number 2?"))
    number1 += number2
    print(number1)
# Okay, i'm not going to make a 'command not found' this is just a silly little project
# Welp, Github is going to be stunned!
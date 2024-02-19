def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("Please choose an operation :")
print(" 1. *ADDITION*")
print(" 2. *MULTIPLICATION*")
print(" 3. *SUBTRACTION*")
print(" 4. *DIVISION*")
while True:
    choice = input("Please enter your choice according to your operation :1/2/3/4   ")
    if choice in ('1','2','3','4'):
        try:
            num1=float(input("Please enter first number: "))
            num2=float(input("Please enter second number: "))
        except ValueError:
            print("Invalid input **Please enter a valid input**")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1,num2))
        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1,num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1,num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1,num2))
        next_cal = input ("Want to do next operation ? y / n   ")
        print('\n')
        if next_cal == "n":
            print("       *** THANK YOU***")
            break
    else:
        print("Invalid input")

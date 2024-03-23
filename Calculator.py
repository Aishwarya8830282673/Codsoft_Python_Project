#For Addition
def addition(a,b):
    return a+b

#For Substraction
def substract(a,b):
    return a-b

#For Multiplication
def multiply(a,b):
    return a*b

#For Division
def divide(a,b):
    return a/b

print("***************** DIGITAL CALCULATOR *********************")
print("Please Select Operator:")
print("1.addition")
print("2.substract")
print("3.multiply")
print("4.divide")

while True:
    choice = input("Enter Your Choice(1/2/3/4): ")
    if choice in ('1','2','3','4'):
        try:
            num1=float(input("Enter First Number: "))
            num2=float(input("Enter Second Number: "))
        except ValueError:
            print("Invalid input. Please Enter a number..")
            continue
    else: 
        print("Error!!! Please Select Correct Number.")

    if choice == '1':
        print(num1, "+", num2, "=", addition(num1, num2))
    
    elif choice == '2':
        print(num1, "-", num2, "=", substract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

    continue_calculation = input("Do You Want To Continue Calculations? (yes/no): ")
    if continue_calculation == "no":
        break
    else:
        print("Error!!! Please Select Valid Input...")

print("Welcome to Multi- Purpose Python projects")

print("If you Want to Calculate enter 1, If you Want to Check if you are eligible for for driving and voting enter 2,:\n")
opt = input("Please enter your options:\n")
opt = int(opt)

if opt == 1:
    print("Welcome TO the calculator. Please Enter the numbers")
    num_1 = input("Enter first number:\n")
    num_2 = input("Enter second number:\n")
    print("If you want to add enter 1, subtract enter 2, multiply enter3, devide enter 4\n")
    operator = input("Enter the operator:\n")
    operator = int(operator)
    num_1 = float(num_1)
    num_2 = float(num_2)

    if operator == 1:
        print("Adding the sums..")
        print("The Sum is:")
        print(num_1 + num_2)
    if operator == 2:
        print("Finding the difference..")
        print("The difference is:")
        print(num_1 - num_2)

    if operator == 3:
        print("Multiplying the numbers..")
        print("The product is:")
        print(num_1 * num_2)
    if operator == 4:
        print("Deviding th numbers the numbers..")
        print("The Questiont is:")
        print(num_1 / num_2)


if opt == 2:
    age = input("Please Enter your age\n")
    age = float(age)

    if age >= 18:
        print("You Can Vote and drive a car")
    else:
        print("you cannot drive a car")
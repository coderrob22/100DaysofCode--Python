#calculator
from calculator_art import logo

#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

# divide
def divide(n1, n2):
    return n1 / n2

calculator_dict ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    
    num1 = float(input("What's the first number?: "))

    for ops in calculator_dict:
        print(ops)

    calculate_more = True


    while calculate_more:
        operation_picker = input("What operation would you like to perform?: ")
        num2 = float(input("What's the next number?: "))

        calc = calculator_dict[operation_picker]

        answer = calc(num1, num2)

        print(f"{num1}{operation_picker}{num2} = {answer}")

        if input("Would you like to calculate more? Type 'y' to continue or 'n' to exit. \n") == 'n':
            calculate_more = False
            calculator()
        else:
            num1 = answer
        
calculator()
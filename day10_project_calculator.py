#calculator

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

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for ops in calculator_dict:
    print(ops)

operation_picker = input("What operation would you like to perform?: ")

calc = calculator_dict[operation_picker]

answer = calc(num1, num2)

print(f"{num1}{operation_picker}{num2} = {answer}")
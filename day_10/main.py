def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    """ A function that takes two number inputs and carries out
     a basic calculation using both numbers"""
    f_num = int(input("Please type the first number: "))
    calculating = True
    while calculating:
        print("+\n-\n*\n/")
        symbol = input("Please choose a mathmetical operator: ")
        l_num = int(input("Please choose a second number: "))

        answer = operations[symbol](f_num,l_num)
        print(f"{f_num} {symbol} {l_num} = {answer}")
        carry_on = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")
        if carry_on == "y":
            f_num = answer
        else:
            calculating = False
            print("\n" * 20)
            calculator()
        # print(operations["*"](4,8))
calculator()
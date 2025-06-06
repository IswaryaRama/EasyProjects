print("Calculator")
print("Enter 'x' to exit")
while True:
    n1 = input("Enter first number: ")
    if n1 == 'x':
        break
    
    n2 = input("Enter second number: ")
    if n2 == 'x':
        break
    
    o = input("Operation:- +, -, *, /: ")
    if o == 'x':
        break
    
    try:
        n1 = float(n1)
        n2 = float(n2)
        
        if o == '+':
            print(f"Result: {n1 + n2}")
        elif o == '-':
            print(f"Result: {n1 - n2}")
        elif o == '*':
            print(f"Result: {n1 * n2}")
        elif o == '/':
            if n2 == 0:
                print("Can't divide by zero!")
            else:
                print(f"Result: {n1 / n2}")
        else:
            print("Invalid operation")
    except ValueError:
        print("Please enter numbers only")
import argparse

parser = argparse.ArgumentParser(description="Simple calculator")
parser.add_argument("-o", choices=["add", "subtract", "multiply", "divide"], help="Operation to perform")
parser.add_argument("-x", type=float, help="First number", required=True)
parser.add_argument("-y", type=float, help="Second number", required=True)

args = parser.parse_args()

def add(x, y):
    print(f"{x} + {y} = {x + y}")
    return x + y

def subtract(x, y):
    print(f"{x} - {y} = {x - y}")
    return x - y

def multiply(x, y):
    print(f"{x} * {y} = {x * y}")
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    print(f"{x} / {y} = {x / y}")
    return x / y

if args.o == "add":
    result = add(args.x, args.y)
elif args.o == "subtract":
    result = subtract(args.x, args.y)
elif args.o == "multiply":
    result = multiply(args.x, args.y)
elif args.o == "divide":
    result = divide(args.x, args.y)
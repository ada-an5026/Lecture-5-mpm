def hello(name):
    print(f"Hello, {name}!")

# hello('Alice')  when importing this file, it will also run this statement and print an output

if __name__ == "__main__":
    hello('Alice')  # This will only run when the script is executed directly, not when imported


from sys import argv,exit

def list_commands():
    print("Available commands in hellosp package are:")
    print("  add <a> <b> : Calculates the sum of <a> and <b>")
    print("  list        : Lists all commands available in hellosp package")

def add(a,b):
    try:
        result = int(a) + int(b)
        print("Sum is ",result)
    except ValueError:
        print("Error: Please provide valid integer arguments.")

def main():
    if len(argv) == 1 and argv[0] == "hellosp":
        print("Hello, this is a simple cli tool that adds 2 integers")
    elif len(argv) <2:
        print("Unknown command. Please find the list of commands")
        list_commands()
        exit(1)
    
    command = argv[1]
    if command == "list":
        list_commands()
    elif command == "add":
        if len(argv) != 4:
            print("Usage: givesum add <a> <b>")
            exit(1)
        a = argv[2]
        b = argv[3]
        add(a,b)
    else:
        print("Unknown command. Please find the list of commands")
        list_commands()
        exit(1)

if __name__ == "__main__":
    main()
#계산기를 만드는 문제로 두가지 방식으로 문제를 풀었음.

playing = True


a = int(input("Choose a number:\n"))
b = int(input("Choose another one:\n"))
operation = input(
    "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n"
)

# add your code here!
while playing:
    a = int(input("Choose a number:\n"))
    b = int(input("Choose another one:\n"))
    operation = input(
        "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n"
    )

    if operation != "exit":
        if operation == "+":
            result = a + b

        elif operation == "-":
            result = a - b

        elif operation == "*":
            result = a * b

        elif operation == "/":
            result = a / b

        print(f"Result: {result}")

    else:
        playing = False

# Another case

playing = True
a = None
b = None
operation = None

while playing:
    if a is None:
        a = int(input("Choose a number:\n"))
    if b is None:
        b = int(input("Choose another one:\n"))
    if operation is None:
        operation = input(
            "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n"
        )

    if operation != "exit":
        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            result = a / b

        print(f"Result: {result}")
    else:
        playing = False

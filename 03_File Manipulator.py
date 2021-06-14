import os

data = input()
while not data == "End":
    command, *options = data.split("-")

    if command == "Create":
        with open(*options, 'w') as file:
            pass

    elif command == "Add":
        file, content = options
        with open(file, 'a') as file:
            file.write(content + '\n')

    elif command == "Replace":
        file_name, old, new = options
        try:
            with open(file_name, 'r') as file:
                content = file.read()

            with open(file_name, 'w') as file:
                content = content.replace(old, new)
                file.write(content)

        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(*options)
        except FileNotFoundError:
            print("An error occurred")

    data = input()

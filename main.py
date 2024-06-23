password = input()

while True:
    command = input().split()
    current_command = command[0]

    if current_command == "Complete":
        break

    if command[0] == "Make":
        if command[1] == "Upper":
            index = int(command[2])
            if 0 <= index < len(password):
                password = password[:index] + password[index].upper() + password[index + 1:]
                print(password)
        if command[1] == "Lower":
            index = int(command[2])
            if 0 <= index < len(password):
                password = password[:index] + password[index].lower() + password[index + 1:]
                print(password)

    elif command[0] == "Insert":
        index = int(command[1])
        char = command[2]
        if 0 <= index <= len(password):
            password = password[:index] + char + password[index:]
            print(password)

    elif command[0] == "Replace":
        char = command[1]
        value = int(command[2])
        if char in password:
            new_char = chr(ord(char) + value)
            password = password.replace(char, new_char)
            print(password)

    elif command[0] == "Validation":
        if len(password) < 8:
            print("Password must be at least 8 characters long!")

        if not all(c.isalnum() or c == '_' for c in password):
            print("Password must consist only of letters, digits and _!")

        if not any(c.isupper() for c in password):
            print("Password must consist at least one uppercase letter!")

        if not any(c.islower() for c in password):
            print("Password must consist at least one lowercase letter!")

        if not any(c.isdigit() for c in password):
            print("Password must consist at least one digit!")

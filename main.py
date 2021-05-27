from input_validation import validate, read_file, clear_file, say_goodbye, agreeWords


while True:
    userInput = input("Enter some value: ")

    if userInput.lower() == "show":
        read_file()

    if userInput.lower() == "clear":

        if input("Are you sure?").lower() in agreeWords:
            clear_file()

        else:
            continue

    elif userInput == "q":
        say_goodbye()
        break

    else:

        validate(userInput)

from model.model import initialize_model, usercall, userresult

while True:
    print("Modes:")
    print("1. High accuracy")
    print("2. High f_score")
    print("3. Custom threshhold value")
    print("Choose: ", end="")
    mode = int(input())
    if mode == 1:
        initialize_model(type="accuracy")
    elif mode == 2:
        initialize_model(type="f_score")
    elif mode == 3:
        print("Enter custom threshhold: ", end="")
        custom_threshhold = float(input())
        initialize_model(type="custon", custom=custom_threshhold)
    else:
        print("Invalid choice")

print("Original filepath to test against: ", end="")
original_file = input()
original_vector = usercall(original_file)

while original_vector == None:
    print("Invalid file, try again: ", end="")
    original_file = input()

while True:
    print("Enter file path: ", end="")
    test_file = input()
    test_vector = usercall(test_file)
    if test_vector != None:
        isPlag = userresult(original_vector, test_vector)
        if isPlag == True:
            print("File is plagiarized!")
        else:
            print("No plagiarism detected")
    else:
        print("Invalid file")
    print("Do you want to exit? y/[n]")
    toExit = input()
    if toExit == "y":
        break

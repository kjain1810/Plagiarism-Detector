import os.path

from model.model import initialize_model, usercall, userresult

while True:
    print("Modes:")
    print("1. High accuracy")
    print("2. High f_score")
    print("3. Custom threshhold value")
    print("Choose: ", end="")
    mode = int(input())
    if mode == 1:
        initialize_model(modeltype="accuracy")
        break
    elif mode == 2:
        initialize_model(modeltype="f_score")
        break
    elif mode == 3:
        print("Enter custom threshhold: ", end="")
        custom_threshhold = float(input())
        initialize_model(modeltype="custom", custom=custom_threshhold)
        break
    else:
        print("Invalid choice")

print("Original filepath to test against: ", end="")
original_file = input()

while os.path.isfile(original_file) == False:
    print("Invalid file, try again: ", end="")
    original_file = input()

original_vector, _ = usercall(original_file)

while True:
    print("Enter file path: ", end="")
    test_file = input()
    if os.path.isfile(test_file) != False:
        test_vector, _ = usercall(test_file)
        print(test_vector)
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

#!/usr/bin/env python3

import os.path

from model.model import initialize_model, calcforuser


def askexit():
    print("Do you want to exit? y/[n]: ", end="")
    ans = input()
    return ans == "y"


def runner():
    while True:
        print("Modes:")
        print("1. High accuracy")
        print("2. High f_score")
        print("3. Custom threshhold value")
        print("Choose: ", end="")
        mode = int(input())
        if mode == 1:
            print("Initializing model....")
            initialize_model(modeltype="accuracy")
            break
        elif mode == 2:
            print("Initializing model....")
            initialize_model(modeltype="f_score")
            break
        elif mode == 3:
            print("Enter custom threshhold: ", end="")
            custom_threshhold = float(input())
            print("Initializing model....")
            initialize_model(modeltype="custom", custom=custom_threshhold)
            break
        else:
            print("Invalid choice")

    while True:
        print("Enter first file: ", end="")
        first_file_path = input()
        if os.path.isfile(first_file_path) == False:
            print("Invalid path!")
            tobreak = askexit()
            if tobreak:
                break
            continue
        print("Enter second file: ", end="")
        second_file_path = input()
        if os.path.isfile(second_file_path) == False:
            print("Invalid path!")
            tobreak = askexit()
            if tobreak:
                break
            continue

        res = calcforuser(first_file_path, second_file_path)
        if res:
            print("Files are plagiarized!")
        else:
            print("Files aren't plagiarized :)")
        tobreak = askexit()
        if tobreak:
            break


if __name__ == '__main__':
    runner()

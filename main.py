#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from getpass import getuser
from platform import system
from shutil import copyfile
from os import mkdir, getcwd
from sys import argv
from secrets import choice
from numpy import append
from json import load
from colorama import init, Fore, Style


init()

fbblue = Fore.BLUE + Style.BRIGHT
fbred = Fore.RED + Style.BRIGHT
fbgreen = Fore.GREEN + Style.BRIGHT
fbmagenta = Fore.MAGENTA + Style.BRIGHT
fbcyan = Fore.CYAN + Style.BRIGHT
reset_Stile = Style.RESET_ALL

def config_save():
    user_name = getuser()
    if system() == "Linux":
        try:

            js = open("/home/" + user_name + "/.config/PassGen/alph.json", "r")

        except BaseException:
            try:
                mkdir("/home/" + user_name + "/.config/PassGen")
            except BaseException:
                pass
            copyfile(
                getcwd() +
                "/alph.json",
                "/home/" +
                user_name +
                "/.config/PassGen/alph.json")
            
            print(
                "\nFile alph.json has been moved to a /home/" +
                user_name +
                "/.config/PassGen/")

            js = open("/home/" + user_name + "/.config/PassGen/alph.json", "r")

    elif "Windows" in system():
        try:
            js = open("C:/Users/" + user_name + "/PassGen/alph.json", "r")

        except BaseException:
            try:
                mkdir("C:/Users/" + user_name + "/PassGen")

            except BaseException:
                pass

            copyfile(
                getcwd() +
                "/alph.json",
                "C:/Users/" +
                user_name +
                "/PassGen/alph.json")
            print(
                "\nFile alph.json has been moved to a C:/Users/" +
                user_name +
                "/PassGen/")

            js = open("C:/Users/" + user_name + "/PassGen/alph.json", "r")
    return js


def PassGen(amount, count, special, name, is_file, numbers):
    result = []
    js = config_save()

    full_alph = load(js)
    simb = full_alph["alph"]
    number_alph = full_alph["numbers"]
    s_simb = full_alph["s_alph"]
    
    us_alph = simb
    color = fbblue

    if special:
        us_alph = append(us_alph, s_simb)
        color = fbmagenta

    if numbers:
        us_alph = append(us_alph,number_alph)
        color = fbgreen

    if numbers and special:
        color = fbcyan


    lst = ""
    password = ""

    for i in range(count):
        password = ""
        for j in range(amount):
            password += choice(us_alph)
        lst += password + "\n"
    if is_file == "True":

        file = open(name + ".txt", "w")
        file.write(lst)
    else:
        pass

    for i in lst.split():
        result.append(str(color + i + reset_Stile))
    return result


if __name__ == "__main__":
    
    amount_= 8
    count_= 10
    special_= False
    name_= "pass"
    numbers_ = False
    is_file_= False
    
    for i in range(1,len(argv),1):
        if argv[i] == "-h" or argv[i] == "--help" or len(argv) == 0:
            print(fbgreen + "Parameter with " + fbmagenta + "this" + reset_Stile + fbgreen +" color does not need additional parameters.\n" + reset_Stile)
            print(fbcyan + "-a or --amount  : Number of characters in the password (" + fbgreen +  "int" + reset_Stile + fbcyan + ").")
            print(fbcyan + "-c or --count   : Amount passwords (" + fbgreen +  "int" + reset_Stile + fbcyan + ").")
            print(fbmagenta + "-s or --special : Use special characters." + reset_Stile)
            print(fbcyan + "-N or --name    : Output file name (" + fbgreen +  "int" + reset_Stile + fbcyan + ").")
            print(fbmagenta + "-f or --file    : Create a text file.")
            print(fbmagenta + "-n or --numbers : Use numbers")
            exit(0)
        try:
            if argv[i] == "-a" or argv[i] == "--amount":
                amount_ = int(argv[i + 1])

            elif argv[i] == "-c" or argv[i] == "--count":
                count_ = int(argv[i + 1])

            elif argv[i] == "-s" or argv[i] == "--special":
                special_ = True

            elif argv[i] == "-N" or argv[i] == "--name":
                name_ = argv[i + 1]

            elif argv[i] == "-f" or argv[i] == "--file":
                is_file_ = "True"

            elif argv[i] == "-n" or argv[i] == "-numbers":
                numbers_ = True

        except:
            print(fbred + "Unknown option: " + argv[i] + ".\nType pg -h.")
            exit()

    print(
        "\n".join(PassGen(
        amount=amount_,
        count=count_,
        special=special_,
        name=name_,
        is_file=is_file_,
        numbers=numbers_))
        )
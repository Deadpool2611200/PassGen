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

fbgreen = Fore.GREEN + Style.BRIGHT
fbmagenta = Fore.MAGENTA + Style.BRIGHT
fbcyan = Fore.CYAN + Style.BRIGHT
reset_Stile = Style.RESET_ALL



def PassGen(amount, count, special, name, is_file):
    
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
                "\n File alph.json has been moved to a /home/" +
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
                "\n File alph.json has been moved to a C:/Users/" +
                user_name +
                "/PassGen/")

            js = open("C:/Users/" + user_name + "/PassGen/alph.json", "r")

    full_alph = load(js)
    simb = full_alph["alph"]
    s_simb = full_alph["s_alph"]

    if special:
        us_alph = append(simb, s_simb)
        color = fbmagenta


    else:
        us_alph = simb
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
    print()
    for i in lst.split():
        print(color + i + reset_Stile)


if __name__ == "__main__":
    
    amount_= 8
    count_= 10
    special_= False
    name_= "pass"
    is_file_= False
    
    for i in range(len(argv)):
        if argv[i] == "-h" or argv[i] == "--help" or len(argv) == 0:
            print(fbgreen + "Parameter with " + fbmagenta + "this" + reset_Stile + fbgreen +" color does not need additional parameters.\n" + reset_Stile)
            print(fbcyan + "-a or --amount  : Number of characters in the password (" + fbgreen +  "int" + reset_Stile + fbcyan + ").")
            print(fbcyan + "-c or --count   : Amount passwords (" + fbgreen +  "int" + reset_Stile + fbcyan + ").")
            print(fbmagenta + "-s or --special : Use or not use special characters." + reset_Stile)
            print(fbcyan + "-n or --name    : Output file name (" + fbgreen +  "int" + reset_Stile + fbcyan + ").")
            print(fbmagenta + "-f or --file    : Create a text file or not.")
            exit(0)
        if argv[i] == "-a" or argv[i] == "--amount":
            amount_ = int(argv[i + 1])

        if argv[i] == "-c" or argv[i] == "--count":
            count_ = int(argv[i + 1])

        if argv[i] == "-s" or argv[i] == "--special":
            special_ = True

        if argv[i] == "-n" or argv[i] == "--name":
            name_ = argv[i + 1]
        if argv[i] == "-f" or argv[i] == "--file":
            is_file_ = "True"

    PassGen(
        amount=amount_,
        count=count_,
        special=special_,
        name=name_,
        is_file=is_file_)

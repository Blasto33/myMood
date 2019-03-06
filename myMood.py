#!/usr/bin/env python3

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

def init_mood():
    sys.stdout.write("\nWelcome on the myMood application !\n")
    sys.stdout.write("----------------\n\n")
    sys.stdout.write("The goal of this application is to get your global mood according to the values you enter everyday.\n\n")

def check_line(list_mood, line):
    period = 7
    #TODO: Afficher seulement les 7 dernières valeurs, sauf si moins de valeurs sont disponibles dans la liste

    if line == "show\n":
        if len(list_mood) == 0:
            print("ZERO")
        else:
            print(list)
    elif line == "exit\n":
        exit(0)

def display_instructions():
    sys.stdout.write("Type \"SHOW\" to display the 7 latest values, \"ENTER\" to append your current mood or \"exit\" to leave. \n")

def shell():
    list_mood = []
    display_instructions()
    while 1:
        sys.stdout.write("> ")
        line = sys.stdin.readline()
        check_line(list_mood, line)
        sys.stdout.write("\n")

if __name__ == '__main__':
    init_mood()
    shell()


#!/usr/bin/env python3

import sys
import os
import datetime

def init_mood():
    sys.stdout.write("\nWelcome on the myMood application !\n")
    sys.stdout.write("----------------\n\n")
    sys.stdout.write("The goal of this application is to get your global mood according to the values you enter everyday.\n\n")

def append_current_energy(list_energy):
    correct_value = "false"

    print("On a scale from 1 to 10, how would you describe your current energy?")
    while correct_value != "true":
        sys.stdout.write("> ")
        line = sys.stdin.readline()
        try:
            value = int(line)
        except ValueError:
            print("\nYou have to type a number between 1 and 10")
        else:
            list_energy.append(value)
            correct_value = "true"
    return (list_energy)

def append_current_focus(list_focus):
    correct_value = "false"

    print("On a scale from 1 to 10, how would you describe your current focus?")
    while correct_value != "true":
        sys.stdout.write("> ")
        line = sys.stdin.readline()
        try:
            value = int(line)
        except ValueError:
            print("\nYou have to type a number between 1 and 10")
        else:
            list_focus.append(value)
            correct_value = "true"
    return (list_focus)

def append_current_motivation(list_motivation):
    correct_value = "false"

    print("On a scale from 1 to 10, how would you describe your current motivation?")
    while correct_value != "true":
        sys.stdout.write("> ")
        line = sys.stdin.readline()
        try:
            value = int(line)
        except ValueError:
            print("\nYou have to type a number between 1 and 10")
        else:
            list_motivation.append(value)
            correct_value = "true"
    return (list_motivation)


def compute_mood(list_energy, list_focus, list_motivation):
    period = 0

    while period < 7:
        print(list_energy[period:])
        print(list_focus[period:])
        print(list_motivation[period:])
        period+=1

def check_line(list_energy, list_focus, list_motivation, line):
    sys.stdout.write("\n")
    if line == "show\n":
        if len(list_energy) == 0:
            print("You have to append your mood at least one time before trying to display anything. Why don't you retry to do this in a few days ?")
        else:
            compute_mood(list_energy, list_focus, list_motivation)
    elif line == "enter\n":
        list_energy = append_current_energy(list_energy)
        list_focus = append_current_focus(list_focus)
        list_motivation = append_current_motivation(list_motivation)
    elif line == "exit\n":
        exit(0)
    else:
        display_instructions()

def display_instructions():
    sys.stdout.write("Type \"SHOW\" to display the 7 latest values, \"ENTER\" to append your current mood or \"exit\" to leave. \n")

def shell():
    list_energy = []
    list_focus = []
    list_motivation = []

    display_instructions()
    while 1:
        sys.stdout.write("> ")
        line = sys.stdin.readline()
        check_line(list_energy, list_focus, list_motivation, line)
        sys.stdout.write("\n")

if __name__ == '__main__':
    init_mood()
    shell()


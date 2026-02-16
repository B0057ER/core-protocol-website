import time
import math
import random

Time = int(60)
print("     Main Menu")
print("        Y/N")
Start_game = input(print("     Start game? "))
if Start_game == "Y":
    print("Starting game")
    #time.sleep(2.5)
    print("Doctor: I'm sorry to tell you this but you have less then 2 mintues to live")
    time.sleep(1.5)
    print("You: WHAT?")
    time.sleep(0.60)
    print("Doctor: the cancer is unlike any we have seen it is killing you at a much faster pace then expected")
    time.sleep(2.75)
    print("You: FINE since you can't save me I'll do it myslef. how long do i have left!?")
    time.sleep(1.80)
    print("Doctor: 60 seconds")
    time.sleep(0.80)
    print("Find a cure for cancer now!")
    time.sleep(0.75)
    print(Time)
    time.sleep(0.5)
    Bed = input(print("Get out of bed Y/N "))
    if Bed == "Y":
        Time = Time - 3
        print("You get out of bed and look around the room")
        print("you see bottles labled with words you don't understand and you see the door")
        print(Time)
        time.sleep(0.5)
        leave = input(print("Do you leave or do you tale the meds?"))
    elif Bed == "N":
        print("You stay in bed and wait out the 60 seconds embracing your fate")
    else:
        print("Your shot for not inpting the right letter or caps")
elif Start_game == "N":
    print("exting Menu")
else:
    print("PLEASE ENTER Y OR N THEY MUST BE CAPS")
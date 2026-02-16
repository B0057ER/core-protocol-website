import random
import time

IP = random.randint(10000000000, 99999999999)


code = input("Please Enter Code ")
if code == "702370":
    print("Welcome B0057TER.INC/Flynn Walsh")
    time.sleep(0.75)
    print("What would you like to do? ")
    time.sleep(0.5)
    pick = input("Hire, Fire, Pay, Contract, transfure ")

    if pick == "Hire":
        print("Loading")
        time.sleep(1)
        Name = input("Who are you hiring? ")
        job = input("What job are they doing? ")
        Pay = input("How much are they being paid ")
        Pay_Rate = input("How offten are they being paid ")
        time.sleep(1.5)
        print("Hired " + Name + " to be a " + job + " and is being payed $" + Pay + " Every " + Pay_Rate)
    elif pick == "Pay":
        print("Loading")
        time.sleep(1)
        who = input("Who are you Paying? ")
        Amount = input("How much are you Paying? ")
        print("Proceesing")
        time.sleep(1.5)
        print("$" + Amount + " Has been paid to " + who)
    elif pick == "Fire":
        print("Loading")
        time.sleep(1)
        Bye = input("Who are you Firing? ")
        why = input("Why are they being fired? ")
        time.sleep(1.5)
        print(Bye + " has been fired because " + why)
    elif pick == "Contract":
        print("Loading")
        time.sleep(1)
        who1 = input("Who is being contraced")
else:
    print("Your IP ardrees is " + str(IP))
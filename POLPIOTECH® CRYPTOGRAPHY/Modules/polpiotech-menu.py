from os import system
from time import gmtime, strftime, sleep
from sys import exit
from termcolor import cprint, colored
import colorama, getpass

colorama.init
# Przełącznik LINUX / WINDOWS.
system('clear')
#system('cls')
cprint("             -- POLPIOTECH®: --             ", "red", "on_white")
cprint("        -- CRYPTOGRAPHY ver. 3.0 --         ", "white", "on_red")
print('▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░▒▒▒▒▒')
print('▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▌░░▒▒▒▒')
print('▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄███▀░░░░▒▒▒')
print('▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░█████░▄█░░░░▒▒')
print('▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄████████▀░░░░▒▒')
print('▒▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░▒')
print('▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄███████▌░░░░░░░▒')
print('▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░░▒')
print('▒░░░░░░░░░░░░░░░░░░░░░▄███████████▌░░░░░░░░▒')
print('▒░░░░░░░░░░░░░░░▄▄▄▄██████████████▌░░░░░░░░▒')
print('▒░░░░░░░░░░░▄▄███████████████████▌░░░░░░░░░▒')
print('▒░░░░░░░░░▄██████████████████████▌░░░░░░░░░▒')
print('▒░░░░░░░░████████████████████████░░░░░░░░░░▒')
print('▒█░░░░░▐██████████▌░▀▀███████████░░░░░░░░░░▒')
print('▒██░░░▄██████████▌░░░░░░░░░▀██▐█▌░░░░░░░░░▒▒')
print('▒██████░█████████░░░░░░░░░░░▐█▐█▌░░░░░░░░░▒▒')
print('▒▒▀▀▀▀░░░██████▀░░░░░░░░░░░░▐█▐█▌░░░░░░░░▒▒▒')
print('▒▒▒▒▒░░░░▐█████▌░░░░░░░░░░░░▐█▐█▌░░░░░░░▒▒▒▒')
print('▒▒▒▒▒▒░░░░███▀██░░░░░░░░░░░░░█░█▌░░░░░░▒▒▒▒▒')
print('▒▒▒▒▒▒▒▒░▐██░░░██░░░░░░░░▄▄████████▄▒▒▒▒▒▒▒▒')
print('▒▒▒▒▒▒▒▒▒██▌░░░░█▄░░░░░░▄███████████████████')
print('▒▒▒▒▒▒▒▒▒▐██▒▒░░░██▄▄███████████████████████')
print('▒▒▒▒▒▒▒▒▒▒▐██▒▒▄████████████████████████████')
print('▒▒▒▒▒▒▒▒▒▒▄▄████████████████████████████████')
print('████████████████████████████████████████████')
cprint("       STARTING PROGRAM PLEASE WAIT...      ", "white", "on_red")
for i in range(101):
    print("\rLOADING {}%".format(i), end='')
    sleep(0.03)
print()
login = getpass.getpass(str("Login: "))
password = getpass.getpass(str("Password: "))
if login == "polpiotech" and password == "WP-93_PB-93=PLSS<(2)3":
    print()
    cprint("CORRECT LOGIN AND PASSWORD!", "white", "on_red")
    for i in range(101):
        print("\rLOADING {}%".format(i), end='')
        sleep(0.03)
    # Przełącznik LINUX / WINDOWS.
    system('clear')
    #system('cls')
    cprint("       -- POLPIOTECH®: --      ", "red", "on_white")
    cprint("  -- CRYPTOGRAPHY ver. 3.0 --  ", "white", "on_red")
    print()
    date_app_reckoning = strftime(" %a, %d %b %Y", gmtime())
    time_app_reckoning = strftime("%r")
    print(date_app_reckoning, time_app_reckoning)
    print()
    def menu():
        cprint("           OPTIONS:           ", "white", "on_red")
        print("1. Encryption message.")
        print("2. Decryption message.")
        print("3. Refresh console.")
        print("4. Close program.")
        print()
        chooseOption = int(input("YOUR CHOICE: "))
        return(chooseOption)
    driver = 1
    while driver != 0:
        driver = menu()

        if driver == 1:
            cprint("You choose encryption message.", "white", "on_red")
            system('python3 polpiotech-encryption.py')
        elif driver == 2:
            cprint("You choose decryption message.", "white", "on_red")
            system('python3 polpiotech-decryption.py')
        elif driver == 3:
            # Przełącznik LINUX / WINDOWS.
            system('clear')
            #system('cls') 
            cprint("      -- POLPIOTECH®: --      ", "red", "on_white")
            cprint("   -- CRYPTOGRAPHY 1.3.2 --   ", "white", "on_red")
            print()
            date_app_reckoning = strftime(" %a, %d %b %Y", gmtime())
            time_app_reckoning = strftime("%r")
            print(date_app_reckoning, time_app_reckoning)
            print()
        elif driver == 4:
            # Przełącznik LINUX / WINDOWS.
            system('clear')
            #system('cls') 
            n = 0
            while n < 3:
                n = n + 1
                print(colored(f"             CLOSE PROGRAM: {n} s.            ", "black", "on_white"))
                sleep(1.5)
                # Przełącznik LINUX / WINDOWS.
                system('clear')
                #system('cls')
                cprint("             -- POLPIOTECH®: --             ", "red", "on_white")
                cprint("        -- CRYPTOGRAPHY ver. 3.0 --         ", "white", "on_red")
                print('▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░▒▒▒▒▒')
                print('▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▌░░▒▒▒▒')
                print('▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄███▀░░░░▒▒▒')
                print('▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░█████░▄█░░░░▒▒')
                print('▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄████████▀░░░░▒▒')
                print('▒▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░▒')
                print('▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄███████▌░░░░░░░▒')
                print('▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░░▒')
                print('▒░░░░░░░░░░░░░░░░░░░░░▄███████████▌░░░░░░░░▒')
                print('▒░░░░░░░░░░░░░░░▄▄▄▄██████████████▌░░░░░░░░▒')
                print('▒░░░░░░░░░░░▄▄███████████████████▌░░░░░░░░░▒')
                print('▒░░░░░░░░░▄██████████████████████▌░░░░░░░░░▒')
                print('▒░░░░░░░░████████████████████████░░░░░░░░░░▒')
                print('▒█░░░░░▐██████████▌░▀▀███████████░░░░░░░░░░▒')
                print('▒██░░░▄██████████▌░░░░░░░░░▀██▐█▌░░░░░░░░░▒▒')
                print('▒██████░█████████░░░░░░░░░░░▐█▐█▌░░░░░░░░░▒▒')
                print('▒▒▀▀▀▀░░░██████▀░░░░░░░░░░░░▐█▐█▌░░░░░░░░▒▒▒')
                print('▒▒▒▒▒░░░░▐█████▌░░░░░░░░░░░░▐█▐█▌░░░░░░░▒▒▒▒')
                print('▒▒▒▒▒▒░░░░███▀██░░░░░░░░░░░░░█░█▌░░░░░░▒▒▒▒▒')
                print('▒▒▒▒▒▒▒▒░▐██░░░██░░░░░░░░▄▄████████▄▒▒▒▒▒▒▒▒')
                print('▒▒▒▒▒▒▒▒▒██▌░░░░█▄░░░░░░▄███████████████████')
                print('▒▒▒▒▒▒▒▒▒▐██▒▒░░░██▄▄███████████████████████')
                print('▒▒▒▒▒▒▒▒▒▒▐██▒▒▄████████████████████████████')
                print('▒▒▒▒▒▒▒▒▒▒▄▄████████████████████████████████')
                print('████████████████████████████████████████████')
                cprint('       AUTOR: PIOTR KAZIMIERZ BODYCH        ', 'white', 'on_red')
                #cprint('            DATA: 01.10.2023 r.             ', 'cyan', 'on_white')
            exit()
else:
    print()
    cprint("LOGIN OR PASSWORD INCORRECT!", "white", "on_red")
    for i in range(101):
        print("\rRELOADING {}%".format(i), end='')
        sleep(0.03)
    # Przełącznik LINUX / WINDOWS.
    system('clear')
    #system('cls')
    system('python3 crypto-menu.py')
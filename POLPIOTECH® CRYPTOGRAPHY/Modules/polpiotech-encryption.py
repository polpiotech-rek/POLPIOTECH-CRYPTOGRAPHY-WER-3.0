from termcolor import cprint, colored
import colorama, os, getpass

colorama.init
print()
print()
cprint("ENTER VALUE ENCRYPTION ALGORITHM:", "white", "on_red")
algValue = getpass.getpass("ENTER VALUE: ")
algKey = int(algValue)
def encrypt(message, key=algKey):
    encrypted = ""
    for mark in message:
        codeASCII = ord(mark)
        codeASCII += key
        while codeASCII > 126:
            codeASCII -= 95
        while codeASCII < 32:
            codeASCII +=95
        encrypted += chr(codeASCII)
    return encrypted
print()
cprint("DO YOU WANT SAVE THIS FILE? (y/n)", "white", "on_red")
saveFile = input("YOUR CHOICE: ")
if saveFile == "y":
    print()
    print()
    cprint("INFORMATION:", "white", "on_red")
    cprint(" * [ D ] - COLOR YELLOW - DIRECTORY", "black", "on_white")
    cprint(" * [ F ] - COLOR BLUE - FILE       ", "black", "on_white")
    print()
    path = str(input('ENTER PATH: '))
    print()
    os.chdir(path)
    cprint("GO TO DIRECTORY:", "white", "on_red")
    path_directory_destination = os.getcwd()
    print(colored("[ SAVE PATH ]","black", "on_white"), colored(path, "black", "on_white"))
    for item in os.listdir('.'):
        if os.path.isdir(item):
            cprint('{} - [ D ]'.format(item), "white", "on_blue")
        else:
            cprint('{} - [ F ]'.format(item), "black", "on_yellow") 
    print()
    cprint("YOUR MESSAGE TO BE ENCRYPTED:", "white", "on_red")
    text = str(input("ENTER TEXT FOR ENCRYPTION: "))
    print()
    cprint("CONTENT ENCRYPTED MESSAGE:", "white", "on_red")
    cprint(encrypt(text), 'yellow')
    print()
    encText = encrypt(text)
    cprint("SAVING THE ENCRYPTED TEXT TO A FILE:", "white", "on_red")
    file_name = str(input('ENTER A FILE NAME: '))
    print()
    print()
    f = open(file_name, "w", encoding="utf-8")
    with open(file_name, 'w') as f:
        f.write(encText)
    f.close
else:
    print()
    cprint("YOUR MESSAGE TO BE ENCRYPTED:", "white", "on_red")
    text = str(input("ENTER TEXT FOR ENCRYPTION: "))
    print()
    cprint("CONTENT ENCRYPTED MESSAGE:", "white", "on_red")
    cprint(encrypt(text), 'yellow')
    print()
    encText = encrypt(text)
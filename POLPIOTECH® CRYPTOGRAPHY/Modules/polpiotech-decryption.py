from termcolor import cprint, colored
import colorama, os, getpass

colorama.init
print()
print()
cprint("ENTER VALUE ENCRYPTION ALGORITHM:", "white", "on_red")
algValue = getpass.getpass("ENTER VALUE: ")
algKey = int(algValue)
def decrypt(message, key=algKey):
    encrypted = ""
    for mark in message:
        codeASCII = ord(mark)
        codeASCII -= key
        while codeASCII > 126:
            codeASCII -= 95
        while codeASCII < 32:
            codeASCII +=95
        encrypted += chr(codeASCII)
    return encrypted
print()
text = str(input("YOUR MESSAGE TO DECRIPT: "))
print()
cprint("CONTENT OF THE DECRIPTED MESSAGE:", "white", "on_red")
cprint(decrypt(text), 'yellow')
print()
decText = decrypt(text)
print()
cprint("DO YOU WANT SAVE THIS FILE? (y/n)", "white", "on_red")
saveFile = input("YOUR CHOICE: ")
if saveFile == "y":
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
    cprint("SAVING THE ENCRYPTED TEXT TO A FILE:", "white", "on_red")
    file_name = str(input('ENTER A FILE NAME: '))
    print()
    print()
    f = open(file_name, "w", encoding="utf-8")
    with open(file_name, 'w') as f:
        f.write(decText)
    f.close
else:
    print()
    print()
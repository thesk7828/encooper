import base64
import sys
import argparse
import os


def hlp():
    print('''Ex: python3 encooper.py <option> <input_file_name> <output_file_name>

    OPTIONS          DESCRIPTIONS
    -h,--help        this script helps you to encrypts the strings
    -bs64,--base64   it convert strings to BASE64
    -hx,--hexa       it convert strings to HEXA DECIMAL
    -oc,--octal      it convert strings to OCTA DECIMAL''')

def bas64():  
    if os.path.isfile(sys.argv[2]):
        if os.path.isfile(sys.argv[3]):
            print(sys.argv[3], "already exist")
            temp=input("are you sure you wanna override it [Y/N]:") 
            agree=temp.lower()
            if (agree == "y") or (agree == "yes"):
                pld = open(sys.argv[2], "r")
                new = open(sys.argv[3], "a")
                for line in pld:
                    x=line.encode("ascii")
                    y=base64.b64encode(x)
                    bs64=y.decode("ascii")
                    new.write(bs64)
                    new.write("\n")
                new.close()
                pld.close()
            elif (agree == "n") or (agree == "no"):
                print("\ndamn, you hit NO, i regret i couldn't you :(")
            else:
                print("\nCouldn't find out, if it is y/n, I'm going, Adios!")
    else:
        print("Ugh, i don't beleive if", sys.argv[2], "exist")

def hexa():
    if os.path.isfile(sys.argv[2]):
        if os.path.isfile(sys.argv[3]):
            print(sys.argv[3], "already exist")
            temp=input("are you sure you wanna override it [Y/N]:") 
            agree=temp.lower()
            if (agree == "y") or (agree == "yes"):
                pld = open(sys.argv[2], "r")
                new = open(sys.argv[3], "a")
                for line in pld:
                    hexa = line.encode("utf-8").hex()
                    new.write(hexa)
                    new.write("\n")
                new.close()
                pld.close()
            elif (agree == "n") or (agree == "no"):
                print("\ndamn, you hit NO, i regret i couldn't you :(")
            else:
                print("\nCouldn't find out, if it is y/n, I'm going, Adios!")
    else:
        print("Ugh, i don't beleive if", sys.argv[2], "exist")

def octal():
    if os.path.isfile(sys.argv[2]):
        if os.path.isfile(sys.argv[3]):
            print(sys.argv[3], "already exist")
            temp=input("are you sure you wanna override it [Y/N]:") 
            agree=temp.lower()
            if (agree == "y") or (agree == "yes"):
                pld = open(sys.argv[2], "r")
                new = open(sys.argv[3], "a")
                for line in pld:
                    octal = oct(line)
                    new.write(octal)
                    new.write("\n")
                new.close()
                pld.close()
            elif (agree == "n") or (agree == "no"):
                print("\ndamn, you hit NO, i regret i couldn't you :(")
            else:
                print("\nCouldn't find out, if it is y/n, I'm going, Adios!")
    else:
        print("Ugh, i don't beleive if", sys.argv[2], "exist")

if __name__ == "__main__":
    try:
        if (sys.argv[1] == "-h") or (sys.argv[1] == "--help") or (sys.argv[1] == ""):
            print('''This tool is used to encrypt the contents under a file\n''')
            hlp()

        elif (sys.argv[1] == "-bs64") or (sys.argv[1] == "--base64"):
            bas64()

        elif (sys.argv[1] == "-hx") or (sys.argv[1] == "--hexa"):
            hexa()

        elif (sys.argv[1] == "-oc") or (sys.argv[1] == "--octal"):
            octal()

        else:
            print('''No No No, this is not how it works\nlet me tell you an EXAMPLE below:\n''')
            hlp()

    except IndexError:
            print('''This tool is used to encrypt the contents under a file\n''')
            hlp()
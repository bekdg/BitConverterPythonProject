import time
import main


def help():
    print("""
                    ====================
                    ||!!!!WELCOME!!!!! ||
                    =====================
    This is a complete program that converts digital number systems
    from one to another.

    You can type help to get help at any step of the program.
    ===============================================================
    short-listes
    
    => bnr ----- Binary
    => dcml ---- Decimal
    => oct ----- Octal
    => hxd ----- HexaDecimal

    => help ---- Get this message again
    => quit ---- Quit the Program

    """)


def close():
    confirm = input(
        "Are you sure you want to quit? (y/Y) or other keys to cancel: ")
    if confirm.lower() == "y":

        print("""
        The program will close in 5 seconds...

        Thank you for using this program! 
        Please don't hesitate to contact us if you need to:

        Developed by: Bekan Deresa (BekDG)
                        +251939961697
                ....
        """)
        time.sleep(5)
        quit()


help()
input("Press Enter to begin the program....... ")

# the converter loop
while True:
    # from and to
    convertFrom = input("Convert From: ")
    convertFrom = convertFrom.lower()
    if convertFrom == "quit":
        close()
        continue
    convertTo = input("Convert To: ")
    convertTo = convertTo.lower()
    if convertTo == "quit":
        close()
        continue

    # case of binary

    if convertFrom == "bnr":
        binary = input("Enter the Binary: ")
        if binary == "quit":
            close()
            continue
        # instantiate the class
        bnr = main.Binary(binary)
        if convertTo == "dcml":
            print(f"Decimal Equivalent: {bnr.toDecimal()}")
        elif convertTo == "oct":
            print(f"Octal Equivalent: {bnr.toOctal()}")
        elif convertTo == "hxd":
            print(f"Hexa-Decimal Equivalent: {bnr.toHexaDecimal()}")

        elif convertFrom == "help":
            help()
            continue
        else:
            print("Invalid Input! Try agian or type 'help' to get some help")
            continue

    # case of decimal
    elif convertFrom == "dcml":
        decimal = input("Enter the Decimal: ")
        if decimal == "quit":
            close()
            continue
        # instantiate the class
        dcml = main.Decimal(decimal)
        if convertTo == "bnr":
            print(f"Binary Equivalent: {dcml.toBinary()}")
        elif convertTo == "oct":
            print(f"Octal Equivalent: {dcml.toOctal()}")
        elif convertTo == "hxd":
            print(f"Hexa-Decimal Equivalent: {dcml.toHexaDecimal()}")

        elif convertFrom == "help":
            help()
            continue
        else:
            print("Invalid Input! Try agian or type 'help' to get some help")
            continue

    # case of octal
    elif convertFrom == "oct":
        octal = input("Enter the Octal: ")
        if octal == "quit":
            close()
            continue
        # instantiate the class
        octl = main.Octal(octal)
        if convertTo == "bnr":
            print(f"Binary Equivalent: {octl.toBinary()}")
        elif convertTo == "dcml":
            print(f"Decimal Equivalent: {octl.toDecimal()}")
        elif convertTo == "hxd":
            print(f"Hexa-Decimal Equivalent: {octl.toHexaDecimal()}")

        elif convertFrom == "help":
            help()
            continue
        else:
            print("Invalid Input! Try agian or type 'help' to get some help")
            continue

    # case of hexadecimal
    elif convertFrom == "hxd":
        hexaDcml = input("Enter the Hexa-Decimal: ")
        if hexaDcml == "quit":
            close()
            continue
        # instantiate the class
        hxd = main.HexaDecimal(hexaDcml)
        if convertTo == "bnr":
            print(f"Binary Equivalent: {hxd.toBinary()}")
        elif convertTo == "dcml":
            print(f"Decimal Equivalent: {hxd.toDecimal()}")
        elif convertTo == "oct":
            print(f"Octal Equivalent: {hxd.toOctal()}")

        elif convertFrom == "help":
            help()
            continue
        else:
            print("Invalid Input! Try agian or type 'help' to get some help")
            continue

    elif convertFrom == "help":
        help()
        continue
    else:
        print("Invalid Input! Try agian or type 'help' to get some help.")
        continue

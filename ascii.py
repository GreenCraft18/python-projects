ASCIItype = input("Do you want to find the ASCII code, or the character that corresponds to a ASCII code? (code, character) ")

if ASCIItype.lower() == "code":
    ASCIIchr = input("What letter do you wanna find the ASCII code of? ")

    letter_count = len("".join(filter(str.isalpha, ASCIIchr)))

    int(letter_count)
    
    if letter_count > 1:
        print("You need to enter only ONE letter. Please try again.")
        exit()
    else:
        print(f"The ASCII code of {ASCIIchr} is", ord(ASCIIchr), "or", ord(ASCIIchr) + 32, "if you want the lowercase version.")
elif ASCIItype.lower() == "character":
    try:
        ASCIIcode = int(input("What number do you wanna find the ASCII character that it corresponds to? "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        exit()

    letter_count = len("".join(filter(str.isalpha, str(ASCIIcode))))

    int(ASCIIcode)

    int(letter_count)

    if letter_count > 3:
        print("Only 2 or 3 numbers are allowed. Try again.")
        exit()
    else:
        print(f"The ASCII letter of {ASCIIcode} is ", chr(ASCIIcode))

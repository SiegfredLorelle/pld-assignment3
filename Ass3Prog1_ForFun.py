"""PROG 1: Added some stuffs
Create a program that will ask for name, age and address. 
Display those details in the following format.
Hi, my name is _____. I am ____ years old and I live in _____ ."""

#Prog1 - 1st try, only for fun
import sys

def FuncName():
    Name = input("Please enter your NAME:  ")
    print()
    return Name

def FuncAge():
    Age = int(input("Please enter you AGE in years:  "))
    return Age

def AgeChecker(FinalAgeF):
    if FinalAgeF <= 0 or FinalAge >= 120:   #wala nmn atang mas matanda sa 120 
        print()                             #no negative age
        print(FinalAgeF, " is not a VALID AGE!!")
        ValidAge = False 
    else:
        ValidAge = True    
    return ValidAge

def TryAgain(FinalValidAgeF):
    if FinalValidAgeF == False: 
        print()
        print("Type '1' to enter a valid age.")
        print("Type '2' to exit the program. ")
        OneOrTwo = input("Reply:  ")
        return OneOrTwo

def FuncAddress():
    Address = (input("Please enter your ADDRESS:  ")) 
    return Address

def FuncFinalDisplay(FinalAddressF,  FinalAgeF, FinalNameF):
    if FinalAgeF == 1:      #1 year old (singular)
        print(f"Hi, my name is {FinalNameF}. I am {FinalAgeF} year old and I live in {FinalAddressF}.")
    else:
        print(f"Hi, my name is {FinalNameF}. I am {FinalAgeF} years old and I live in {FinalAddressF}.")

# Step 1 - ask name then save to var
print("Good Day Mate!!")
FinalName = FuncName()

#Step 2 - ask age them save to var
FinalAge = FuncAge()

#Step 3.0 - check if age is valid 
FinalValidAge = AgeChecker(FinalAge)

#Step 3.1 - if not, ask if want to try again, if valid, go step 4
FinalOneOrTwo = TryAgain(FinalValidAge)

#Step 3.2 -  if no stop the prog, if yes go back to step 2
if FinalOneOrTwo == str("2"):
    print()
    print("Thank you for trying!")
    print()
    sys.exit()

while FinalOneOrTwo == str("1"):
     print()
     print("Please try again :) ")
     FinalAge = FuncAge()
     FinalValidAge = AgeChecker(FinalAge)
     FinalOneOrTwo = TryAgain(FinalValidAge)
           
if FinalOneOrTwo is None:
     print()
else:
    print()
    print("That was your last chance!! Restart the program if you want to try again!")
    print()
    sys.exit()

#Step 4 - ask address then save to var
FinalAdress = FuncAddress()

#Step 5 - display name age & address
print()
FuncFinalDisplay(FinalAdress,  FinalAge, FinalName)
print()

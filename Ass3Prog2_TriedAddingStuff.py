"""PROG 2:
Create a program that will ask how many apples and oranges you want
to buy. Display the total amount you need to pay if apple price is 
20 pesos and orange is 25. Display the output in the following format.
The total amount is ______."""

#Prog2 - 2nd try. avoided negatives

def FuncNumApple():
    NumApple = int(input("How many APPLES would you like to buy?  "))
    return NumApple

def FuncNumOrange():
    NumOrange = int(input("How many ORANGES would you like to buy?  "))
    return NumOrange

def FuncApplePrice(FinalNumAppleF):
    PriceApple = FinalNumAppleF * 20
    return PriceApple

def FuncOrangePrice(FinalNumOrangeF):
    PriceOrange = FinalNumOrangeF * 25
    return PriceOrange

def FuncTotalPrice(FinalPriceAppleF, FinalPriceOrangeF): 
    TotalPrice = FinalPriceAppleF + FinalPriceOrangeF
    return TotalPrice

def FuncDisplayEachPrice(FinalNumAppleF, FinalNumOrangeF, FinalPriceAppleF, FinalPriceOrangeF):
    print(f"An APPLE cost 20 php & you want x{FinalNumAppleF} apple(s), it would cost {FinalPriceAppleF} php for the apple(s).") 
    print(f"An ORANGE cost 25 php & you want x{FinalNumOrangeF} orange(s), it would cost {FinalPriceOrangeF} php for the orange(s).")

def FuncDisplayTotalPrice(FinalTotalPrice):
    print( f"The total amount is {FinalTotalPrice} php. ")

#Step 0 - prints only
print()
print("Good Day Mate!")
print("APPLES cost 20php each and ORANGES cost 25php each.")
print()

#Step 1 - ask how many apples and save to var
FinalNumApple = FuncNumApple()

#Step 2 - check if apple is not negative
while FinalNumApple < 0:
    print()
    if FinalNumApple < 0:
         print("You cannot buy NEGATVE APPLES!!")
         print()
         print("Please try again. ")
         FinalNumApple = FuncNumApple()

#Step 3 - ask how many oranges and save to var
print()
FinalNumOrange = FuncNumOrange()

#Step 4 - check if orange is not negative
while  FinalNumOrange < 0:
    print()
    if FinalNumOrange < 0:
        print("You cannot buy NEGATVE ORANGES!!")
        print()
        print("Please try again. ")
        FinalNumOrange = FuncNumOrange()

#Step 5 - multiply apple to 20, multiply orange to 25
FinalPriceApple = FuncApplePrice(FinalNumApple)

#Step 6 - multiply orange to 25 then save to var
FinalPriceOrange = FuncOrangePrice(FinalNumOrange)

#Step 7 - add apple price and orange price
FinalTotalPrice = FuncTotalPrice(FinalPriceApple, FinalPriceOrange)

#Step 8 - display total apple & orange price
print()
FuncDisplayEachPrice(FinalNumApple, FinalNumOrange, FinalPriceApple, FinalPriceOrange)

#Step 9 - display total price
print()
FuncDisplayTotalPrice(FinalTotalPrice)
print()
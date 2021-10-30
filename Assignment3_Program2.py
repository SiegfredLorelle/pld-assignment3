"""Create a program that will ask how many apples and oranges you want
to buy. Display the total amount you need to pay if apple price is 
20 pesos and orange is 25. Display the output in the following format.
The total amount is ______."""

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

def FuncDisplayTotalPrice(FinalTotalPrice):
    print( f"The total amount is {FinalTotalPrice} pesos. ")

#Step 1 - ask how many apples and save to var
print("Good Day Mate!")
FinalNumApple = FuncNumApple()

#Step 2 - ask how many oranges and save to var
FinalNumOrange = FuncNumOrange()

#Step 3 - multiply apple to 20 then save to var
FinalPriceApple = FuncApplePrice(FinalNumApple)

#Step 4 - multiply orange to 25 then save to var
FinalPriceOrange = FuncOrangePrice(FinalNumOrange)

#Step 5 - add apple price and orange price
FinalTotalPrice = FuncTotalPrice(FinalPriceApple, FinalPriceOrange)

#Step 5 - Display total price
print()
FuncDisplayTotalPrice(FinalTotalPrice)
print()

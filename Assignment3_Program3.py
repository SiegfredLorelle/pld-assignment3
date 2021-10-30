"""PROG 3: 
Create a program which you will enter the amount of money you have,
it will also ask for the price of an apple. Display the maximum number
of apples that you can buy and the remaining money that you will have.
Display the output in the following format.
You can buy ___ apples and your change is ___ pesos."""

import math

def FuncMoneyStart():
    MoneyStart = int(input("How much money do you have?  "))
    return MoneyStart

def FuncPriceApple():
    PriceApple = int(input("How much is an apple?  "))
    return PriceApple

def FuncBoughtApple(FinalMoneyStartF, FinalPriceAppleF):
    FuncBoughtApple = math.floor (FinalMoneyStartF / FinalPriceAppleF)
    return FuncBoughtApple

def FuncMoneyLeft(FinalMoneyStartF, FinalPriceAppleF):
    MoneyLeft = FinalMoneyStartF % FinalPriceAppleF
    return MoneyLeft 

def FuncFinalDisplay(FinalBoughtAppleF, FinalMoneyLeftF):
    print(f"You can buy {FinalBoughtAppleF} apple(s) and your change is {FinalMoneyLeftF} pesos.")
    
#Step 1 - ask how much money then save to var
print("Good Day Mate!!")
FinalMoneyStart = FuncMoneyStart()

#Step 2 - ask how much is an apple and save to var
FinalPriceApple = FuncPriceApple()

#Step 3 - divide apple price to money (max apple bought)
FinalBoughtApple = FuncBoughtApple (FinalMoneyStart, FinalPriceApple)

#Step 4 - remainder of money divided by apple (money left)
FinalMoneyLeft = FuncMoneyLeft (FinalMoneyStart, FinalPriceApple)

#Step 5 - Display apple max apple bought and money left
print()
FuncFinalDisplay(FinalBoughtApple, FinalMoneyLeft)
print()
"""PROG 3: 
Create a program which you will enter the amount of money you have,
it will also ask for the price of an apple. Display the maximum number
of apples that you can buy and the remaining money that you will have.
Display the output in the following format.
You can buy ___ apples and your change is ___ pesos."""

#Prog 3 - 2nd try, 
#centavos, avoid negative currency

import math

def FuncMoneyStart():
    MoneyStart = float(input("How much MONEY do you have?  "))
    MoneyStart = round(MoneyStart,2)
    return MoneyStart

def FuncPriceApple():
    PriceApple = float(input("How much is an APPLE?  "))
    PriceApple = round(PriceApple,2)
    return PriceApple

def FuncBoughtApple(FinalMoneyStartF, FinalPriceAppleF):
    FuncBoughtApple = math.floor (FinalMoneyStartF / FinalPriceAppleF)
    return FuncBoughtApple

def FuncMoneyLeftWithNoDeci(FinalMoneyStartF, FinalPriceAppleF):
    MoneyLeftWithNoDeci = math.floor (FinalMoneyStartF % FinalPriceAppleF)
    return MoneyLeftWithNoDeci 

def FuncMoneyLeftWithDeci(FinalMoneyStartF, FinalPriceAppleF):
    MoneyLeftWithDeci = FinalMoneyStartF % FinalPriceAppleF
    return MoneyLeftWithDeci 

def FuncMoneyLeftCentavo(FinalMoneyLeftWithDeciF, FinalLeftPesosF):
    MoneyLeftCentavo = (FinalMoneyLeftWithDeciF - FinalLeftPesosF) * 100
    return MoneyLeftCentavo 

def FuncFinalDisplay(FinalBoughtAppleF, FinalMoneyLeftPesosF, FinalMoneyLeftCentavoF):
    print(f"You can buy {FinalBoughtAppleF} apple(s) and your change is {FinalMoneyLeftPesosF} pesos and {FinalMoneyLeftCentavoF:.0f} centavos.")
    
#Step 1 - ask how much money then save to var
print()
print("Good Day Mate!!")
FinalMoneyStart = FuncMoneyStart()

#Step 2 - ask how much is an apple and save to var
FinalPriceApple = FuncPriceApple()

#Step 3 - check negatives & zero currencies
while FinalMoneyStart <= 0 or FinalPriceApple <= 0 or FinalPriceApple > FinalMoneyStart:
    print()

    if FinalMoneyStart <= 0 and FinalPriceApple > 0:
        if FinalMoneyStart == 0:
            print("You cannot buy with ZERO balance!")
        else:
            print("You cannot buy with NEGATIVE balance!")
    
    elif FinalPriceApple <= 0 and FinalMoneyStart > 0 :
        if FinalPriceApple == 0:
            print("Apples are not sold for free!")
        else:
            print("Apples cannot be sold for a NEGATIVE price!")
    
    elif FinalMoneyStart <= 0 and FinalPriceApple <= 0:
        if FinalMoneyStart == 0 and FinalPriceApple == 0:
            print("No ZEROS please!")
        else:
            print("No NEGATIVES please!")

    elif FinalPriceApple > FinalMoneyStart:
        print("Sorry, you are too broke to buy an apple. ")

    print()
    print("Please try again. ")
    FinalMoneyStart = FuncMoneyStart()
    FinalPriceApple = FuncPriceApple()


#Step 4 - divide apple price to money (max apple bought)
FinalBoughtApple = FuncBoughtApple (FinalMoneyStart, FinalPriceApple)

#Step 5 - money left with no deci (money left in pesos)
FinalMoneyLeftPesos = FuncMoneyLeftWithNoDeci (FinalMoneyStart, FinalPriceApple)

#Step 6 - money left with deci (need sa centavo)
FinalMoneyLeftWithDeci = FuncMoneyLeftWithDeci(FinalMoneyStart, FinalPriceApple)

#Step 7 - (money left in centavos)
FinalMoneyLeftCentavo = FuncMoneyLeftCentavo (FinalMoneyLeftWithDeci, FinalMoneyLeftPesos)

#Step 8 - Display max apple bought and money left
print()
FuncFinalDisplay(FinalBoughtApple, FinalMoneyLeftPesos, FinalMoneyLeftCentavo)
print()
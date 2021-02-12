print("Rules:\nNIM is a simple game where you try to be the one that takes the last coin in the pile. \nThis NIM-bot is really good at NIM, but do try to beat him.\nThe human always plays the first move against this bot.\n\n")
amount=input('With how many coins do you want to play NIM? Minimal amount is 12 coins. ')
try:
    amount=int(amount)
    i=int(amount*15.5)
except ValueError:
    print("That is not a number, NIM-bot decides the game will be played with 12 coins.")
    amount=12
if amount < 12:
    print("The NIM-bot notices with less coins than he allows. He adds the needed coins for the least coins he allows!")
    amountadd=12-amount
    amount=amount+amountadd

while True:
    if amount != 0 or amount<0:
        minusplayer=input("How many coins do you want to remove? (1,2,3), the current amount of coins is " + str(amount) + " coins. ")
        try:
            minusplayer=int(minusplayer)
        except ValueError:
            print("That's not a number!")
            continue
        if minusplayer==1 or minusplayer==2 or minusplayer==3:
            amount=amount-minusplayer
        else:
            minusplayer=1
            print("That is not a valid number! CHEATER!! So instead I chose 1 for you.")
            last_amount=amount
            amount=amount-minusplayer
    else:
        print("The NIM bot won.")
        quit()
    if amount != 0 or amount<0:
        if (amount-1)%4==0:
            minusbot=1
        elif (amount-2)%4==0:
            minusbot=2
        elif (amount-3)%4==0:
            minusbot=3
        else:
            weirdnumber=round(((amount%minusplayer)^amount)%3+2^i)
            print(weirdnumber)
            if weirdnumber%3==0:
                minusbot=3
            elif weirdnumber%2==0:
                minusbot=2
            elif weirdnumber%3==0:
                minusbot=1
        amount=amount-minusbot
        print("The NIM bot took " + str(minusbot) + " coins!")
    else:
        print("You beat the unbeatable NIM-bot! HOW???")
        quit()

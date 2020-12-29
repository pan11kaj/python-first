import  random
print("guess number game")
print("guess a number (between 1-9)")
guessnum = int(input('enter your number:-'))
chances = 1
number = random.randrange(1,9)
while chances<5:
    if(guessnum < number  ):
        print('to loo please try again')
        guessnum = int(input('enter your number:'))
        chances=chances+1
    if(guessnum > number   ):
        print('to high please try again')
        guessnum = int(input('enter your number:'))
        chances=chances+1
    if(guessnum == number):
        print('congratulations you win the game')
        break
    if( chances ==5):
        print('you lose the game the number is',number)
        break
   
        

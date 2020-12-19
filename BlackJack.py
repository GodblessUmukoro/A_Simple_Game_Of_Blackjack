import random
maxBet=500 
minBet=2
cardNum1=[1,2,3,4,5,6,7,8,9,10,12,13]
cardNum2=[1,2,3,4,5,6,7,8,9,10,12,13]
#The random cards picked by the system.



num1=random.choice(cardNum1)
num2=random.choice(cardNum2)
#these pick the two random cards

def shakeDice():#select a radom card from both of the list
    
    dice=num1+num2
    return dice



def showCard():#displays the random card picked byt the user.
    card=('Your card number is {} and {}.'.format(num1,num2))
    return card


def blackjack():
    reward=0
    stake=int(input('Enter stake amount for your game session:'))#the amount player want to start with
    card=shakeDice()#this is the dice number
    if stake>=minBet and stake<=maxBet:
        if card%2==0:#even card
            reward=stake*2
        elif card%2==1:#odd card
            reward=stake*2
        elif card>13:
            reward=stake*2
        elif card<13:
            reward=stake*2
        elif reward==13:
            reward=10*stake
        elif cardNum1==cardNum2:#if both the cards are the same 
            reward=stake*7
        
        else:
            reward=0                 
    else:
        reward='The min staking amount is $2 and the maximum is $500.'
        #alert user if the amount is not the between the given range
  
        
    
    print(showCard())#display the card picked by the system
    print('Your winning for this game session is:',reward)#shows the reward for each session played by the user
    return reward 


def playAgain():#allows the user to play again and start another session
   
    playAgain=str(input('Enter yes or no to play again:'))
    reply=playAgain.lower()
    if reply=='yes':
        newSession='yes'
    elif reply=='no':#an option to opt out of the game
        newSession='no'
    else:
        return 'invalid input'
    return newSession

def Help(): #gives instructions on how to play black jack
    print('***Game of Black-Jack***')
    print("***************************")
    print('**How to play**')
    print('1. Enter your stake for the game session.')
    print("2. Stake must be in this range(Max. is $500, Min. is $2).\n   You will be assigned two random card numbers which determine your winnings.")
    print('3. Show numbers for the two card')
    print('4. Display the gambling results:\n * Current  cash on hand\n * Numbers of winnings \n * Total number of game sessions played so far')
    print('5. Enter no in the playagain option to Quit or yes to continue.')

    return ''
print(Help())


def totalReward():
    newSession='yes' #allows the user the choice of another session
    totalReward=0
    count=0#counts the number of sessions played
    total=0#gets the total amount earned by the player
    List=[]#saves all the wins from different session in a list container
    replay=None#make replay default, set to none
    while newSession=='yes':
        result=blackjack()
        totalReward=result
        List.append(totalReward)# append the reward to the list
        print('List of amount won for each session:',List)#display the amount for each session
        replay=playAgain()# check for replay
        if replay=='no':#if replay is false or no
            for i in List: #add all the reward won and count the total sessions played by the user
                count+=1#total sessions of games
                total+=i#total money won
            newSession='no'
    
        
    
    
    return ('In {} game sessions, you won a total of ${}.'.format(count,total))

print(totalReward())#this runs the entire game for the black jack


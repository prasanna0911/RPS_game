import sys
import random

arr=['Rock','Paper','Scissor']

print('\n--------------\n')
def rps():
    gamecount=0
    wincount=0
    losscount=0
    def play_rps():
        player=input('Enter 1 for Rock \nEnter 2 for Paper \nEnter 3 for Scissor \n')
        nonlocal gamecount,wincount,losscount
        if player not in ['1','2','3']:
            print("You must enter 1, 2, or 3.")
            play_rps()
        playerchoice=int(player)
        computerchoice = int(random.choice('123'))
        print('')
        print(f'You Chose {arr[playerchoice-1]}')
        print(f'Computer Chose {arr[computerchoice-1]}')
        print('')
        if playerchoice==computerchoice:
            print('Match Draw')
        elif playerchoice==1 and computerchoice==3:
            wincount+=1
            print("🎉 You win!")
        elif playerchoice==2 and computerchoice==1:
            wincount+=1
            print("🎉 You win!")
        elif playerchoice==3 and computerchoice==2:
            wincount+=1
            print("🎉 You win!")
        else:
            losscount+=1
            print('you lose')
        
        gamecount+=1

        print(f"\nGame count: {gamecount}")
        print(f"\nPlayer wins: {wincount}")
        print(f"\nPython wins: {losscount}")
        while True:
            playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")
            if playagain.lower() not in ['y','q']:
                print('Please press y or q')
                continue
            else:
                break
        if playagain.lower() == "y":
            return play_rps()
        else:
            print(f"\nYou won {wincount} out of {gamecount} games")
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            print('--------------\n')
            sys.exit('Bye')
    return play_rps

play=rps()
play()
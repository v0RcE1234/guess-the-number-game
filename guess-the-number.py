import random
import time

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

max_number=int(input('What should the maximum number be: '))
answer=random.randrange(1, max_number+1)
print('Computer is choosing number...')
time.sleep(2)
isguesscorrect=False
guess_number='1'
while isguesscorrect==False:
    str_guess=input('What is your guess #'+guess_number+': ')
    if RepresentsInt(str_guess):
        guess=int(str_guess)
        if guess > answer:
            print('Guess is too high, try again.')
        if guess < answer:
            print('Guess is too low, try again.')
        if guess==answer:
            if guess_number=='1':
                print('You are correct, yay. You took 1 guess.')
            else:
                print ('You are correct, yay. You took '+str(int(guess_number))+' guesses.')
            isguesscorrect=True
        guess_number=str(int(guess_number)+1)
    else:
        print('Please enter an integer')
    
'''
snake<gun
gun<water
water<snake
'''
import random

elements=['snake','water','gun']
computer=random.choice(elements)
user=input("Choose:snake,water,gun->\n")

if(computer=='snake' and user.lower()=='gun'):
    print('You win')
elif(computer=='gun' and user.lower()=='snake'):
    print('You lose')
elif(computer=='water' and user.lower()=='snake'):
    print("You win")
elif(computer=='snake' and user.lower()=='water'):
    print("You lose")
elif(computer=='gun' and user.lower()=='water'):
    print("You win")
elif(computer=='water' and user.lower()=='gun'):
    print("You lose")
else:
    print("Game is tie")
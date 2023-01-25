import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=[rock,paper,scissors]
#Write your code below this line 👇
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors :"))
print(game[choice])
comp=random.randint(0,2)
print(game[comp])
if choice<0 and choice>=3:
  print("You typed an invalid number, you lose!")
elif choice==0 and comp==2:
  print("You Win!")
elif choice==2 and comp==0:
  print("You Lose!")
elif choice>comp:
  print("You Win!")
elif comp>choice:
  print("You Lose!")
else:
  print("It's a draw")
  
  

  
  
  
  
  
  


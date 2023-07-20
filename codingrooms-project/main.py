# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1


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

#Write your code below this line 👇
choosen_value= int(input("what do you choose?Type 0 for Rock, 1 for paper or 2 for Scissors\n"))
if choosen_value==0:
    print(rock)
elif choosen_value==1:
    print(paper)
elif choosen_value==2:
    print(scissors)

print("Computer chose")
choosen_sign=random.randint(0,2)
if choosen_sign==0:
    print(rock)
elif choosen_sign==1:
    print(paper)
elif choosen_sign==2:
    print(scissors)

if choosen_value==0:
    if choosen_sign==0:
        print("Draw")
    elif choosen_sign==1:
        print("lose")
    elif choosen_sign==2:
        print("win")
if choosen_value==1:
    if choosen_sign==0:
        print("win")
    elif choosen_sign==1:
        print("draw")
    elif choosen_sign==2:
        print("lose")
if choosen_value==2:
    if choosen_sign==0:
        print("lose")
    elif choosen_sign==1:
        print("win")
    elif choosen_sign==2:
        print("draw")

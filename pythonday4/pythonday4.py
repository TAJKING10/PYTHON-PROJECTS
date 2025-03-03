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

game__images=[rock, paper , scissors]
choice = (input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n0/1/2:"))
computer_choice= random.randint(0,2)

if not choice.isdigit():
    print("u did not write a number rerun")
else:
    choice=int(choice)
    if choice == 2:
        print ("u picked siccors +{siccors}")
        print(game__images[choice])
    elif choice == 1:
        print ("u picked paper {paper}")
        print(game__images[choice])

    elif choice == 0:
        print ("u picked rock {rock}")
        print(game__images[choice])

    if computer_choice == 0:
        print("the computer choice is rock {rock}")
        print(game__images[computer_choice])

        if choice == 0:
            print("it is a draw")
        elif choice == 1:
            print("u win")
        elif choice == 2:
            print("u lose")
    
    
    
    
    
    
    if computer_choice == 1:
        print("the computer choice is paper {paper}")
        print(game__images[computer_choice])

        if choice == 1:
            print("it is a draw")
        elif choice == 2:
            print("u win")
        elif choice == 0:
            print("u lose")
    
    
    
    
    if computer_choice == 2:
        print("the computer choice is siccors {siccors}")       
        print(game__images[computer_choice])

        if choice == 2:
            print("it is a draw")
        elif choice == 0:
            print("u win")
        elif choice == 1:
            print("u lose")
    
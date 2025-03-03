from art import logo, vs
from gamedata import data
import random
import os


def format_data(account):
   accountName = account["name"]
   accountDesc = account["description"]
   accountCountry = account["country"]
   return f"{accountName}, a  {accountDesc} , from  {accountCountry}"
def check_answer(user_guess, Afollowers, Bfollowers):
    if Afollowers> Bfollowers:
       return user_guess == "a"
    else:
       return user_guess == "b"

Baccount = random.choice(data)
print(logo)
score = 0


GAMESHOULDCONTINUE = True
while GAMESHOULDCONTINUE:
   
    Aaccount = Baccount
    Baccount = random.choice(data)

    if Aaccount == Baccount:
     Baccount = random.choice(data)

    print(f"Compare A {format_data(Aaccount)}")
    print(vs)
    print(f"Compare B {format_data(Baccount)}")

    guess = input("guess who has more followers TYPE A OR B ").lower()
    # print("\n" * 20)
    print(logo)

    AfollowerAcoount = Aaccount["follower_count"]
    BfollowerAccount = Baccount["follower_count"]
    is_correct = check_answer(guess, AfollowerAcoount, BfollowerAccount)
    if is_correct:
     score  += 1
     os.system('cls')
     print(f"ur answer is correct :{score}")
    else:
     print(f"sorry wrong answer ur score is :{score}")
     GAMESHOULDCONTINUE = False
     








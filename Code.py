# Blackjack

import random

def dealer_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)== 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
def compare(user_score,computer_score):
    if user_score>21 or computer_score>21:
        return"You went over. you lose"
    if user_score==computer_score:
        return"Draw"
    elif computer_score==0:
        return"you lose opponent ha blackjack."
    elif user_score==0:
        return "you win blackjack."
    elif user_score>21:
        return "you went over you lose."
    elif computer_score>21:
        return"opponent went over.You win"
    elif user_score> computer_score:
        return "You win"
    else:
        return "you lose."

def playgame():
    user_card=[]
    computer_card=[]
    is_game_over= False

    for _ in range(0,2):
        user_card.append(dealer_card())
        computer_card.append(dealer_card())


    while not is_game_over:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)
        print(f"Your cards:{user_card}, current score:{user_score}.")
        print(f"Computer's first card:{computer_card[0]}")
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input(" 'y' to get another card or 'n' to pass.")
            if user_should_deal=="y":
                user_card.append(dealer_card())
            else:
                is_game_over=True

    while computer_score!=0 and computer_score<17:
        computer_card.append(dealer_card())
        computer_score=calculate_score(computer_card)
    print(f"computer final hand {computer_card} final score: {computer_score}")
    print (compare(user_score,computer_score))

while input("Do you want to play a game of blackjack? type 'y or 'n'") =='y':
    playgame()
import random

# One player Blackjack vs the computer (Dealer)
# Dealer sticks on 17+ 
# One dealer card will be shown at start of deal and only one deck will be used
# Ace will only be 11

# Making deck of cards with values
deck_value = {"A": 11, "K": 10, "Q": 10, "J": 10, "2": 2, "3": 3, "4": 4, 
              "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10
              }


full_deck = []

for cards in range(4):
    for card in deck_value:
        full_deck.append(card)

#Welcome Message
print("----------------------------------------------------------------------------")
print("Welcome to Blackjack. Dealer must stick on 17+ and show one card. Good luck.")
print("----------------------------------------------------------------------------")

# Blackjack checker, will be used during the deal

def is_blackjack_check(card_1, card_2):
    if deck_value.get(card_1) + deck_value.get(card_2) == 21:
        return False

# Deal the player cards


def deal():
    deck = full_deck
    dealer_cards = []
    user_cards = []


    dealer_card_1 = random.choice(deck)
    deck.remove(dealer_card_1)
    dealer_cards.append(dealer_card_1)

    dealer_card_2 = random.choice(deck)
    deck.remove(dealer_card_2)
    dealer_cards.append(dealer_card_2)

    user_card_1 = random.choice(deck)
    deck.remove(user_card_1)
    user_cards.append(user_card_1)

    user_card_2 = random.choice(deck)
    deck.remove(user_card_2)
    user_cards.append(user_card_2)

    print("Dealer shows: {}".format(dealer_card_1))
    print("Your cards are {}".format(user_cards))
    print("----------------------------------------------------------------------------")

    
    #Check if either player has blackjack

    if is_blackjack_check(user_cards[0], user_cards[1]) == False:
        print("You have Blackjack!")
        if is_blackjack_check(dealer_cards[0], dealer_cards[1]) == False:
            print("Computer has Blackjack as well. It's a push.")
            return False
        else:
            print("You win!")
            return False
    elif is_blackjack_check(dealer_cards[0], dealer_cards[1]) == False:
        print("Dealer has Blackjack.")
        return False

    #When no players has blackjack, the dealt cards and deck will be returned


    return [dealer_cards, user_cards, deck]


    
# Score Calculator


def total_score(card_1, card_2):
    return deck_value.get(card_1) + deck_value.get(card_2)



#Function for taking another card
def another_card(deck):
    deck = deck
    card = random.choice(deck)
    deck.remove(card)

    print("Hit card is {} ".format(card))
    card_value = deck_value.get(card)
    return [card_value, deck]

# User turn

def user_turn(score, deck):
   

    if score > 21:
        print("Bust!")
        return [22, deck]
    elif score == 21:
        print("21!")
        return [score, deck]

    print("Your current score is {} ".format(score))
    hit_or_stick = input("Would you like another card? (y/n) ").lower()

    if hit_or_stick == "n":
        print("Sticking on {} ".format(score))
        print("----------------------------------------------------------------------------")
        return [score, deck]
    else:
        hit_card = another_card(deck)
        new_card_value = hit_card[0]
        new_deck = hit_card[1]
        user_update_score = new_card_value + score
        
        
        
        # run function again with new score
        return user_turn(user_update_score, new_deck)

#Dealer turn

def dealer_turn(dealer_score, user_score, deck):
    current_deck = deck
    dealer_score = dealer_score
    print("Dealer score is {} ".format(dealer_score))

    while dealer_score < 17:
        dealer_hit = another_card(current_deck)
        new_dealer_card = dealer_hit[0]
        current_deck = dealer_hit[1]
        dealer_score += new_dealer_card
        print("Dealer score is {} ".format(dealer_score))


    return [dealer_score, user_score]

# Final score

def results(dealer_score, user_score):
    if dealer_score > 21:
        print("Dealer busts. You win.")   
    elif dealer_score > user_score:
        print("Dealer wins with {}.".format(dealer_score))
    elif dealer_score < user_score:
        print("You win with {} ".format(user_score))
    elif dealer_score == user_score:
        print("It's a push!")

# Game

def game():
    new_deal = deal()

    if new_deal == False:
        print("Thanks for playing.")
        exit()


    dealer_cards = new_deal[0]
    user_cards = new_deal[1]
    current_deck = new_deal[2]

    #Getting user score
    user_score = total_score(user_cards[0], user_cards[1])

    #Getting dealer score 
    dealer_score = total_score(dealer_cards[0], dealer_cards[1])


    #User turn 
    user_finished_turn = user_turn(user_score, current_deck)
   
    if user_finished_turn[0] == 22:
        print("Thanks for playing.")
        exit()
    else:
        final_user_score = user_finished_turn[0]
        deck_left = user_finished_turn[1]
        final_scores = dealer_turn(dealer_score, final_user_score, deck_left)
        results(final_scores[0], final_scores[1])



game()





    











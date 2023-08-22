import random
import os
import time
from art import logo_top
from art import logo_bottom

def is_linux():
    return os.name == "posix"

def clear():
    """Clear the console."""
    os.system("clear") if is_linux() else os.system("cls")

def deal_card():
    """ Return a random card from the deck. """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_number = random.randint(0, len(cards) - 1)
    random_card = cards[random_number]
    return random_card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def display_verdict(user_score, computer_score):

    if user_score == computer_score:
        return "Game ends with a draw 😇"
    elif computer_score == 0:
        return "Opponent has Blackjack. You lose 😱"
    elif user_score == 0:
        return "You have Blackjack. You win! 😎"
    elif user_score > 21:
        return "You went over 21. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over 21. You win 😄"
    elif user_score > computer_score:
        return "You win 😄"
    else:
        return "You lose 😭"

def display_cards(cards):
    cards_dict = { 
        1: ["🂡", "🂱", "🃁", "🃑"],
        2: ["🂢", "🂲", "🃂", "🃒"],
        3: ["🂣", "🂳", "🃃", "🃓"],
        4: ["🂤", "🂴", "🃄", "🃔"],
        5: ["🂥", "🂵", "🃅", "🃕"],
        6: ["🂦", "🂶", "🃆", "🃖"],
        7: ["🂧", "🂷", "🃇", "🃗"],
        8: ["🂨", "🂸", "🃈", "🃘"],
        9: ["🂩", "🂹", "🃉", "🃙"],
        10: ["🂪", "🂺", "🃊", "🃚", "🂫", "🂻", "🃋", "🃛", "🂬", "🂼", "🃌", "🃜", "🂭", "🂽", "🃍", "🃝", "🂮", "🂾", "🃎", "🃞"],
        11: ["🂡", "🂱", "🃁", "🃑"]
    }
    
    for index in range(len(cards)):
        card_types = cards_dict[cards[index]]
        card = random.choice(card_types)
        is_first_item = "    " if index == 0 else ""
        is_last_item = "\n" if index == len(cards) - 1 else " "
        
        print(is_first_item + card, end = is_last_item)

def verdict(user_cards, computer_cards, user_score, computer_score):
    print("♠♥♦♣ ♠♥♦♣ ♠♥♦♣ ♠♥♦♣ ♠♥♦♣ ♠♥♦♣ ♠♥♦♣ ♠♥♦♣ ♠♥♦♣ ♠♥♦♣ ♠♥♦♣ ♠♥♦♣")
    display_user_score = 21 if user_score == 0 else user_score
    display_computer_score = 21 if computer_score == 0 else computer_score
    print(f"  Your final hand: {user_cards}, current score: {display_user_score}")
    display_cards(user_cards)
    print(f"  Computer's final hand: {computer_cards}, current score: {display_computer_score}")
    display_cards(computer_cards)
    print(display_verdict(user_score, computer_score))

def play_blackjack():

    if input("Do you want to play a game of Blackjack? Type 'y', or 'n': ") == 'y':
        
        clear()
        print(logo_top)
        print(logo_bottom)
        
        user_cards = []
        computer_cards = []
        
        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())
            
        is_game_over = False
        
        while not is_game_over:
            
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f"  Your cards: {user_cards}, current score: {user_score}")
            display_cards(user_cards)
            print(f"  Computer's first card: {computer_cards[0]}")
            display_cards([computer_cards[0]])
    
            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True
            else:
                draw_card = input("Type 'y' to draw another card and hit, otherwise type 'n' to stand: ")
    
                if draw_card == "y":
                    user_cards.append(deal_card())
                else:
                    is_game_over = True

                    while computer_score < 17:
                        computer_cards.append(deal_card())
                        computer_score = calculate_score(computer_cards)
        
        verdict(user_cards, computer_cards, user_score, computer_score)
        play_blackjack()

play_blackjack()

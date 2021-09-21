import random
from art import logo
 
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
 
def calculate_score(cards):
    """Calculates the total of the cards dealt."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
 
def compare(user_score, computer_score):
    """Compares the user's score and and computer's score."""
    if user_score == computer_score:
        return "DRAW 👀"
    elif computer_score == 0:
        return "YOU LOSE, computer has scored a Blackjack 🤯"
    elif user_score == 0:
        return "Congratulations, you scored a Blackjack 🥳"
    elif user_score > 21:
        return "You went over 21, YOU LOSE 😭"
    elif computer_score > 21:
        return "YOU WIN, the computer scored over 21 🤯"
    elif user_score == 21:
        return "YOU WIN, Blackjack!!"
        
    elif user_score > computer_score:
        return "YOU WIN 😎"
    elif computer_score > user_score:
        return "YOU LOSE 😭"
 
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
 
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while not is_game_over:    
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}\nYour score: {user_score}")
        print(" ")
        print(f"Computer's first card: {computer_cards[0]}")
        print(" ")
 
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                
                print(logo)
                user_cards.append(deal_card())
            else:
                is_game_over = True
 
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
 
    
    print(logo)
    print(f"Your final hand: {user_cards}\nYour final score: {user_score}")
    print(" ")
    print(f"Computer's final hand: {computer_cards}\nComputer's final score: {computer_score}")
    print(" ")
    print(compare(user_score, computer_score))
 
while input("Do you want to play a game of Blackjack, type 'y' or 'n': ") == "y":
    
    play_game()
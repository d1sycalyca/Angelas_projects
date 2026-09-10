import random
from art import logo

# def winner_calc(user_cards, comp_cards):
#     """A function that calculates the winner of the blackjack game and outputs a string"""
#     user_score = sum(user_cards)
#     comp_score = sum(comp_cards)
#     if user_score <= 21:
#         if user_score > comp_score:
#             return (f"Your final hand: {user_cards} final score: {user_score}"
#                     f" Computers final hand: {comp_cards} final score: {comp_score}"
#                     f" You win!")
#         elif user_score == comp_score:
#             return (f"Your final hand: {user_cards} final score: {user_score}"
#                     f" Computers final hand: {comp_cards} final score: {comp_score}"
#                     f" Its a tie.")
#         else:
#             return (f"Your final hand: {user_cards} final score: {user_score}"
#                     f" Computers final hand: {comp_cards} final score: {comp_score}"
#                     f" You lose.")
#     elif comp_score > 21 and user_score < 21:
#         return (f"Your final hand: {user_cards} final score: {user_score}"
#                 f" Computers final hand: {comp_cards} final score: {comp_score}"
#                 f" You win!")
#     else:
#         return (f"Your final hand: {user_cards} final score: {user_score}"
#                 f" Computers final hand: {comp_cards} final score: {comp_score}"
#                 f" You lose.")
#
# def blackjack():
#     cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
#     my_cards = random.choices(cards,k=2)
#     compy_cards = random.choices(cards,k=2)
#     score = sum(my_cards)
#     d_score = sum(compy_cards)
#     print(f"Your cards are: {my_cards} Current score: {score}"
#           f" Computers first card is {compy_cards[0]}")
#     while score <= 21:
#         if d_score < 17:
#             compy_cards.append(random.choice(cards))
#         more_cards = input("Type 'y' for another card or type 'n' to pass ")
#         if more_cards == "y":
#             my_cards.append(random.choice(cards))
#             score = sum(my_cards)
#             print(f"Your cards are: {my_cards} Current score: {score}")
#             if score < 21:
#                 print(more_cards)
#             else:
#                 output = winner_calc(user_cards=my_cards, comp_cards=compy_cards)
#                 print(output)
#                 again = input("Would you like to play again? Type 'y' or 'n'\n")
#                 if again == "y":
#                     print("\n" * 20)
#                     blackjack()
#                 else:
#                     print("Okay thanks for playing")
#
#         else:
#             output = winner_calc(user_cards= my_cards, comp_cards= compy_cards)
#             print(output)
#             again = input("Would you like to play again? Type 'y' or 'n'\n")
#             if again == "y":
#                 blackjack()
#             else:
#                 print("Okay thanks for playing")
#
# welcome = input("Would you like to play a game of blackjack? Type 'y' or 'n'\n")
# if welcome == "y":
#     blackjack()
def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    selector = random.choice(cards)
    return selector


def calculate_score(card_list):
    score = sum(card_list)

    if score == 21 and card_list.count(11) == 1:
        return 0

    elif score > 21 and card_list.count(11) > 1:
        card_list.remove(11)
        card_list.append(1)

    return score


def compare(u_score, c_score):
    if u_score == c_score:
        return "Its a Draw"
    elif u_score == 0:
        return "You win by blackjack"
    elif c_score == 0:
        return "You lose. Computer wins by blackjack."
    elif u_score > 21:
        return "You went bust. You lose."
    elif c_score > 21:
        return "The computer went over. You win!"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    user_cards = []
    computer_cards = []
    computer_score =-1
    user_score =-1
    game_over = False
    print(logo)

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())


    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are: {user_cards} and your current score is: {user_score}")
        print(f"The computers first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score >21:
            game_over = True

        else:
            card_choice = input("Would you like to draw another card? Type 'y' or 'n': ").lower()
            if card_choice == "y":
                user_cards.append(deal_cards())
            else:
                game_over = True

    while computer_score != 0 and computer_score <17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is {user_cards} and your final score is {user_score}")
    print(f"The computers final hand is {computer_cards} and the computers final score is {computer_score}")
    print(compare(user_score, computer_score))


while input("Would you like to play a game of black jack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()

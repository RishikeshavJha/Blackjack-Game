import random

def draw_card():
    return random.randint(2, 11)

def calculate_score(cards):
    total = sum(cards)
    while 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)
        total = sum(cards)
    return total

def blackjack():
    while True:
        print("\n" * 20)
        print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
        player_cards = [draw_card(), draw_card()]
        player_score = calculate_score(player_cards)
        computer_cards = [draw_card()]
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        while player_score < 21:
            next_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if next_card == "y":
                player_cards.append(draw_card())
                player_score = calculate_score(player_cards)
                print(f"Your cards: {player_cards}, current score: {player_score}")
            else:
                break

        if player_score > 21:
            print("You went over. You lose 😭")
        else:
            while computer_score < 17:
                computer_cards.append(draw_card())
                computer_score = calculate_score(computer_cards)

            print(f"Your final hand: {player_cards}, final score: {player_score}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
            if computer_score > 21:
                print("Opponent went over. You win 😁")
            elif player_score == computer_score:
                print("Draw 🙃")
            elif player_score == 21:
                print("Win with a Blackjack 😎")
            elif computer_score == 21:
                print("Lose, opponent has Blackjack 😱")
            elif player_score > computer_score:
                print("You win 😃")
            else:
                print("You lose 😤")
        play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if play_again != "y":
            print("Bye!!!")
            break

if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    blackjack()
else:
    print("Bye!!!")

import random

# creating a full deck of playing cards
deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
total_decks = {}
all_cards = []
for suit in suits:
    total_decks[suit] = deck
    for i in range(len(deck)):
        all_cards.append(deck[i])
        # all_cards.append((deck[i],
        #                   suits
        # ))

# shuffle cards
random.shuffle(all_cards)
player_size = int(input("How many people are playing? "))

# players and hands initiation
players = {}
for i in range(1, int(player_size) + 1):
    if player_size <= 4:
        hands = [all_cards.pop(0) for j in range(7)]

    else:
        hands = [all_cards.pop(0) for j in range(5)]
    players[i] = hands


def print_result():
    result = [sorted(list(players.values())[element]) for element in
              range(len(players.values()))]
    return result


def start_game():
    # initialising score
    score = {}
    for n_players in players:
        score[n_players] = 0

    # start with player 1
    current_player = 1
    player_change = True
    turn = True
    while player_change:
        while turn:

            # count type of cards with each player
            # if number == 4, score increase
            element_count = {}
            for values in players[current_player]:
                element_count.setdefault(values, 0)
                element_count[values] += 1

            for key, values in element_count.items():
                if values == 4:
                    print(f"Player {current_player} cleared {key}")
                    # print(players[current_player])
                    while key in players[current_player]:
                        players[current_player].remove(key)
                    score[current_player] += 1

            if sum(score.values()) == 13:
                player_change = False
                print(score)
                break
            else:
                if not players[current_player] and all_cards:
                    card_picked = all_cards.pop(0)
                    players[current_player].append(card_picked)
                    print(f"{len(all_cards)} Cards in the deck")
                    # showing all values in a sorted manner
                print(print_result())
                print(score)
                print(f"Player{current_player}'s turn")
                call = input("Player and Card? ").upper()

                # check if the current player has cards
                while not players[current_player] and not all_cards:
                    if sum(score.values()) == 13:
                        player_change = False
                        print(score)
                        break
                    elif current_player == player_size:
                        current_player = 1
                    else:
                        current_player += 1

                if call:
                    try:
                        player, card = call.split()
                        player = int(player)
                        if player != current_player and player in players.keys() and card in players[current_player]:
                            if card in players[player]:
                                print(f"Player {current_player} received {card} from Player {player}")
                                card_found = True

                                # card found
                                if card_found:
                                    while card in players[player]:
                                        players[current_player].append(card)
                                        players[player].remove(card)
                                        turn = True
                            else:
                                print("GO FISH")
                                # check number of cards left in deck
                                while all_cards:
                                    card_picked = all_cards.pop(0)
                                    players[current_player].append(card_picked)

                                    # # card picked is with the player and he got lucky
                                    # if card_picked in players[current_player] and players[current_player].count(card_picked) == 4:
                                    #     print(f"Player {current_player} cleared {card_picked}")
                                    #     while card_picked in players[current_player]:
                                    #         players[current_player].remove(card_picked)
                                    #     score[current_player] += 1
                                    #     turn = True
                                    # # print(f"{len(all_cards)} Card/s in the deck")

                                else:
                                    print("Deck empty")

                                # player change if gofish
                                if current_player == player_size:
                                    current_player = 1
                                else:
                                    current_player += 1
                        else:
                            print("The card and the player should exist")

                    except ValueError:
                        print("Enter two values")


start_game()

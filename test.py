'''
two people card game 52 cards,
1 - 52 numbers;
randomly be given 26 cards
26 rounds: one round: each person pick the card from their own pile,
compare their values,
alice, bob
alice > bob: taking the card to her own winning pile
eg: 25, 20 -> (25, 20)
after the rounds over, who has more cards wins
tie: maximum number
simulate the process -> output the winner, the score
'''
import random

def compare_winning_pile(alice_winning_pile, bob_winning_pile):
    if len(alice_winning_pile) > len(bob_winning_pile):
        print("alice")
        print(len(alice_winning_pile))
    elif len(alice_winning_pile) < len(bob_winning_pile):
        print("bob")
        print(len(bob_winning_pile))
    else:
        if max(alice_winning_pile) > max(bob_winning_pile):
            print("alice")
            print(len(alice_winning_pile))
        else:
            print("bob")
            print(len(bob_winning_pile))

def card_game():
    # randomly distribute the cards
    alice, bob = [], []
    card_set= set()
    for i in range(1, 53):
        card_set.add(i)
    for i in range(52):
        card = random.randint(1,53)
        card_set.remove(card)
        if i % 2 == 0:
            alice.append(card)
        else:
            bob.append(card)
        break
            
    # for loop to simulate, compare the cards
    alice_winning_pile, bob_winning_pile = [], []
    for i in range(26):
        alice_card = alice.pop()
        bob_card = bob.pop()
        if alice_card > bob_card:
            alice_winning_pile += [alice_card, bob_card]
        else:
            bob_winning_pile += [alice_card, bob_card]
    
    # compare the number of piles
    compare_winning_pile(alice_winning_pile, bob_winning_pile)

card_game()
    
import random
import time

# Card representations
suits = ['♥', '♦', '♣', '♠']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            print("Reshuffling deck...")
            self.build()
            self.shuffle()
            return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'A':
            self.aces += 1
        
        # Adjust for aces if over 21
        self.adjust_for_ace()
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
    
    def __str__(self):
        return " ".join(str(card) for card in self.cards)

def display_hands(player_hand, dealer_hand, hide_dealer=True):
    print("\n" + "="*50)
    print("DEALER'S HAND:")
    if hide_dealer:
        print(f" {dealer_hand.cards[0]} [?]")
    else:
        print(f" {dealer_hand} (Value: {dealer_hand.value})")
    
    print("\nYOUR HAND:")
    print(f" {player_hand} (Value: {player_hand.value})")
    print("="*50)

def player_busts(player_hand):
    print("\n*** You bust! ***")
    return True

def player_wins(player_hand, dealer_hand):
    print(f"\n*** You win with {player_hand.value} against dealer's {dealer_hand.value}! ***")
    return True

def dealer_busts(dealer_hand):
    print(f"\n*** Dealer busts with {dealer_hand.value}! You win! ***")
    return True

def dealer_wins(player_hand, dealer_hand):
    print(f"\n*** Dealer wins with {dealer_hand.value} against your {player_hand.value}! ***")
    return True

def push(player_hand, dealer_hand):
    print(f"\n*** It's a tie! Both have {player_hand.value}. ***")
    return True

def player_double_down_wins(player_hand, dealer_hand):
    print(f"\n*** You win with Double Down! {player_hand.value} against dealer's {dealer_hand.value}! ***")
    print("*** In a real casino, you would have won double your bet! ***")
    return True

def player_double_down_loses(player_hand, dealer_hand):
    print(f"\n*** You lose with Double Down! Your {player_hand.value} against dealer's {dealer_hand.value}. ***")
    print("*** In a real casino, you would have lost double your bet. ***")
    return True

def play_again():
    while True:
        answer = input("\nWould you like to play again? (y/n): ").lower()
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print("Please enter 'y' or 'n'.")

def can_double_down(hand):
    # Double down is typically only allowed on the initial two cards
    return len(hand.cards) == 2

def blackjack():
    print("\n" + "*"*50)
    print("*" + " "*14 + "WELCOME TO BLACKJACK" + " "*15 + "*")
    print("*" + " "*48 + "*")
    print("*  Rules:                                          *")
    print("*  - Try to get as close to 21 as possible         *")
    print("*  - Dealer hits until 17 or higher                *")
    print("*  - Face cards are worth 10                       *")
    print("*  - Aces are worth 1 or 11                        *")
    print("*  - Double Down: Take one card and stand          *")
    print("*    (In casinos, this doubles your bet)           *")
    print("*" + " "*48 + "*")
    print("*"*50)
    
    # Create & shuffle deck
    deck = Deck()
    deck.shuffle()
    
    playing = True
    
    while playing:
        # Set up the game
        player_hand = Hand()
        dealer_hand = Hand()
        doubled_down = False
        
        # Deal initial cards
        for _ in range(2):
            player_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())
        
        # Show the hands
        display_hands(player_hand, dealer_hand)
        
        game_over = False
        
        # Player's turn
        while not game_over:
            # Check if player can double down (only on initial two cards)
            if can_double_down(player_hand):
                choice = input("\nWould you like to [H]it, [S]tand, or [D]ouble down? ").lower()
            else:
                choice = input("\nWould you like to [H]it or [S]tand? ").lower()
            
            if choice.startswith('h'):
                player_hand.add_card(deck.deal())
                print("\nYou drew:", player_hand.cards[-1])
                time.sleep(1)
                display_hands(player_hand, dealer_hand)
                
                if player_hand.value > 21:
                    game_over = player_busts(player_hand)
                    break
            
            elif choice.startswith('s'):
                print("\nYou stand. Dealer's turn.")
                break
            
            elif choice.startswith('d') and can_double_down(player_hand):
                doubled_down = True
                print("\n*** Double Down! ***")
                print("You take exactly one more card and stand.")
                print("In a real casino, this would double your bet.")
                
                player_hand.add_card(deck.deal())
                print("\nYou drew:", player_hand.cards[-1])
                time.sleep(1)
                display_hands(player_hand, dealer_hand)
                
                if player_hand.value > 21:
                    game_over = player_busts(player_hand)
                else:
                    print("\nYou automatically stand after doubling down. Dealer's turn.")
                break
            
            else:
                if choice.startswith('d') and not can_double_down(player_hand):
                    print("You can only double down on your initial two cards.")
                else:
                    print("Please enter 'h', 's', or 'd' (if available).")
        
        # Dealer's turn
        if not game_over:
            display_hands(player_hand, dealer_hand, hide_dealer=False)
            time.sleep(1)
            
            while dealer_hand.value < 17:
                print("\nDealer hits...")
                dealer_hand.add_card(deck.deal())
                print("Dealer drew:", dealer_hand.cards[-1])
                time.sleep(1)
                display_hands(player_hand, dealer_hand, hide_dealer=False)
            
            if dealer_hand.value > 21:
                game_over = dealer_busts(dealer_hand)
            elif dealer_hand.value > player_hand.value:
                if doubled_down:
                    game_over = player_double_down_loses(player_hand, dealer_hand)
                else:
                    game_over = dealer_wins(player_hand, dealer_hand)
            elif player_hand.value > dealer_hand.value:
                if doubled_down:
                    game_over = player_double_down_wins(player_hand, dealer_hand)
                else:
                    game_over = player_wins(player_hand, dealer_hand)
            else:
                game_over = push(player_hand, dealer_hand)
        
        # Ask to play again
        playing = play_again()
    
    print("\nThanks for playing!")

if __name__ == "__main__":
    blackjack() 
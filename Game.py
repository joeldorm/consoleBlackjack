
from Card import Deck
from Card import Hand


class Game:
    def __init__(self) -> None:
        playing = True

        while playing:
            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)

            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())

            print("Your hand is:")
            self.player_hand.display()
            print()
            print("Dealer's hand is:")
            self.dealer_hand.display()

            game_over = False
            while not game_over:
                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()
                if player_has_blackjack or dealer_has_blackjack:
                    game_over = True
                    self.show_blackjacj_results(
                        player_has_blackjack, dealer_has_blackjack)
                    continue
                choice = input("Please choose [Hit / Stick] ").lower()
                while choice not in ['h', 's', 'hit', 'stick']:
                    choice = input(
                        "Please enter 'hit' or 'stick' (or H/S) ").lower()
                    if choice in ['hit', 'h']:
                        self.player_hand.add_card(self.deck.deal())
                        self.player_hand.display()
                    if self.player_is_over():
                        print("You have lost!")
                        has_won = True
                    else:
                        print("Final Results")
                        print("Your hand: ", self.player_hand.get_value())
                        print("Dealer's hand: ", self.dealer_hand.get_value())
                        if self.player_hand.get_value() > self.dealer_hand.get_value():
                            print("You Win!")
                        else:
                            print("Dealer Wins!")
                            has_won = True
            again = input("Play again? [Y/N] ")
            while again.lower() not in ['y', 'n']:
                again = input("Please enter Y or N")
                if again.lower() == "n":
                    print("Thanks for playing")
                    playing = False
                else:
                    has_won = False

    def check_for_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True

        return player, dealer

    def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            print("Both players have blackjack Draw!")
        elif player_has_blackjack:
            print("You have blackjack! You win")
        elif dealer_has_blackjack:
            print("Dealer has blackjack! Dealer wins!")

    def player_is_over(self):
        return self.player_hand.get_value() > 21


if __name__ == "__main__":
    game = Game()

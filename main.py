
from game import Game
#import django
# Hey its david
# Initialize game and deal cards
g = Game()
g.deck.shuffle()
g.deck.deal_cards(g.players)

# play game until there is a winner
while not g.check_winner():
    print('\n' + g.player_active.name + ', it is your turn' + '\n')
    g.take_turn()

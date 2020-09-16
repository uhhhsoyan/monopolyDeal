
import random
from card import PropertyCard, PropertyWildCard, ActionCard, RentCard, MoneyCard


class Deck:
    def __init__(self):
        # count_full and rents array are redundant with PropertySet dataclass
        self.deck = [
            PropertyCard(value=1, name='Mediterranean Ave', color='brown', count_full=2, rents=[1, 2]),
            PropertyCard(value=1, name='Baltic Ave', color='brown', count_full=2, rents=[1, 2]),
            PropertyCard(value=1, name='Connecticut Ave', color='light blue', count_full=2, rents=[1, 2, 3]),
            PropertyCard(value=1, name='Vermont Ave', color='light blue', count_full=2, rents=[1, 2, 3]),
            PropertyCard(value=1, name='Oriental Ave', color='light blue', count_full=2, rents=[1, 2, 3]),
            PropertyCard(value=2, name='Water Works', color='utility', count_full=2, rents=[1, 2]),
            PropertyCard(value=2, name='Electric Company', color='utility', count_full=2, rents=[1, 2]),
            PropertyCard(value=2, name='Virginia Ave', color='pink', count_full=3, rents=[1, 2, 4]),
            PropertyCard(value=2, name='St Charles Place', color='pink', count_full=3, rents=[1, 2, 4]),
            PropertyCard(value=2, name='States Avenue', color='pink', count_full=3, rents=[1, 2, 4]),
            PropertyCard(value=2, name='Tennessee Avenue', color='orange', count_full=3, rents=[1, 3, 5]),
            PropertyCard(value=2, name='New York Avenue', color='orange', count_full=3, rents=[1, 3, 5]),
            PropertyCard(value=2, name='St James Place', color='orange', count_full=3, rents=[1, 3, 5]),
            PropertyCard(value=2, name='B & O Railroad', color='railroad', count_full=4, rents=[1, 2, 3, 4]),
            PropertyCard(value=2, name='Short Line', color='railroad', count_full=4, rents=[1, 2, 3, 4]),
            PropertyCard(value=2, name='Pennsylvania Railroad', color='railroad', count_full=4, rents=[1, 2, 3, 4]),
            PropertyCard(value=2, name='Reading Railroad', color='railroad', count_full=4, rents=[1, 2, 3, 4]),
            PropertyCard(value=3, name='Atlantic Avenue', color='yellow', count_full=3, rents=[2, 4, 6]),
            PropertyCard(value=3, name='Marvin Gardens', color='yellow', count_full=3, rents=[2, 4, 6]),
            PropertyCard(value=3, name='Ventnor Avenue', color='yellow', count_full=3, rents=[2, 4, 6]),
            PropertyCard(value=3, name='Illinois Avenue', color='red', count_full=3, rents=[2, 3, 6]),
            PropertyCard(value=3, name='Indiana Avenue', color='red', count_full=3, rents=[2, 3, 6]),
            PropertyCard(value=3, name='Kentucky Avenue', color='red', count_full=3, rents=[2, 3, 6]),
            PropertyCard(value=4, name='Pennsylvania Avenue', color='green', count_full=3, rents=[2, 4, 7]),
            PropertyCard(value=4, name='North Carolina Avenue', color='green', count_full=3, rents=[2, 4, 7]),
            PropertyCard(value=4, name='Pacific Avenue', color='green', count_full=3, rents=[2, 4, 7]),
            PropertyCard(value=4, name='Park Place', color='dark blue', count_full=2, rents=[3, 8]),
            PropertyCard(value=4, name='Boardwalk', color='dark blue', count_full=2, rents=[3, 8]),
            PropertyWildCard(value=1, color=['light blue', 'brown']),
            PropertyWildCard(value=2, color=['pink', 'orange']),
            PropertyWildCard(value=2, color=['pink', 'orange']),
            PropertyWildCard(value=2, color=['railroad', 'utility']),
            PropertyWildCard(value=3, color=['red', 'yellow']),
            PropertyWildCard(value=3, color=['red', 'yellow']),
            PropertyWildCard(value=4, color=['railroad', 'light blue']),
            PropertyWildCard(value=4, color=['railroad', 'green']),
            PropertyWildCard(value=4, color=['green', 'dark blue']),
            PropertyWildCard(value=0, color=['light blue', 'brown', 'pink', 'orange', 'railroad', 'utility', 'red', 'yellow', 'green', 'dark blue']),
            PropertyWildCard(value=0, color=['light blue', 'brown', 'pink', 'orange', 'railroad', 'utility', 'red', 'yellow', 'green', 'dark blue']),
            ActionCard(value=1, action='pass go'),
            ActionCard(value=1, action='pass go'),
            ActionCard(value=1, action='pass go'),
            ActionCard(value=1, action='pass go'),
            ActionCard(value=1, action='pass go'),
            ActionCard(value=1, action='pass go'),
            ActionCard(value=1, action='pass go'),
            ActionCard(value=1, action='pass go'),
            ActionCard(value=1, action='pass go'),
            ActionCard(value=1, action='pass go'),
            ActionCard(value=1, action='double rent'),
            ActionCard(value=1, action='double rent'),
            ActionCard(value=2, action='birthday'),
            ActionCard(value=2, action='birthday'),
            ActionCard(value=3, action='sly deal'),
            ActionCard(value=3, action='sly deal'),
            ActionCard(value=3, action='sly deal'),
            ActionCard(value=3, action='forced deal'),
            ActionCard(value=3, action='forced deal'),
            ActionCard(value=3, action='forced deal'),
            ActionCard(value=3, action='debt collector'),
            ActionCard(value=3, action='debt collector'),
            ActionCard(value=3, action='debt collector'),
            ActionCard(value=3, action='house'),
            ActionCard(value=3, action='house'),
            ActionCard(value=3, action='house'),
            ActionCard(value=4, action='hotel'),
            ActionCard(value=4, action='hotel'),
            ActionCard(value=4, action='just say no'),
            ActionCard(value=4, action='just say no'),
            ActionCard(value=4, action='just say no'),
            ActionCard(value=5, action='deal breaker'),
            ActionCard(value=5, action='deal breaker'),
            RentCard(value=1, colors=['light blue', 'brown']),
            RentCard(value=1, colors=['light blue', 'brown']),
            RentCard(value=1, colors=['pink', 'orange']),
            RentCard(value=1, colors=['pink', 'orange']),
            RentCard(value=1, colors=['red', 'yellow']),
            RentCard(value=1, colors=['red', 'yellow']),
            RentCard(value=1, colors=['dark blue', 'green']),
            RentCard(value=1, colors=['dark blue', 'green']),
            RentCard(value=1, colors=['railroad', 'utility']),
            RentCard(value=1, colors=['railroad', 'utility']),
            RentCard(value=3, colors=['light blue', 'brown', 'pink', 'orange', 'railroad', 'utility', 'red', 'yellow', 'green', 'dark blue']),
            RentCard(value=3, colors=['light blue', 'brown', 'pink', 'orange', 'railroad', 'utility', 'red', 'yellow', 'green', 'dark blue']),
            RentCard(value=3, colors=['light blue', 'brown', 'pink', 'orange', 'railroad', 'utility', 'red', 'yellow', 'green', 'dark blue']),
            MoneyCard(value=1),
            MoneyCard(value=1),
            MoneyCard(value=1),
            MoneyCard(value=1),
            MoneyCard(value=1),
            MoneyCard(value=1),
            MoneyCard(value=2),
            MoneyCard(value=2),
            MoneyCard(value=2),
            MoneyCard(value=2),
            MoneyCard(value=2),
            MoneyCard(value=3),
            MoneyCard(value=3),
            MoneyCard(value=3),
            MoneyCard(value=4),
            MoneyCard(value=4),
            MoneyCard(value=4),
            MoneyCard(value=5),
            MoneyCard(value=5),
            MoneyCard(value=10)
        ]

    # fisher yates shuffle method
    def shuffle(self):
        for i in range(len(self.deck) - 1, 0, -1):
            j = random.randint(0, i + 1)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
        return self.deck

    def deal_cards(self, players):
        for i in range(5):
            for player in players:
                temp = self.deck.pop()
                player.hand.append(temp)

    def draw(self, player):
        for i in range(2):
            temp = self.deck.pop()
            player.hand.append(temp)

    def draw_five(self, player):
        for i in range(5):
            temp = self.deck.pop()
            player.hand.append(temp)
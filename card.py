from dataclasses import dataclass
import typing as t


@dataclass
class Card:
    value: int


@dataclass
class PropertyCard(Card):
    name: str
    color: str
    count_full: int
    rents: t.List[int]


@dataclass
class PropertyWildCard(Card):
    color: t.List[str]


@dataclass
class ActionCard(Card):
    action: str


@dataclass
class RentCard(Card):
    colors: t.List[str]


@dataclass
class MoneyCard(Card):
    pass


@dataclass
class PropertySet:
    properties: t.List[PropertyCard]
    wild_properties: t.List[PropertyWildCard]
    house: bool = False
    hotel: bool = False
    color: str = None
    is_full: bool = False
    current_rent: int = 0

    def add_house_hotel(self, card):
        if not self.is_full:
            print('Houses and hotels can only be played on full property sets')
            return False
        elif card.action == 'house':
            if self.house:
                print('A house has already been played on this property set')
                return False
            else:
                self.house = True
                self.update_set()
                return True
        elif card.action == 'hotel':
            if self.house and not self.hotel:
                self.hotel = True
                self.update_set()
                return True
            elif self.hotel:
                print('A hotel has already been played on this property set')
                return False
            else:
                print('You must play a house on this property set before playing a hotel')
                return False

    def add_card(self, card):
        # scenario A: property set is full
        if self.is_full:
            print('The stack is full, please select another or create a new stack')
            return False
        # scenario B: property set has no prop card, no wild card
        elif len(self.properties) == 0 and len(self.wild_properties) == 0:
            if isinstance(card, PropertyWildCard):
                selected_color = ''
                while selected_color not in card.color:
                    selected_color = input('Which color would you like to play this card as?').lower()
                self.wild_properties.append(card)
                self.update_set(selected_color)
                return True
            else:
                self.properties.append(card)
                self.color = card.color
                return True
        # scenario C: property set has prop card
        elif len(self.properties) > 0:
            if isinstance(card, PropertyWildCard):
                if self.color in card.color:
                    self.wild_properties.append(card)
                    self.update_set()
                    return True
                else:
                    print('That card cannot be played on this property set')
                    return False
            else:  # PropertyCard
                if self.color == card.color:
                    self.properties.append(card)
                    self.update_set()
                    return True
                else:
                    print('That card cannot be played on this property set')
                    return False
        # scenario D: property set has wild card and no prop card
        elif len(self.wild_properties) > 0 and len(self.properties) == 0:
            if isinstance(card, PropertyCard):
                if card.color in self.wild_properties[0].color:
                    self.properties.append(card)
                    self.update_set(card.color)
                    return True
                else:
                    print('That card cannot be played on this property set')
                    return False
            else:  # PropertyWildCard
                if self.wild_properties[0].color[0] in card.color and self.wild_properties[0].color[1] in card.color:
                    self.wild_properties.append(card)
                    self.update_set()
                    return True
                else:
                    print('That card cannot be played on this property set')
                    return False

    def update_set(self, color=None):
        color_rents = {
            'brown': [1, 2],
            'light blue': [1, 2, 3],
            'utility': [1, 2],
            'pink': [1, 2, 4],
            'orange': [1, 3, 5],
            'railroad': [1, 2, 3, 4],
            'yellow': [2, 4, 6],
            'red': [2, 3, 6],
            'green': [2, 4, 7],
            'dark blue': [3, 8]
        }
        if color:
            self.color = color
        set_size = len(self.properties) + len(self.wild_properties)
        self.is_full = set_size == len(color_rents[self.color])
        self.current_rent = color_rents[self.color][set_size - 1] + 3 * self.house + 1 * self.hotel


@dataclass
class Player:
    name: str
    hand: t.List[Card]  # list of Card objects
    bank: t.List[Card]  # list of MoneyCard objects or banked ActionCards
    properties: t.List[PropertySet]  # list of Stacks of PropertyCard objects

    def pay_up(self, amount_owed):
        cards_paid = []
        while amount_owed > 0:
            if len(self.bank) == 0 and len(self.properties) == 0:
                print('Sorry! ' + self.name + ' has nothing to pay with!')
                amount_owed = 0
            else:
                pay_method = input(self.name + ', you owe ' + str(amount_owed) + '. Would you like to pay from bank or '
                                                                            'properties? Enter \'b\' for bank or '
                                                                            '\'p\' for properties: ').lower()
                if pay_method == 'b':
                    if len(self.bank) == 0:
                        print('Your bank is empty, please select a property card')
                        continue
                    card_index = int(input('Which card from your bank? Enter the index: '))
                    card_selected = self.bank[int(card_index)]
                    cards_paid.append(card_selected)
                    del self.bank[card_index]
                    amount_owed -= card_selected.value
                elif pay_method == 'p':
                    set_idx = int(input('Which set? Enter the index'))
                    prop_or_wild = input('Prop card or wild card? Enter \'p\' or \'w\': ').lower()
                    prop_idx = int(input('Enter the index in the corresponding list: '))
                    if prop_or_wild == 'p':
                        card_selected = self.properties[set_idx].properties[prop_idx]
                        cards_paid.append(card_selected)
                        del self.properties[set_idx].properties[prop_idx]
                        amount_owed -= card_selected.value
                    else:
                        card_selected = self.properties[set_idx].wild_properties[prop_idx]
                        cards_paid.append(card_selected)
                        del self.properties[set_idx].wild_properties[prop_idx]
                        amount_owed -= card_selected.value
        return cards_paid

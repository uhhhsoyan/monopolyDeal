from deck import Deck
from card import PropertyCard, PropertyWildCard, ActionCard, RentCard, MoneyCard, PropertySet, Player


class Game:
    def __init__(self, player_count=None):
        if player_count is None:
            player_count = 2
        self.player_count = player_count
        self.player_one = Player(name="Eric", hand=[], bank=[], properties=[])
        self.player_two = Player(name="Rach", hand=[], bank=[], properties=[])
        """
        TESTING SETUP
        self.player_one = Player(
            name="Test John",
            hand=[
                PropertyWildCard(value=0, color=['light blue', 'brown', 'pink', 'orange', 'railroad', 'utility', 'red', 'yellow', 'green', 'dark blue']),
                RentCard(value=3,
                         colors=['light blue', 'brown', 'pink', 'orange', 'railroad', 'utility', 'red', 'yellow',
                                 'green', 'dark blue']),
                ActionCard(value=3, action='house'),
                ActionCard(value=4, action='hotel'),
                ActionCard(value=2, action='birthday'),
            ],
            bank=[
                MoneyCard(value=2),
                MoneyCard(value=2),
                MoneyCard(value=3),
                MoneyCard(value=3),
                MoneyCard(value=3),
                MoneyCard(value=4),
            ],
            properties=[
                PropertySet(properties=[
                    PropertyCard(value=1, name='Mediterranean Ave', color='brown', count_full=2, rents=[1, 2]),
                    PropertyCard(value=1, name='Baltic Ave', color='brown', count_full=2, rents=[1, 2])],
                            wild_properties=[], house=False, hotel=False, color='brown', is_full=True, current_rent=2),
                PropertySet(properties=[
                    PropertyCard(value=1, name='Mediterranean Ave', color='brown', count_full=2, rents=[1, 2]),
                    PropertyCard(value=1, name='Baltic Ave', color='brown', count_full=2, rents=[1, 2])],
                        wild_properties=[], house=False, hotel=False, color='brown', is_full=True, current_rent=2),
                PropertySet(properties=[
                    PropertyCard(value=1, name='Baltic Ave', color='brown', count_full=2, rents=[1, 2])],
                        wild_properties=[], house=False, hotel=False, color='brown', is_full=False, current_rent=1)
            ]
        )
        self.player_two = Player(
            name="Test Jane",
            hand=[
                PropertyWildCard(value=0,
                                 color=['light blue', 'brown', 'pink', 'orange', 'railroad', 'utility', 'red', 'yellow',
                                        'green', 'dark blue']),
                RentCard(value=3,
                         colors=['light blue', 'brown', 'pink', 'orange', 'railroad', 'utility', 'red', 'yellow',
                                 'green', 'dark blue']),
                ActionCard(value=3, action='house'),
                ActionCard(value=4, action='hotel'),
                ActionCard(value=2, action='birthday'),
                PropertyCard(value=1, name='Mediterranean Ave', color='brown', count_full=2, rents=[1, 2]),
                PropertyCard(value=1, name='Baltic Ave', color='brown', count_full=2, rents=[1, 2]),
            ],
            bank=[
                MoneyCard(value=1),
            ],
            properties=[
                PropertySet(properties=[
                    PropertyCard(value=1, name='Mediterranean Ave', color='brown', count_full=2, rents=[1, 2]),
                    PropertyCard(value=1, name='Baltic Ave', color='brown', count_full=2, rents=[1, 2])],
                    wild_properties=[], house=False, hotel=False, color='brown', is_full=True, current_rent=2)
            ]
        )
        """
        self.players = [self.player_one, self.player_two]
        self.deck = Deck()
        self.discard = []
        self.player_active = self.player_one
        self.plays_left = 0

    # print board for playing the game in the console
    def print_board(self):
        for player in self.players:
            print('Player: ' + player.name)
            print('Hand:')
            for i in range(len(player.hand)):
                print(str(i) + ': ' + str(player.hand[i]))
            print('Properties:')
            for i in range(len(player.properties)):
                print(str(i) + ': ' + str(player.properties[i]))
            print('Bank:')
            for i in range(len(player.bank)):
                print(str(i) + ': ' + str(player.bank[i]))
            print('----------')
        print('Discard: ' + str(self.discard))
        print('\n')

    # check for a winner (player with 3 full property sets)
    def check_winner(self) -> bool:
        for player in self.players:
            full_sets = 0
            for property_set in player.properties:
                if property_set.is_full:
                    full_sets += 1
            if full_sets >= 3:
                print(player.name + ' is the winner!')
                return True
        return False

    def get_user_input(self, prompt, return_type, accept_range=None, special=None):
        output = ''
        while True:
            if return_type == 'int':
                try:
                    output = int(input(prompt))
                except ValueError:
                    print("Invalid input, please try again")
                    continue
            else:
                output = input(prompt).lower()
            if accept_range is not None and output not in accept_range and output != special:
                print("Invalid input, please try again")
                continue
            else:
                break
        return output

    # current player takes a turn and makes up to 3 plays
    def take_turn(self):
        plays_left = 3
        # draw five cards if empty hand
        if len(self.player_active.hand) == 0:
            print('Current player is drawing five cards')
            self.deck.draw_five(self.player_active)
        # draw two cards to start turn
        else:
            self.deck.draw(self.player_active)

        while plays_left > 0:
            self.print_board()
            print(self.player_active.name + ', you have ' + str(plays_left) + ' plays left')
            play_idx = self.get_user_input('Enter the index of the card to play (99 to end turn early): ',
                                           'int', range(len(self.player_active.hand)), 99)
            if play_idx == 99:
                break
            self.play_card(self.player_active.hand[play_idx])
            plays_left -= 1
        self.end_turn()

    def end_turn(self):
        while len(self.player_active.hand) > 7:
            discard_idx = self.get_user_input('You have too many cards in your hand. Enter the index to be discarded: ',
                                              'int', range(len(self.player_active.hand)))
            discarded_card = self.player_active.hand[discard_idx]
            self.discard.append(discarded_card)
            self.player_active.hand.remove(discarded_card)
        # change the active player
        active_index = self.players.index(self.player_active)
        if active_index == len(self.players) - 1:
            self.player_active = self.players[0]
        else:
            self.player_active = self.players[active_index + 1]

    def play_card(self, card):
        # call the appropriate play_card method based on card type
        if isinstance(card, PropertyCard) or isinstance(card, PropertyWildCard):
            self.play_property_card(card)
        elif isinstance(card, ActionCard):
            self.play_action_card(card)
        elif isinstance(card, RentCard):
            self.play_rent_card(card)
        else:
            self.play_money_card(card)

    def play_property_card(self, card):
        if len(self.player_active.properties) == 0:
            temp = PropertySet(properties=[], wild_properties=[])
            temp.add_card(card)
            self.player_active.properties.append(temp)
            self.player_active.hand.remove(card)
        else:
            # add input validation
            while True:
                set_idx = self.get_user_input('Which property set? Enter index or 99 for new: ',
                                              'int', range(len(self.player_active.properties)), 99)
                if set_idx == 99:
                    print("MADE IT HERE")
                    temp = PropertySet(properties=[], wild_properties=[])
                    if temp.add_card(card):  # check if able to add card to set
                        self.player_active.properties.append(temp)
                        # self.player_active.properties.append([card])
                        self.player_active.hand.remove(card)
                        break
                    else:
                        continue
                elif self.player_active.properties[set_idx].add_card(card):
                    break
                else:
                    print('You selected an invalid property set')
                    continue

    def play_rent_card(self, card, doubler=False):
        bank_or_play = self.get_user_input('Bank or play? Enter \'b\' for bank or \'p\' for play: ',
                                           'str', ['b', 'p'])
        if bank_or_play == 'b':
            self.player_active.bank.append(card)
            self.player_active.hand.remove(card)
        else:
            color_rent = self.get_user_input('Which color: ', 'str', card.colors)
            set_idx = self.get_user_input('Enter the index of the property set to charge rent on: ',
                                          'int', range(len(self.player_active.properties)))
            selected_set = self.player_active.properties[set_idx]
            while True:
                if selected_set.color == color_rent:
                    for p in self.players:
                        if p == self.player_active:
                            pass
                        else:
                            cards_received = p.pay_up(selected_set.current_rent + doubler * selected_set.current_rent)
                            for card in cards_received:
                                if isinstance(card, MoneyCard) or isinstance(card, ActionCard):
                                    self.player_active.bank.append(card)
                                else:
                                    print(self.player_active.name + ', you received ' + str(card))
                                    # temporarily add card to hand - it will be immediately removed by play_card method
                                    self.player_active.hand.append(card)
                                    self.play_card(card)
                    break
                else:
                    print('You selected an invalid property set. Please try again')
                    continue
        self.discard.append(card)
        self.player_active.hand.remove(card)

    def play_money_card(self, card):
        self.player_active.bank.append(card)
        self.player_active.hand.remove(card)
        return True

    def play_action_card(self, card):
        bank_or_play = self.get_user_input('Bank or play this action card? Enter \'b\' for bank or \'p\' for play: ',
                                           'str', ['b', 'p'])
        if bank_or_play == 'b':
            self.player_active.bank.append(card)
            self.player_active.hand.remove(card)
        elif card.action == 'house' or card.action == 'hotel':
            # update input validation - don't allow player to select play without at least one full set, non RR/utility
            set_idx = self.get_user_input('Which property set? Enter set index: ',
                                            'int', range(len(self.player_active.properties)))
            selected_set = self.player_active.properties[set_idx]
            selected_set.add_house_hotel(card)
        elif card.action == 'pass go':
            self.discard.append(card)
            self.player_active.hand.remove(card)
            self.deck.draw(self.player_active)
        elif card.action == 'birthday':
            for p in self.players:
                if p == self.player_active:
                    pass
                else:
                    cards_received = p.pay_up(2)
                    for card in cards_received:
                        if isinstance(card, MoneyCard) or isinstance(card, ActionCard):
                            self.player_active.bank.append(card)
                        else:
                            print(self.player_active.name + ', you received ' + str(card))
                            # temporarily add card to hand - it will be removed immediately when played
                            self.player_active.hand.append(card)
                            self.play_card(card)
            self.discard.append(card)
            self.player_active.hand.remove(card)
        elif card.action == 'debt collector':
            player_selected = self.get_user_input('Which player would you like to collect from? Enter their index: ',
                                                  'int', len(range(self.players)))
            cards_received = self.players[player_selected].pay_up(5)
            for card in cards_received:
                if isinstance(card, MoneyCard) or isinstance(card, ActionCard):
                    self.player_active.bank.append(card)
                else:
                    print('You received ' + str(card))
                    self.play_card(card)
            self.discard.append(card)
            self.player_active.hand.remove(card)
        elif card.action == 'sly deal':
            player_selected = self.players[self.get_user_input(
                'Which player would you like to collect from? Enter their index: ',
                'int',
                range(len(self.players)))]
            while True:
                set_selected = player_selected.properties[self.get_user_input(
                    'From which property set? Enter the index: ',
                    'int',
                    range(len(player_selected.properties)))]
                if set_selected.is_full:
                    continue
                else:
                    break
            card_selected = set_selected.properties[self.get_user_input('Which card? Enter the index: ', 'int', )]
            set_selected.properties.remove(card_selected)
            print(self.player_active.name + ', you received ' + str(card))
            # temporarily add card to hand - it will be removed immediately when played
            self.player_active.hand.append(card_selected)
            self.play_card(card_selected)
            self.discard.append(card)
            self.player_active.hand.remove(card)
        elif card.action == 'forced deal':
            # update logic
            self.discard.append(card)
            self.player_active.hand.remove(card)
        elif card.action == 'deal breaker':
            # update logic
            self.discard.append(card)
            self.player_active.hand.remove(card)
        elif card.action == 'double rent':
            # update logic
            self.discard.append(card)
            self.player_active.hand.remove(card)
        elif card.action == 'just say no':
            # update logic
            self.discard.append(card)
            self.player_active.hand.remove(card)


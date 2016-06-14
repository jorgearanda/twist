import collections

Card = collections.namedtuple('Card', ['shortname', 'name', 'stage', 'type', 'after_play', 'ops'])

class TwilightDeck:
    def __init__(self, stage='all'):
        self._cards = {}
        self._stages = ['early', 'mid', 'late', 'special']
        if stage != 'all':
            self.add_stage_cards(stage)
        else:
            for s in self._stages:
                self.add_stage_cards(s)

    def add_stage_cards(self, stage):
        with open('cards.txt') as f:
            for line in f:
                card_values = line.split(',')
                if card_values[2] != stage:
                    continue
                card_values[-1] = int(card_values[-1])  # ops value
                self._cards[card_values[0]] = Card(*card_values)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, shortname):
        return self._cards.get(shortname)

    def __iter__(self):
        for card in self._cards.values():
            yield card
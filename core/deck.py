import random

DECK_DEFINITION = [
    ("MOVE", 1, 18),  # 18 cards with move 1
    ("MOVE", 2, 12),  # 12 cards with move 2
    ("MOVE", 3, 6),  # 6 cards with move 3
    ("AI_TURN", 0, 6),  # 6 cards with AI Turn
]

DECK_SIZE = sum(t[2] for t in DECK_DEFINITION)


class Card:
    """Single card used by the deck."""

    def __init__(self, kind: str, steps: int, name: str):
        self.kind = kind
        self.steps = steps
        self.name = name

    def __repr__(self):
        return f"{self.name}"


class Deck:
    """Deck of cards used by the game.

    Attributes:
        active_pile: Remaining cards in the draw pile.
        discard_pile: Cards that were already drawn.
    """

    def __init__(self):
        self._base_deck = self._create_base_deck()
        self.active_pile: list[Card] = []
        self.discard_pile: list[Card] = []
        self.reshuffled_last_draw = False
        self._reset_and_shuffle()

    def _create_base_deck(self) -> list[Card]:
        """Created base deck according to DECK_DEFINITION.

        Returns:
            Cards: The list of cards.
        """

        cards: list[Card] = []

        for kind, steps, count in DECK_DEFINITION:
            for _ in range(count):

                if kind == "MOVE":
                    card = Card(
                        kind=kind, steps=steps, name=f"Movement Card - {steps} step(s)"
                    )
                else:
                    card = Card(kind=kind, steps=steps, name="AI Turn Card")
                cards.append(card)

        return cards

    def _reset_and_shuffle(self):
        """Resets and shuffle base deck."""

        self.active_pile = self._base_deck.copy()
        self.discard_pile.clear()
        random.shuffle(self.active_pile)

    def draw(self):
        """Draw the next card from the deck.
        If the deck is empty, it is reshuffled automatically.

        Returns:
            Card: Draw card.
        """

        card = self.active_pile.pop()
        self.discard_pile.append(card)

        self.reshuffled_last_draw = False
        if len(self.active_pile) == 0: # reshuffle deck if last card was taken
            self.reshuffled_last_draw = True
            self._reset_and_shuffle()
        return card

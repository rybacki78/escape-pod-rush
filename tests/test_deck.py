from escape_pod_rush.core.deck import Deck, Card, DECK_SIZE


def test_deck_initial_state():
    deck = Deck()
    assert len(deck.active_pile) == DECK_SIZE
    assert len(deck.discard_pile) == 0


def test_deck_draw_moves_card_to_discard():
    deck = Deck()
    card = deck.draw()
    assert isinstance(card, Card)
    assert len(deck.active_pile) == DECK_SIZE - 1
    assert len(deck.discard_pile) == 1
    assert deck.discard_pile[-1] is card


def test_deck_reshuffles_after_last_card():
    deck = Deck()

    for _ in range(DECK_SIZE - 1):
        deck.draw()
        assert deck.reshuffled_last_draw is False
        assert len(deck.active_pile) < DECK_SIZE
    assert len(deck.active_pile) == 1

    last_card = deck.draw()
    assert isinstance(last_card, Card)

    assert deck.reshuffled_last_draw is True
    assert len(deck.active_pile) == DECK_SIZE


def test_deck_produces_all_card_types():
    deck = Deck()
    seen = set()

    for _ in range(DECK_SIZE):
        card = deck.draw()
        seen.add(card.name)

    assert "Movement Card - 1 step(s)" in seen
    assert "Movement Card - 2 step(s)" in seen
    assert "Movement Card - 3 step(s)" in seen
    assert "AI Turn Card" in seen

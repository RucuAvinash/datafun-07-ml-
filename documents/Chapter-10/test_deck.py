# test_deck.py
"""Test the Card and DeckOfCards classes."""
from deck import DeckOfCards

def run_card_deck_test():
    """Create a deck, shuffle it, and deal a few cards."""
    print("--- Creating a new Deck of Cards ---")
    deck_of_cards = DeckOfCards()

    # Test the initial (unshuffled) deck structure and the __str__ method
    print("Initial (Unshuffled) Deck:")
    print(deck_of_cards)

    # --- Test Shuffle ---
    print("\n" + "=" * 30)
    print("--- Shuffling the Deck ---")
    deck_of_cards.shuffle()
    print("Shuffled Deck (first 20 cards):")
    # Print the first 4 cards from the shuffled deck (to show it changed)
    print(str(deck_of_cards._deck[0:20]) + "...")

    # --- Test Dealing Cards ---
    print("\n" + "=" * 30)
    print("--- Dealing Cards ---")
    
    # Deal the first 5 cards
    for i in range(1, 6):
        card = deck_of_cards.deal_card()
        if card:
            # Test the __str__ and image_name property
            print(f"Card {i}: {card!s:<18} (Image File: {card.image_name})")
        else:
            print(f"Card {i}: Deck is empty!")

    # Deal a card to test the __repr__ method
    print("\n--- Testing Card __repr__ ---")
    first_dealt_card = deck_of_cards._deck[0] # The card at index 0 is the one that will be dealt next
    print(f"The next card is represented by: {first_dealt_card!r}") 
    
    # --- Test Exhausting the Deck (Dealing all 52 cards) ---
    print("\n" + "=" * 30)
    print("--- Dealing Remaining Cards (to check for None return) ---")
    
    # Deal the remaining 52 - 5 = 47 cards
    for _ in range(47):
        deck_of_cards.deal_card()

    # Try to deal the 53rd card (should return None)
    print(f"Attempting to deal the 53rd card...")
    final_card = deck_of_cards.deal_card()
    if final_card is None:
        print("Successfully returned None, indicating the deck is empty.")
    else:
        print(f"Error: Expected None, got {final_card}")


if __name__ == "__main__":
    run_card_deck_test()
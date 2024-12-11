def display_card(card):
    return ", ".join(map(str, card))

def display_table(table):
    print(f"Common cards: {display_card(table.common_cards)}")
    print(f"Blind: {table.blind}")
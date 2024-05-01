from typing import List
import requests
from mtg_kit.utils import MTG_FORMATS


def get_banned_cards(fmt: str) -> List[str]:
    """Get a list of card names banned in a given format.
    :param fmt: Format string. As per Scryfall.
    :return: A list of card names.
    """
    if fmt not in MTG_FORMATS:
        raise ValueError(f'Error: format (fmt) must be one of {MTG_FORMATS}')
    card_objs = get_card(f'banned:{fmt}')
    return [c['name'] for c in card_objs]


def get_card(query: str):
    """Runs a card search on the Scryfall API.
    :param query: A query string using Scryfall syntax.
    :return: A list of Scryfall card objects.
    """
    cards = []
    page = 1
    while True:
        url = f"https://api.scryfall.com/cards/search?q={query}&page={page}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch cards: {response.text}")
            break
        data = response.json()
        cards.extend([card for card in data['data']])

        if not data['has_more']:
            break
        page += 1

    return cards


def get_card_printings(card_name: str):
    card = get_card(card_name)[0]  # assume the first card is the wanted one
    prints_url = card['prints_search_uri']

    # Fetch all printings
    response = requests.get(prints_url)
    data = response.json()

    # Check if the printings fetch was successful
    if response.status_code == 200:
        card_printings = [cp for cp in data['data']]
    else:
        print(f"Failed to retrieve card printings: {data['details']}")
        card_printings = None

    return card_printings


if __name__ == '__main__':
    # Get Pauper banlist
    pauper_banlist = get_banned_cards('pauper')
    print(pauper_banlist)

    # Search card
    r = get_card_printings('Demand Answers')
    print(r)
    
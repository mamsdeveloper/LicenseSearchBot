from models import Item
from search_utils.utils import normalize


def direct_search(query: str, items: list[Item]) -> list[Item]:
    query = normalize(query)

    relevant_items = [
        item for item in items
        if query in normalize(item.name)
    ]
    return relevant_items

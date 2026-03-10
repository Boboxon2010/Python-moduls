# list_utils.py

def list_length(items: list) -> int:
    return len(items)


def add_item(items: list, item) -> list:
    items.append(item)
    return items


def insert_item(items: list, index: int, item) -> list:
    items.insert(index, item)
    return items


def remove_item(items: list, item) -> list:
    if item in items:
        items.remove(item)
    return items


def remove_by_index(items: list, index: int):
    if 0 <= index < len(items):
        return items.pop(index)
    return None


def sort_list(items: list, reverse: bool = False) -> list:
    return sorted(items, reverse=reverse)


def reverse_list(items: list) -> list:
    return items[::-1]


def count_item(items: list, item) -> int:
    return items.count(item)


def find_index(items: list, item) -> int:
    return items.index(item) if item in items else -1


def unique_items(items: list) -> list:
    return list(dict.fromkeys(items))


def sum_list(items: list) -> float:
    return sum(items)


def max_item(items: list):
    return max(items)


def min_item(items: list):
    return min(items)


def average_list(items: list) -> float:
    return sum(items) / len(items) if items else 0


def filter_even_numbers(items: list) -> list:
    return [x for x in items if isinstance(x, int) and x % 2 == 0]


def filter_odd_numbers(items: list) -> list:
    return [x for x in items if isinstance(x, int) and x % 2 != 0]


def flatten_list(items: list) -> list:
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result


def list_summary(items: list) -> dict:
    return {
        "length": len(items),
        "unique_count": len(set(items)) if all(isinstance(x, (int, float, str, tuple)) for x in items) else None,
        "first_item": items[0] if items else None,
        "last_item": items[-1] if items else None
    }
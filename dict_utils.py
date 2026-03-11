# dict_utils.py

def get_keys(data: dict) -> list:
    return list(data.keys())


def get_values(data: dict) -> list:
    return list(data.values())


def get_items(data: dict) -> list:
    return list(data.items())


def add_item(data: dict, key, value) -> dict:
    data[key] = value
    return data


def remove_item(data: dict, key) -> dict:
    if key in data:
        del data[key]
    return data


def update_item(data: dict, key, value) -> dict:
    data[key] = value
    return data


def key_exists(data: dict, key) -> bool:
    return key in data


def value_exists(data: dict, value) -> bool:
    return value in data.values()


def merge_dicts(dict1: dict, dict2: dict) -> dict:
    return {**dict1, **dict2}


def dict_length(data: dict) -> int:
    return len(data)


def clear_dict(data: dict) -> dict:
    data.clear()
    return data


def sort_dict_by_key(data: dict) -> dict:
    return dict(sorted(data.items(), key=lambda item: item[0]))


def sort_dict_by_value(data: dict) -> dict:
    return dict(sorted(data.items(), key=lambda item: item[1]))


def invert_dict(data: dict) -> dict:
    return {value: key for key, value in data.items()}


def filter_dict_by_value(data: dict, min_value) -> dict:
    return {k: v for k, v in data.items() if v >= min_value}


def dict_summary(data: dict) -> dict:
    return {
        "length": len(data),
        "keys": list(data.keys()),
        "values": list(data.values()),
        "items": list(data.items())
    }
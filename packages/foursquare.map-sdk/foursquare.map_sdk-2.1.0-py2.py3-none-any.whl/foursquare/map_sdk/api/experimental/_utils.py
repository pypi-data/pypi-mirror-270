from uuid import uuid4


def remove_none_values(d):
    if isinstance(d, dict):
        return {k: remove_none_values(v) for k, v in d.items() if v is not None}
    elif isinstance(d, list):
        return [remove_none_values(elem) for elem in d if elem is not None]
    else:
        return d


def generate_uuid() -> str:
    return str(uuid4())

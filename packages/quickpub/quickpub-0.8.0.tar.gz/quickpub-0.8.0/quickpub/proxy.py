import danielutils
import requests


# need it like this for the testing
def cm(*args, **kwargs) -> tuple[int, bytes, bytes]:
    return danielutils.cm(*args, **kwargs)


def get(*args, **kwargs):
    return requests.get(*args, **kwargs)


def add_verbose_keyword(func):
    def wrapper(*args, verbose: bool = False, **kwargs):
        if verbose:
            return func(*args, **kwargs)

    return wrapper


__all__ = [
    "cm",
    "get",
    'add_verbose_keyword'
]

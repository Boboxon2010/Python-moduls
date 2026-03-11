# text_utils.py

def to_upper(text: str) -> str:
    return text.upper()


def to_lower(text: str) -> str:
    return text.lower()


def capitalize_text(text: str) -> str:
    return text.capitalize()


def title_text(text: str) -> str:
    return text.title()


def reverse_text(text: str) -> str:
    return text[::-1]


def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOUo‘u‘"
    return sum(1 for char in text if char in vowels)


def count_consonants(text: str) -> int:
    vowels = "aeiouAEIOUo‘u‘"
    return sum(1 for char in text if char.isalpha() and char not in vowels)


def count_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str, with_spaces: bool = True) -> int:
    return len(text) if with_spaces else len(text.replace(" ", ""))


def is_palindrome(text: str) -> bool:
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def remove_spaces(text: str) -> str:
    return text.replace(" ", "")


def replace_word(text: str, old: str, new: str) -> str:
    return text.replace(old, new)


def starts_with(text: str, prefix: str) -> bool:
    return text.startswith(prefix)


def ends_with(text: str, suffix: str) -> bool:
    return text.endswith(suffix)


def split_text(text: str, separator: str = " ") -> list:
    return text.split(separator)


def join_text(words: list, separator: str = " ") -> str:
    return separator.join(words)


def remove_punctuation(text: str) -> str:
    punctuation = "!?.,:;'-_()[]{}\"/"
    return "".join(char for char in text if char not in punctuation)


def find_substring(text: str, sub: str) -> int:
    return text.find(sub)


def repeat_text(text: str, n: int) -> str:
    return text * n


def text_summary(text: str) -> dict:
    return {
        "original": text,
        "upper": text.upper(),
        "lower": text.lower(),
        "word_count": count_words(text),
        "char_count": count_characters(text),
        "vowel_count": count_vowels(text),
    }
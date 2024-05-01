from enum import Enum, auto


class Language(Enum):
    NL = auto()
    EN = auto()


class CONFIG:
    language = Language.EN


NS = {"scia": "http://www.scia.cz"}


def set_language(language: str) -> None:
    """
    Sets the language according to the given string. Checks whether 'nl' or 'en' is 
    present in the given argument and sets the config accordingly.
    """
    if 'nl' in language.lower():
        CONFIG.language = Language.NL
    elif 'en' in language.lower():
        CONFIG.language = Language.EN
    else:
        raise ValueError(
            f"Language '{language}' not recognized. Please provide a string with either 'nl' or 'en' in it.")

from abc import ABC, abstractmethod
from re import IGNORECASE
import regex


class CopyParser(ABC):

    """
    Social copy is parsed via regex. Each subclass parses copy for their respective platform.
    """

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def parse(self) -> str:
        pass


class LinkedInParser(CopyParser):
    """
    Parser for LinkedIn. Parses copy and returns the platform specific substring of the full copy that was passed.
    """

    def __init__(self, post_data) -> None:
        self.post_data: str = (post_data,)
        self.full_copy: str = post_data["LinkedIn/Facebook Copy"]
        self.parsed_copy: str = None
        # self._regex_pattern: str = r"(?<=linkedin|linkedin:|linkedin-|linkedin\ ?\n|linkedin copy:|linkedin copy-|linkedin copy\ ?\n)."
        self._regex_pattern: str = r"(\w?)*-?li-?\w*(\ copy)*(:|-)?\n?\ ?(\(.*\))?\ ?\K.*"

    def parse(self) -> str:
        search_result = regex.search(self._regex_pattern, self.full_copy, IGNORECASE)
        self.parsed_copy: str = search_result[0]
        return self.parsed_copy


class TwitterParser(CopyParser):

    """
    Parser for Twitter. Parses copy and returns the platform specific substring of the full copy that was passed.
    """

    def __init__(self, full_copy) -> None:
        self.full_copy: str = full_copy
        self.parsed_copy: str = None
        self._regex_pattern: str = ""

    def parse(self) -> str:
        # Should return parsed copy as string
        pass


class FacebookParser(CopyParser):

    """
    Parser for Facebook. Parses copy and returns the platform specific substring of the full copy that was passed.
    """

    def __init__(self, full_copy) -> None:
        self.full_copy: str = full_copy
        self.parsed_copy: str = None
        self._regex_pattern: str = ""

    def parse(self) -> str:
        # Should return parsed copy as string
        pass


class InstagramParser(CopyParser):

    """
    Parser for Instagram. Parses copy and returns the platform specific substring of the full copy that was passed.
    """

    def __init__(self, full_copy) -> None:
        self.full_copy: str = full_copy
        self.parsed_copy: str = None
        self._regex_pattern: str = ""

    def parse(self) -> str:
        # Should return parsed copy as string
        pass

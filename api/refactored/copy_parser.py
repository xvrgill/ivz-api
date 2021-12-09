from abc import ABC, abstractmethod
from re import IGNORECASE, MULTILINE
import regex

# Exceptions
from api.refactored.exceptions import EmptyLinkedinFacebookCopyError, RegexPatternResultError


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
        self.post_data: str = post_data
        try:
            self.full_copy: str = post_data["LinkedIn/Facebook Copy"]
        except:
            raise EmptyLinkedinFacebookCopyError(post_data)
        self.parsed_copy: str = None
        self.if_pattern: str = r"(?(?=(li[:\-\n]+)|linkedin)((\w?)*-?li-?\w*(\ copy)*(:|-)?\n?\ ?(\(.*\))?\ ?\K(?P<licopy>.*)))"
        self.elif_pattern: str = r"(fb|ig|facebook|instagram):?-?\ ?\n?\K.*"

    def parse(self) -> str:
        if_result = regex.search(self.if_pattern, self.full_copy, IGNORECASE)[0]
        if if_result != "":
            # Pass parsed LI copy if found
            self.parsed_copy: str = if_result
        elif len(regex.search(self.elif_pattern, self.full_copy, IGNORECASE)[0]) != 0:
            # Raise exception when non-target platform copy is found
            raise RegexPatternResultError(self.full_copy)
        else:
            # Parsed copy is the full copy (no distinction made between platforms)
            self.parsed_copy = self.full_copy

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

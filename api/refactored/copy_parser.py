from abc import ABC, abstractmethod
from re import IGNORECASE
import regex

# Exceptions
from api.refactored.exceptions import RegexPatternResultError


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

    def parse(self) -> str:
        # TODO: Need to filter out thought leader linkedin posts
        # TODO: Need error out if linkedin/facebook copy is blank

        full_copy = self.post_data["linkedin_facebook_copy"]

        linkedin_identifier_pattern = r"\bli\b|linkedin(\ copy)?[/\w:\-\n]*"
        p1 = regex.compile(linkedin_identifier_pattern, IGNORECASE)
        m1 = p1.search(full_copy)

        target_pattern = r"(((\w*-?\bli\b-?\w*)|linkedin)(\ copy)?[/\w]*[\n\ ]?(\(.*\))?[:\-]?\ ?\K(?P<licopy>.*))"
        p2 = regex.compile(target_pattern, IGNORECASE)
        m2 = p2.search(full_copy)

        nontarget_pattern = r"(\bfb\b|\big\b|(hr?sy)|facebook|instagram|hearsay):?-?\ ?\n?"
        p3 = regex.compile(nontarget_pattern, IGNORECASE)
        m3 = p3.search(full_copy)

        if m1 and m2:
            return m2.group()
        elif m1 and not m2:
            raise RegexPatternResultError(
                full_copy,
                "Linkedin copy found but could not be parsed. Issue with regex pattern likely.",
            )
        elif m3:
            raise RegexPatternResultError(
                full_copy,
                "Linkedin copy not found, but nontarget platfom copy found. Specify linkedin copy in Air Table.",
            )
        else:
            # TODO: Need to separate out various posts here (eg. Post 1, Post 2, Post 3...)
            return full_copy


class TwitterParser(CopyParser):

    """
    Parser for Twitter. Parses copy and returns the platform specific substring of the full copy that was passed.
    """

    pass


class FacebookParser(CopyParser):

    """
    Parser for Facebook. Parses copy and returns the platform specific substring of the full copy that was passed.
    """

    pass


class InstagramParser(CopyParser):

    """
    Parser for Instagram. Parses copy and returns the platform specific substring of the full copy that was passed.
    """

    pass

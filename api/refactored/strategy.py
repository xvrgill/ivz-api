from typing import Dict
from api.refactored.copy_parser import (
    LinkedInParser,
    # TwitterParser,
    # FacebookParser,
    # InstagramParser,
)
from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def parse_copy(self):
        pass

    # @abstractmethod
    # def add_to_db(self):
    #     pass

    # @abstractmethod
    # def add_to_socialstudio(self):
    #     pass


class LinkedInStrategy(Strategy):
    def parse_copy(self, post_data: Dict) -> str:
        """
        Returns parsed copy for LinkedIn.
        """
        parser: LinkedInParser = LinkedInParser(post_data)
        parsed = parser.parse()

        return parsed

    # def add_to_db(self):
    #     pass

    # def add_to_socialstudio(self):
    #     pass


class TwitterStrategy(Strategy):
    # def parse_copy(self, full_copy: str) -> str:
    #     """
    #     Returns parsed copy for LinkedIn.
    #     """
    #     parser: TwitterParser = TwitterParser()
    #     parsed = parser.parse(full_copy)

    #     return parsed

    # def add_to_db(self):
    #     pass

    # def add_to_socialstudio(self):
    #     pass
    pass


class FacebookStrategy(Strategy):
    # def parse_copy(self, full_copy: str) -> str:
    #     """
    #     Returns parsed copy for LinkedIn.
    #     """
    #     parser: FacebookParser = FacebookParser()
    #     parsed = parser.parse(full_copy)

    #     return parsed

    # def add_to_db(self):
    #     pass

    # def add_to_socialstudio(self):
    #     pass
    pass


class InstagramStrategy(Strategy):
    # def parse_copy(self, full_copy: str) -> str:
    #     """
    #     Returns parsed copy for LinkedIn.
    #     """
    #     parser: InstagramParser = InstagramParser()
    #     parsed = parser.parse(full_copy)

    #     return parsed

    # def add_to_db(self):
    #     pass

    # def add_to_socialstudio(self):
    #     pass
    pass

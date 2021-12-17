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

    @abstractmethod
    def find_image(self):
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

    def find_image(self):
        """
        Method gets a singular image from air that is most likely to be associated with a LinkedIn post using regex.

        Sudo Code:
        Extract image list from passed data
        Loop through list to find li or linkedin in the image title
        If no linkedin titled image is found, look for dimensions of 1920x1080
        If those dimensions aren't found, look for dimensions of 1200x627
        When any of the above conditions are met proceed by passing the index, if none are found raise error
        """

        pass

    # TODO: Implement a method that adds the post data to database for later retrieval
    # def add_to_db(self):
    #     pass

    # TODO: Implement a method that creates a linkedin post in social studio. Pass in the data and use scraper.
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

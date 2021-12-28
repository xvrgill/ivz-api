from re import IGNORECASE
import requests
import regex
from api.refactored.copy_parser import (
    LinkedInParser,
    # TwitterParser,
    # FacebookParser,
    # InstagramParser,
)
from api.refactored.ss_scraper import SSScraper
from abc import ABC, abstractmethod
import os
import shutil


class Strategy(ABC):
    @abstractmethod
    def parse_copy(self):
        pass

    @abstractmethod
    def find_image(self):
        pass

    @abstractmethod
    def cache_image(self):
        pass

    # @abstractmethod
    # def add_to_db(self):
    #     pass

    # @abstractmethod
    # def add_to_socialstudio(self):
    #     pass


class LinkedInStrategy(Strategy):
    # TODO: An init might be useful here to avoid continuously passing post_data

    def parse_copy(self, post_data: dict) -> str:
        """
        Returns parsed copy for LinkedIn.
        """
        parser: LinkedInParser = LinkedInParser(post_data)
        parsed = parser.parse()

        return parsed

    def find_image(self, post_data: dict) -> dict:
        """
        Method gets a singular image from air that is most likely to be associated with a LinkedIn post using regex. Checks filename for reference to linkedin, checks image width for 1920, checks image width for fallback of 1200 (in that order). Returns image dictionary when first match is found.

        :return - dictionary containing image data
        """

        image_list = post_data["images"]

        # Regex filename search loop
        file_name_pattern = r"li|linkedin"
        p1 = regex.compile(file_name_pattern, IGNORECASE)
        for image in image_list:
            image_title = image["filename"]
            match = p1.search(image_title)
            if match:
                # TODO: Ensure image has a proper file extension (jpg or png)
                return image

        # Dimensions check loop
        for image in image_list:
            image_width: str = image["width"]
            if image_width == "1920":
                # TODO: Ensure image has a proper file extension (jpg or png)
                return image

        # Fallback dimensions search loop
        for image in image_list:
            image_width: str = image["width"]
            if image_width == "1200":
                # TODO: Ensure image has a proper file extension (jpg or png)
                return image

    def cache_image(self, post_data: dict, cache_dir: str = "images"):
        """
        Caches image for later use.
        """
        image_data: dict = self.find_image(post_data)
        file_name: str = image_data["filename"]
        cache_path: str = os.path.join(cache_dir, file_name)
        url: str = image_data["url"]

        with requests.get(url, stream=True) as r:
            if r.status_code == 200:
                with open(cache_path, "wb") as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)

        if os.path.isfile(cache_path):
            self.image_cache_path = cache_path
            return cache_path

    def rm_cached_image(self):
        if os.path.isfile(self.image_cache_path):
            os.remove(self.image_cache_path)

    # TODO: Implement a method that adds the post data to database for later retrieval
    # def add_to_db(self):
    #     pass

    # TODO: Implement a method that creates a linkedin post in social studio. Pass in the data and use scraper.
    def add_to_socialstudio(self, compose_data: dict) -> str:
        scraper = SSScraper(compose_data, "linkedin")
        scraper.open_chrome()
        scraper.login()
        return scraper.compose_post()


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

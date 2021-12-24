import os
from api.refactored.strategies.scraper_strategy import (
    LinkedinSSScraperStrategy as lss,
)

# Chromedriver path - /Users/xaviergill/opt/anaconda3/envs/ivz_scheduling_api/lib/python3.9/site-packages/helium/_impl

# Dict to hold strategy mappings
strategy_mapping = dict(linkedin=lss())

# Class definition for scraper
class SSScraper:
    def __init__(
        self, post_data: dict, platform: str, strategy_mapping: dict = strategy_mapping
    ) -> None:
        self.post_data = post_data
        self.strategy_mapping = strategy_mapping
        self.platform = platform
        self.strategy = self.assign_strategy()

    # Function that initializes the strategy to be used for the class instance
    def assign_strategy(self) -> lss:
        return self.strategy_mapping[self.platform]

    # Instantiate driver to enable use of both heium and selenium commands
    def open_chrome(self):
        self.strategy.open_chrome()

    # Log into Social Studio
    def login(self) -> None:
        self.strategy.login()

    def compose_post(self, as_draft=True):
        """
        Create a post in social studio depending on the data that was passed in.
        """
        compose_data: dict = self.post_data
        self.strategy.compose_post(compose_data, as_draft=as_draft)

    def open_in_new_tab(self, url: str = "") -> None:
        self.strategy.open_in_new_tab(url)

    def close_current_tab(self) -> None:
        self.strategy.close_current_tab()

    def close_browser(self) -> None:
        self.strategy.kill_browser()


if __name__ == "__main__":

    post_data = {
        "platform": "linkedin",
        "post_to": "invesco us",
        "parsed_copy": "This is a test piece of copy 2.",
        "image_path": "images/biden-michigan-ap-rc-200909_hpMain_16x9_1600.jpg",
    }

    scraper = SSScraper(post_data, "linkedin")
    scraper.open_chrome()
    scraper.login()
    scraper.compose_post()

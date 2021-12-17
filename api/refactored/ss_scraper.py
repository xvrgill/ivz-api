from helium import *
import os
from api.refactored.strategies.scraper_strategy import LinkedinSSScraperStrategy as lss

# Chromedriver path - /Users/xaviergill/opt/anaconda3/envs/ivz_scheduling_api/lib/python3.9/site-packages/helium/_impl

# Dict to hold strategy mappings
strategy_mapping = dict(linkedin=lss)

# Class definition for scraper
class SSScraper:
    def __init__(self, post_data: dict, strategy_mapping: dict = strategy_mapping) -> None:
        self.post_data = post_data
        self.strategy_mapping = strategy_mapping
        # self.strategy = self.assign_strategy()

    # Function that initializes the strategy to be used for the class instance
    # def assign_strategy(self, data=post_data) -> lss:
    #     pass

    # Instantiate driver to enable use of both heium and selenium commands
    def open_chrome(self):
        global driver
        driver = start_chrome()

    # Log into Social Studio
    def login(self) -> None:
        go_to("https://socialstudio.radian6.com/login")
        write(os.environ.get("SOCIAL_STUDIO_USER_NAME"), into="Username")
        write(os.environ.get("SOCIAL_STUDIO_PASSWORD"), into="Password")
        click("Login")

    # TODO: Build out scraper logic for creating a post
    # def create_post(self, post_data=post_data, as_draft=True):
    #     """
    #     Create a post in social studio depending on the data that was passed in.
    #     """
    #     pass

    def open_in_new_tab(self, url: str = "") -> None:
        """
        Default behavior: Opens a new tab with an empty string as a URL

        Kwargs:
            -- url: specify a url to open in the new tab
        """

        driver.execute_script(f"window.open({url})")

    def close_current_tab(self) -> None:
        """
        Default behavior: close current tab
        """

        driver.execute_script("window.close();")

    # Kill entire browser instance
    def close_browser(self) -> None:
        kill_browser()


if __name__ == "__main__":
    scraper = SSScraper()
    scraper.open_chrome()

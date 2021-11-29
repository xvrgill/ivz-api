import json
from helium import *
import os
from datetime import datetime

# Chromedriver path - /Users/xaviergill/opt/anaconda3/envs/ivz_scheduling_api/lib/python3.9/site-packages/helium/_impl

# Class definition for scraper
class SSScraper:
    def __init__(self) -> None:
        self.loogged_in = False

    # Instantiate driver to enable use of both heium and selenium commands
    def open_chrome(self):
        global driver
        driver = start_chrome()

    # Log into Social Studio
    # TODO: store url in environement variable
    # TODO: store credentials in environement variables
    def login(self):
        go_to("https://socialstudio.radian6.com/")
        write(os.environ.get("SOCIAL_STUDIO_USER_NAME"), into="Username")
        write(os.environ.get("SOCIAL_STUDIO_PASSWORD"), into="Password")
        click("Login")

    # Generate timestamps from serialized date
    def create_timestamp(self, month, day, year):
        date_object = datetime(year, month, day)
        timestamp = datetime.timestamp(date_object)
        return timestamp

    # Get post data based on passed in dates
    def fetch_posts(
        self,
        from_month: str = 1,
        from_day: str = 1,
        from_year: str = 2021,
        to_month: str = 12,
        to_day: str = 30,
        to_year: str = 2021,
    ):
        # Create relevant unix timestamps
        from_timestamp = self.create_timestamp(int(from_month), int(from_day), int(from_year))
        to_timestamp = self.create_timestamp(int(to_month), int(to_day), int(to_year))
        workspace_id = os.environ.get("SOCIAL_STUDIO_WORKSPACE_ID")

        # Open new tab and sed request to Social Studio API
        data_url = f"https://p.socialstudio.radian6.com/api/v1/calendaritems?since={from_timestamp}&until={to_timestamp}&workspace_id={workspace_id}&status_types="
        driver.execute_script(f"window.open('{data_url}');")

        # Switch to the window we just opened
        switch_to(find_all(Window())[1])

        # Get text from this window - contains requested data
        data = json.loads(Text().value)
        data = data["response"]

        # Close window to return to Social Studio session
        driver.execute_script("window.close();")

        return data

    # Kill entire browser instance
    def close_browser(self):
        kill_browser()


if __name__ == "__main__":
    scraper = SSScraper()
    scraper.open_chrome()

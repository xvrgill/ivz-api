from abc import ABC, abstractmethod
from helium import *
from selenium.webdriver.common.by import By
import os
from time import sleep


class SSScraperStrategy(ABC):
    @abstractmethod
    def open_chrome(self) -> None:
        pass

    @abstractmethod
    def open_in_new_tab(self) -> None:
        pass

    @abstractmethod
    def close_current_tab(self) -> None:
        pass

    @abstractmethod
    def close_browser(self) -> None:
        pass

    @abstractmethod
    def login(self) -> None:
        pass

    @abstractmethod
    def compose_post(self) -> None:
        pass


class LinkedinSSScraperStrategy(SSScraperStrategy):
    """
    Linkedin strategy that is passed to the social studio scraper.
    """

    ### Browser Control ###

    def open_chrome(self):
        """
        Open instance of Google Chrome browser.
        """
        global driver
        driver = start_chrome()

    def open_in_new_tab(self, url: str = "") -> None:
        """
        Opens a new tab with an empty string as a URL

        :url -- specify a url to open in the new tab
        """
        driver.execute_script(f"window.open({url})")

    def close_current_tab(self) -> None:
        """
        Default behavior: close current tab
        """
        driver.execute_script("window.close();")

    def close_browser(self) -> None:
        """
        Kills entire browser instance
        """
        kill_browser()

    # Compose Control
    def login(self) -> None:
        """
        Log into social studio in current tab.
        """
        go_to("https://socialstudio.radian6.com/login")
        write(os.environ.get("SOCIAL_STUDIO_USER_NAME"), into="Username")
        write(os.environ.get("SOCIAL_STUDIO_PASSWORD"), into="Password")
        click("Login")

    def compose_post(self, compose_data: dict, as_draft: bool = True) -> str:
        """
        Compose post with passed post data.
        """

        # TODO: Handle links when they are present in the copy
        go_to("https://p.socialstudio.radian6.com/publish/w/a10353d3-e7d5-4637-8698-7107792fd27e/compose/#linkedin")
        sleep(1)
        post_to_field = S("//html/body/section[4]/div/div[2]/div[1]/div/div[1]/div/div[2]/div")
        click(post_to_field)
        wait_until(Text("Invesco US").exists)
        invesco_us_profile = S("//html/body/section[4]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/ul/li[3]")
        click(invesco_us_profile)
        press(TAB)
        write(compose_data["parsed_copy"], into="Content")
        sleep(3)
        # Handle image differently depending on if the content box has a link or not
        if Text("Headline").exists():
            upload_image = driver.find_element(By.XPATH, "/html/body/section[4]/div/div[2]/div[1]/div/div[3]/div/div[3]/div/div[4]/div[2]/div/div[2]/div[2]/div/form/input")
            image_path: str = compose_data["image_path"]
            upload_image.send_keys(os.path.abspath(image_path))
            # Image check mark
            wait_until(lambda: S("//html/body/section[4]/div/div[2]/div[1]/div/div[3]/div/div[3]/div/div[4]/div[2]/div/div[1]/div/div[1]/i").exists())
            deployment_box = S("//html/body/section[4]/div/div[2]/div[1]/div/div[5]/div/div/div[1]")
            click(deployment_box)
            sleep(0.5)
            schedule_from_ss_selection = S("//html/body/div[8]/div[2]/ul/li[2]")
            click(schedule_from_ss_selection)
            sleep(1)
            # TODO: Make sure that passed date is in the future
            write("01/02/2022", into=S("//html/body/section[4]/div/div[2]/div[1]/div/div[5]/div/div/div[2]/div/input"))
            press(ESCAPE)
            sleep(1)
            # TODO: Make sure that passed time is in the future if the passed date is today
            write("03:00 am", into=S("//html/body/section[4]/div/div[2]/div[1]/div/div[5]/div/div/div[2]/div/span/input"))
            press(ESCAPE)
            sleep(1)
            select(ComboBox(below="Link Shortening"), "Do Not Shorten")
            sleep(3)
        else:
            upload_image = driver.find_element(By.XPATH, "//html/body/section[4]/div/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/form/input")
            image_path: str = compose_data["image_path"]
            upload_image.send_keys(os.path.abspath(image_path))
            wait_until(Text("Please be advised that the files you have uploaded will be available across the tenant").exists)
            deployment_box = S("//html/body/section[4]/div/div[2]/div[1]/div/div[5]/div/div/div[1]/div")
            click(deployment_box)
            sleep(0.5)
            schedule_from_ss_selection = S("//html/body/div[12]/div[2]/ul/li[2]")
            click(schedule_from_ss_selection)
            sleep(1)
            # TODO: Make sure that passed date is in the future
            write("01/02/2022", into=S("//html/body/section[4]/div/div[2]/div[1]/div/div[5]/div/div/div[2]/div/input"))
            press(ESCAPE)
            sleep(1)
            # TODO: Make sure that passed time is in the future if the passed date is today
            write("03:00 am", into=S("//html/body/section[4]/div/div[2]/div[1]/div/div[5]/div/div/div[2]/div/span/input"))
            press(ESCAPE)
            sleep(1)
            select(ComboBox(below="Link Shortening"), "Do Not Shorten")
            sleep(3)

        if as_draft:
            click("Save as a Draft")

        new_draft_card = S("//html/body/section[6]/div[2]/div[1]/div[2]/div/div[2]")
        click(new_draft_card)
        draft_url: str = str(driver.current_url)
        url_split: list = draft_url.split("/")
        draft_id: str = url_split.pop()
        # self.close_browser()

        return draft_url, draft_id

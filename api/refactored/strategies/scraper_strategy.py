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

    Sudo code:
        Go to compose linkedin post page
        Select social account
        Enter social copy into copy field
        Handle preview properties scraped by social studio (preview title, preview caption, and preview image)
        If no link, add image
        If creative asset is video file,
    """

    # Browser Control
    def open_chrome(self):
        global driver
        driver = start_chrome()

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

    def compose_post(self, data: dict, as_draft: bool = True) -> None:
        """
        Compose post with passed post data.
        """
        # Navigate to compose page
        go_to(
            "https://p.socialstudio.radian6.com/publish/w/a10353d3-e7d5-4637-8698-7107792fd27e/compose/#linkedin"
        )
        sleep(1)
        # Enter post to field
        post_to_field = S("//html/body/section[4]/div/div[2]/div[1]/div/div[1]/div/div[2]/div")
        click(post_to_field)
        invesco_us_profile = S(
            "//html/body/section[4]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/ul/li[3]"
        )
        wait_until(Text("Invesco US").exists)
        click(invesco_us_profile)
        press(TAB)
        write("This is a test", into="Content")
        image_path: str = data["image_path"]
        upload_image = driver.find_element(
            By.XPATH,
            "//html/body/section[4]/div/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/form/input",
        )
        upload_image.send_keys(os.path.abspath(image_path))
        deployment_box = S("//html/body/section[4]/div/div[2]/div[1]/div/div[5]/div/div/div[1]/div")
        schedule_from_ss_selection = S("//html/body/div[12]/div[2]/ul/li[2]")
        click(deployment_box)
        sleep(0.5)
        click(schedule_from_ss_selection)
        sleep(1)
        write(
            "12/25/2021",
            into=S("//html/body/section[4]/div/div[2]/div[1]/div/div[5]/div/div/div[2]/div/input"),
        )
        press(ESCAPE)
        sleep(1)
        write(
            "03:00 am",
            into=S(
                "//html/body/section[4]/div/div[2]/div[1]/div/div[5]/div/div/div[2]/div/span/input"
            ),
        )
        press(ESCAPE)
        sleep(1)
        select(ComboBox(below="Link Shortening"), "Do Not Shorten")
        sleep(3)
        # Create post as draft by default
        if as_draft:
            click("Save as a Draft")

        # TODO: Return the draft ID if succesful for storage in database
        # Draft url structure:
        # https://p.socialstudio.radian6.com/publish/w/a10353d3-e7d5-4637-8698-7107792fd27e/compose/#linkedin/4c717566-3cdd-4045-aeed-0cb852ee4823
        # Get this by using driver.current_url

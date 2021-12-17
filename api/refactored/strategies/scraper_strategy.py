from abc import ABC

# IMPORTANT: MAY NOT NEED THESE STRATEGIES BECAUSE THE PLATFORM STRATEGY CAN IMPLEMENT THIS LOGIC. KEEPING HERE FOR LATER

# TODO: Add abstract methods to base class
class SSScraperStrategy(ABC):
    pass


# TODO: Implement sudo code
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

    pass

from api.refactored.exceptions import StrategyNotSupportedError
from api.refactored.strategies.platform_strategy import LinkedInStrategy


class SocialStudioPostContext:
    def __init__(self, post_data: dict, platform: str, compose_data: dict = None) -> None:
        self.post_data = post_data
        self.platform = platform
        self.strategy = self.assign_strategy()
        self.compose_data = compose_data

    def assign_strategy(self):
        if self.platform.lower() == "linkedin":
            return LinkedInStrategy()
        else:
            # Raise unsupported platform assigned error
            raise StrategyNotSupportedError(
                self.platform,
                message=f"{self.platform.title()} is not currently supported as a strategy.",
            )

    def parse_copy(self) -> str:
        return self.strategy.parse_copy(self.post_data)

    def cache_image(self) -> str:
        return self.strategy.cache_image(self.post_data)

    def rm_cached_image(self) -> None:
        self.strategy.rm_cached_image()

    # def add_to_db(self):
    #     pass

    def add_to_socialstudio(self) -> str:
        return self.strategy.add_to_socialstudio(self.compose_data)

    def run(self) -> dict:

        # locally store data used to compose ss post
        parsed_copy = self.parse_copy()
        # TODO: Maybe use context manager for this to remove cached file when done?
        image_path = self.cache_image()
        # create dictionary for data to be used to compose ss post
        self.compose_data = dict(parsed_copy=parsed_copy, image_path=image_path)
        # compose post in social studio
        if self.compose_data:
            draft_id = self.add_to_socialstudio()
        # delete cached image
        self.rm_cached_image()
        # choose data to be returned
        return (parsed_copy, image_path, draft_id)


if __name__ == "__main__":
    # Test function
    def main() -> str:
        test_data = {
            "linkedin_facebook_copy": """LinkedIn: Who said financial education can't be fun? How Not To Suck At Money is a free interactive game to help step up students' money decision skills, and it's launching November 8th. Sign up now: HNTSAM.com #HowNotToSuckAtMoney

Facebook: Who said financial education can't be fun? We're launching a free interactive game to help college students make better money-managing decisions and have fun while doing it. Launching November 8th. Sign up now: HNTSAM.com #HowNotToSuckAtMoney

Instagram: How Not To Suck At Money is backed by real research and real lessons to help college students get smarter about their money today. Our free interactive game helps students make better money decisions. Launching November 8th. Sign up now. Link in bio. #HowNotToSuckAtMoney"""
        }
        context = SocialStudioPostContext(test_data, "linkedin")
        parsed = context.parse_copy()
        print(parsed)

    main()

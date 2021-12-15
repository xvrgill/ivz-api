from api.refactored.exceptions import StrategyNotSupportedError
from api.refactored.strategy import LinkedInStrategy


class SocialStudioPostContext:
    def __init__(self, post_data: dict, platform: str) -> None:
        self.post_data = post_data
        self.platform = platform
        self.strategy = self.assign_strategy()

    def assign_strategy(self):
        if self.platform.lower() == "linkedin":
            return LinkedInStrategy()
        else:
            # Raise unsupported platform assigned error
            raise StrategyNotSupportedError(
                self.platform,
                message=f"{self.platform.title()} is not currently supported as a strategy.",
            )

    def parse_copy(self):
        parsed_copy = self.strategy.parse_copy(self.post_data)
        return parsed_copy

    # def add_to_db(self):
    #     pass

    # def add_to_socialstudio(self):
    #     pass


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

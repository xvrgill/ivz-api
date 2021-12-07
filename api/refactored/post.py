from api.refactored.strategy import LinkedInStrategy


class SocialStudioPostContext:
    def __init__(self, post_data, strategy, parsed_copy=None) -> None:
        self.post_data = post_data
        self.strategy = strategy
        self.parsed_copy = parsed_copy

    def parse_copy(self):
        self.parsed_copy = self.strategy.parse_copy(self.post_data)

    def add_to_db(self):
        pass

    def add_to_socialstudio(self):
        pass


# Test function
def main() -> str:
    test_data = {
        "LinkedIn/Facebook Copy": "IVZ-LI-IDI0610aa: (InvescoUS) The lessons NCAA Legend and Invesco QQQ Agent of Innovation Grant Hill learned during his basketball career have transferred into the business world and through to his personal life. Watch his full conversation with 15-year-old CEO Trey Brown:  Agents of Innovation: Grant Hill & Trey Brown."
    }
    _strategy = LinkedInStrategy()
    context = SocialStudioPostContext(test_data, _strategy)
    context.parse_copy()
    print(context.parsed_copy)


if __name__ == "__main__":
    main()

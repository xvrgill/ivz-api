from api.refactored.strategy import LinkedInStrategy


class SocialStudioPostContext:
    def __init__(self, post_data, strategy, parsed_copy=None) -> None:
        self.post_data = post_data
        self.strategy = strategy
        self.parsed_copy = parsed_copy

    # @property
    # def strategy(self):
    #     return self.strategy

    # @strategy.setter
    # def strategy(self, strategy) -> None:
    #     self.strategy = strategy

    def parse_copy(self):
        self.parsed_copy = self.strategy.parse_copy(self.post_data)

    def add_to_db(self):
        pass

    def add_to_socialstudio(self):
        pass


def main() -> str:
    test_data = {"LinkedIn/Facebook Copy": "Hello World"}
    _strategy = LinkedInStrategy()
    context = SocialStudioPostContext(test_data, _strategy)
    context.parse_copy()
    print(context.parsed_copy)


if __name__ == "__main__":
    main()

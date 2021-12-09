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
        "LinkedIn/Facebook Copy": "The research, effort, and development invested by [TAG] Moderna into mRNA technology extends far beyond the integral inclusion in the COVID-19 vaccine. Learn more about how this #AgentofInnovation is driving its purpose through technology.\nFacebook: Moderna’s role in pioneering the mRNA technology, which was integral to the COVID-19 vaccine, helped change lives. Their investment in that technology extends far beyond the pandemic and it could potentially be groundbreaking in confronting disease as a whole.\nIG: You may know them for their role in pioneering the mRNA technology that drives the COVID-19 vaccine, but @Moderna is also investing in innovative technology that is changing lives. Link in bio to learn more through our Innovation Realized series."
    }
    _strategy = LinkedInStrategy()
    context = SocialStudioPostContext(test_data, _strategy)
    context.parse_copy()
    print(context.parsed_copy)


if __name__ == "__main__":
    main()

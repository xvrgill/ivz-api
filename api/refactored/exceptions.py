### Copy Parser Exceptions ###
class CopyParserError(Exception):
    """
    Base class for copy parser exceptions
    """

    pass


class EmptyLinkedinFacebookCopyError(CopyParserError):
    """
    Exception raised when the key 'LinkedIn/Facebook Copy' is not found in data passed to the copy parser.

    Attributes:
        post_data -- dictionary of full data passed to the parser
        message -- explanation of error
    """

    def __init__(
        self,
        post_data: dict,
        message: str = "\nLinkedIn/Facebook Copy field is empty.\n\n",
    ):
        self.post_data = post_data
        self.message = message + "Post data:\n\n" + str(self.post_data) + "\n"
        super().__init__(self.message)


class RegexPatternResultError(CopyParserError):
    """
    Exception raised when parse() method of the copy parser instance does not return a valid result.
    If target platform regex expression does not find a match AND if non-target platform(s) does find a match, this exception will be raised.

    Purpose: Notify user that the parser found a match for a platform that is not of interest, and therefore will not be returned. Indicates an error with the underlying regex pattern OR the passed in string.

    Attributes:
        full_copy -- unparsed copy
        message -- explanation of error
    """

    def __init__(
        self,
        full_copy,
        message: str = "\n\nUnexpected error in regex pattern. No copy found for target platform, but copy for non-target platform was found. Check associated copy feild in Air Table. Copy in this field must include two letter abreviation or full platfom name (not case sensitive) followed by any of the following: colon, hyphen, or enter\n",
    ) -> None:
        self.full_copy = full_copy
        self.message = message
        super().__init__(self.message)


### Strategy Exceptions ###
class PlatformStrategyError(Exception):
    """
    Base class for platform specific strategy exceptions
    """

    pass


class StrategyNotSupportedError(PlatformStrategyError):
    """
    Exception raised when strategy assignment based on platform - passed as a string - does not map to a strategy class.

    Purpose: Platform was passed that is not currently supported

    Attributes:
        platform -- platform that was passed to the post context
        message -- explanation of error
    """

    def __init__(
        self,
        platform,
        message: str = "\n\nPlatform not supported. No strategy available for passed platform.\n",
    ) -> None:
        self.platform = platform
        self.message = message
        super().__init__(self.message)

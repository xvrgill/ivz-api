"""
Unit tests for platform strategies.
"""
from api.refactored.strategies.platform_strategy import LinkedInStrategy
import os


class TestLinkedinStrategy:
    ### Tests for method: find_image() ###
    def test_image_match_conditions(self, test_data) -> None:
        """Test -- image filename should contain a reference to linkedin"""
        image_data = LinkedInStrategy().find_image(test_data)
        assert ("li" or "linkedin" in image_data["filename"]) or (1920 or 1200 in image_data["width"])

    def test_filename_and_width_dtypes(self, test_data) -> None:
        """
        Test -- image filename should be string and width should be integer.

        Checks all list items in image key of post data to ensure that filename values are strings and width values are integers.
        Subsequently checks the singular return dictionary to ensure that the filename value is a string and the width value is an integer.
        """
        image_data = LinkedInStrategy().find_image(test_data)
        for image in test_data["images"]:
            assert type(image["filename"]) is str
            assert type(image["width"]) is int
        assert type(image_data["filename"]) is str
        assert type(image_data["width"]) is int

    ### Tests for method: cache_image() ###
    def test_cache_path_type(self, test_data) -> None:
        """Test -- cache path should be of type string."""
        cache_path = LinkedInStrategy().cache_image(test_data)
        assert type(cache_path) is str

    def test_cache_image_exists(self, test_data) -> None:
        """Test -- file should exist at cache path."""
        cache_path = LinkedInStrategy().cache_image(test_data)
        assert os.path.isfile(cache_path)

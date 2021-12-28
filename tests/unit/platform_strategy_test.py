"""
Unit tests for platform strategies.
"""
import pytest
from api.refactored.strategies.platform_strategy import LinkedInStrategy
import os


class TestLinkedinStrategy:
    ### Tests for method: find_image() ###
    def test_image_match_conditions(self, test_data) -> None:
        """Test -- image filename should contain a reference to linkedin"""
        passing_data, _ = test_data
        image_data = LinkedInStrategy().find_image(passing_data)
        assert ("li" or "linkedin" in image_data["filename"]) or (1920 or 1200 in image_data["width"])

    def test_filename_and_width_dtypes(self, test_data) -> None:
        """
        Test -- image filename should be string and width should be integer.

        Checks all list items in image key of post data to ensure that filename values are strings and width values are integers.
        Subsequently checks the singular return dictionary to ensure that the filename value is a string and the width value is an integer.
        """
        passing_data, _ = test_data
        image_data_1 = LinkedInStrategy().find_image(passing_data)
        for image in passing_data["images"]:
            assert type(image["filename"]) is str
            assert type(image["width"]) is int
        assert type(image_data_1["filename"]) is str
        assert type(image_data_1["width"]) is int

    def test_value_error_on_no_match(self, test_data) -> None:
        _, failing_data = test_data
        with pytest.raises(ValueError, match="Image does not contain reference to linkedin or proper image dimensions"):
            LinkedInStrategy().find_image(failing_data)

    ### Tests for method: cache_image() ###
    def test_cache_path_type(self, test_data) -> None:
        """Test -- cache path should be of type string."""
        passing_data, _ = test_data
        cache_path = LinkedInStrategy().cache_image(passing_data)
        assert type(cache_path) is str

    def test_cache_image_exists(self, test_data) -> None:
        """Test -- file should exist at cache path."""
        passing_data, _ = test_data
        cache_path = LinkedInStrategy().cache_image(passing_data)
        assert os.path.isfile(cache_path)

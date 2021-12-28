"""
Unit tests for platform strategies.
"""
from api.refactored.strategies.platform_strategy import LinkedInStrategy
import os


class TestLinkedinStrategy:
    ### Tests for method: find_image() ###
    def test_find_image(self, test_data):
        image_data = LinkedInStrategy().find_image(test_data)
        assert "li" or "linkedin" in image_data["filename"]

    ### Tests for method: cache_image() ###
    def test_cache_image(self, test_data):
        """
        Cache path should be of type string.
        File should exist at cache path.
        File should have a valid image extension (jpg or png)
        """
        cache_path = LinkedInStrategy().cache_image(test_data)
        assert os.path.isfile(cache_path)
        assert type(cache_path) is str

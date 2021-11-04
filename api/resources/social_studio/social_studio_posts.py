from flask import request
from flask_restful import Resource
from api.scrapers.ss_scraper import SSScraper


class SocialStudioPosts(Resource):
    def get(self):
        args = request.args

        s = SSScraper()
        s.open_chrome()
        s.login()
        response = s.fetch_posts(**args)
        s.close_browser()

        return response

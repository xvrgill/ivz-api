import pytest
from api import app

# Test client used for functional tests
@pytest.fixture
def client():
    with app.test_client() as client:
        return client


@pytest.fixture(scope="class")
def test_data():
    """
    Dummy deserialized data for use in testing platform specific strategies.

    Module path: api/refactored/strategies/platform_strategy.py
    """
    # Data contains all proper key value pairs. Should pass tests as is.
    passing_post_data = {
        "_id": "12893468fjdi9283",
        "air_table_id": "kdjfao3290",
        "name": "Test Post Data",
        "images": [
            {
                "id": "attLTAwdLbKQguEU4",
                "width": 506,
                "height": 286,
                "url": "https://dl.airtable.com/.attachments/d0f93c09ebd0dfeb68dfbad5ba3925a5/8c2697f7/li-idi0519ff.png",
                "filename": "li-idi0519ff.png",
                "size": 272741,
                "type": "image/png",
                "thumbnails": {
                    "small": {"url": "https://dl.airtable.com/.attachmentThumbnails/dc750ce17555717b6624ad16d94351e3/8af1c4db", "width": 64, "height": 36},
                    "large": {"url": "https://dl.airtable.com/.attachmentThumbnails/54a3a03f2fc4355e7c31cab06e8579e7/636ad1c0", "width": 506, "height": 286},
                    "full": {"url": "https://dl.airtable.com/.attachmentThumbnails/4df84e6cb79ff52b8b5dc46ab8f68901/519bb2b0", "width": 3000, "height": 3000},
                },
            }
        ],
        "status": ["Ready for Social", "Live on Web"],
        "us_web_lauch_date": "2014-09-05",
        "social_date_1": "2021-05-21",
        "social_channel": ["Facebook", "Twitter", "Instagram", "Hearsay"],
    }

    # Data contains no reference to linkedin in filename and incorrect type for image width. Should raise value error.
    failing_post_data = {
        "_id": "12893468fjdi9283",
        "air_table_id": "kdjfao3290",
        "name": "Test Post Data",
        "images": [
            {
                "id": "attLTAwdLbKQguEU4",
                "width": "506",
                "height": 286,
                "url": "https://dl.airtable.com/.attachments/d0f93c09ebd0dfeb68dfbad5ba3925a5/8c2697f7/li-idi0519ff.png",
                "filename": "idi0519ff.png",
                "size": 272741,
                "type": "image/png",
                "thumbnails": {
                    "small": {"url": "https://dl.airtable.com/.attachmentThumbnails/dc750ce17555717b6624ad16d94351e3/8af1c4db", "width": 64, "height": 36},
                    "large": {"url": "https://dl.airtable.com/.attachmentThumbnails/54a3a03f2fc4355e7c31cab06e8579e7/636ad1c0", "width": 506, "height": 286},
                    "full": {"url": "https://dl.airtable.com/.attachmentThumbnails/4df84e6cb79ff52b8b5dc46ab8f68901/519bb2b0", "width": 3000, "height": 3000},
                },
            }
        ],
        "status": ["Ready for Social", "Live on Web"],
        "us_web_lauch_date": "2014-09-05",
        "social_date_1": "2021-05-21",
        "social_channel": ["Facebook", "Twitter", "Instagram", "Hearsay"],
    }

    return passing_post_data, failing_post_data


# TODO: Implement the data below as required for testing by adding it to post data dictionary
# "content_author": []
# social_campaign = []
# live_urls: ""
# satus_update: ""
# tweet_copy: "This is some twitter specific test copy"
# paid_copy = ""
# linkedin_facebook_copy = "LI Copy: This is some linkedin copy\n\nFB Copy: "
# article_copy = fields.List(fields.Dict, data_key="Article copy")
# us_web_compliance_log_number = fields.Str(data_key="US Web: Compliance log #")
# programs_and_themes = fields.List(fields.Str, data_key="Programs & Themes")
# web_role = fields.List(fields.Str, data_key="Web: Role")
# web_date_of_last_use = fields.String(data_key="Web: Date of last use")
# email_trigger = fields.Bool(data_key="Need email trigger?")
# linkedin_thought_leader = fields.List(fields.Str, data_key="LinkedIn Thought Leader")
# editorial_rep = fields.List(fields.Str, data_key="Editorial rep")
# social_team = fields.List(fields.Str, data_key="Social Team")
# web_topic_tag = fields.List(fields.Str, data_key="Web: Topic Tag")
# ca_web_launch = fields.Str(data_key="CA Web launch")
# planning = fields.List(fields.Str, data_key="Planning")
# where_to_post = fields.List(fields.Str, data_key="Where to post")
# editorial_process_steps = fields.Str(data_key="Editorial process steps")
# ca_web_compliance_log = fields.Str(data_key="CA Web: Compliance log")
# see_associated_record = fields.List(fields.Str, data_key="See associated record")
# social_brand = fields.List(fields.Str, data_key="Social: Brand")
# soocial_review_queue = fields.String(data_key="Social review queue")
# ca_web_fr_translation_publish_date = fields.Str(data_key="CA Web: Fr translation publish date")
# link_to_qqq_images = fields.List(fields.Str, data_key="Link to QQQ Images")
# social_canada_copy = fields.Str(data_key="Social: Canada copy")
# qqq_content_partner = fields.Str(data_key="QQQ: Content Partner")
# instagram_copy = fields.Str(data_key="Instagram Copy")
# social_initiative = fields.Str(data_key="Social: Initiative")
# create_socialstudio_post_button = fields.Dict(
#     keys=fields.Str(), values=fields.Str(), data_key="Create Social Studio Post(s)"
# )

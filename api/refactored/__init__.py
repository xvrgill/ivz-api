"""
Contains refactored code using the strategy pattern. Simplified code base that is more readable.
Additionally, this makes the code extensible. New functionality can be added as required.
Refactored code accepts http requests directly from Air Table that pass in the post's Air Table ID.
The ID is then used to acquire the JSON formatted Air Table data by pulling it directly from the Air Table API.
Data is then processed and passed to a web scraper which creates the post in social studio.
"""

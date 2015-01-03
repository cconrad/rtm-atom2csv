Usage
=====

* ```pip install scrapy```
* Get atom feed URL from RTM website
* Replace the placeholder URL in rtm/spiders/__init__.py
* Run from the root directory to create CSV file:

     scrapy crawl rtm -o /path/to/export.csv

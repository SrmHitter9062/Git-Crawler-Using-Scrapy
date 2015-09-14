# -*- coding: utf-8 -*-

# Scrapy settings for GitCrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'GitCrawler'

SPIDER_MODULES = ['GitCrawler.spiders']
NEWSPIDER_MODULE = 'GitCrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'GitCrawler (+http://www.yourdomain.com)'

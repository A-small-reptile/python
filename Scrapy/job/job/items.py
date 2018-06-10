# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    jobweal=scrapy.Field()
    jobtag=scrapy.Field()
    jobmsg=scrapy.Field()
    jobrequired=scrapy.Field()
    jobplace=scrapy.Field()
    jobsalary=scrapy.Field()
    comparyname=scrapy.Field()
    comparyattr=scrapy.Field()
    jobname=scrapy.Field()
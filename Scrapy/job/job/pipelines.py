# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from job.models import create_session
from job.models.job_msg import JobMsg
import MySQLdb
from scrapy import log
from job.models import Base,engine

class JobPipeline(object):
    def __init__(self):
        self.session=create_session()
        self.table=Base.metadata.create_all(engine)
    def process_item(self, item, spider):
        if item:
            job_required = self.str_handler(item['jobrequired'])
            item['jobrequired'] = ','.join(job_required).replace(' ','')
            job=JobMsg(
                jobname=item['jobname'],
                jobsalary=item['jobsalary'],
                jobplace=item['jobplace'],
                comparyname=item['comparyname'],
                comparyattr=item['comparyattr'],
                jobtag=item['jobtag'],
                jobweal=item['jobweal'],
                jobrequired=item['jobrequired'],
            )
            try:
                self.session.add(job)
                self.session.commit()
            except MySQLdb.IntegrityError as e:
                log.msg("MySQL Error: %s" % str(e))
        else:
            log.msg("item is invalid!")
    def close_spider(self):
        self.session.close()

    # 数据清洗
    def str_handler(self, msg):
        pan = 1
        while pan:
            if msg:
                if '\r' in msg[-1]:
                    msg.pop()
                else:
                    pan = 0
                    return msg
            else:
                pan=0
                return msg

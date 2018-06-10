import scrapy
from job.items import JobItem
import re
import time

class JobSpider(scrapy.Spider):

    name='jobspider'
    allowed_domains = ["51job.com"]
    start_urls=["https://search.51job.com/list/040000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=4&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="]
    count2=0
    count1 = 0
    count3=0
    def parse(self, response):
        self.logger.info('访问的初始网页是 %s'%response.url)
        job_page = int(response.xpath('//div[@class="dw_page"]//span[@class="td"]').re('共(\w+)页')[0])
        self.logger.info('获取的页面数%s' % job_page)
        base_url = "https://search.51job.com/list/040000,000000,0000,00,9,99,python,2,{0}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
        for i in range(1,job_page+1):
            url = base_url.format(i)
            self.logger.info('获取第%s页'%i)
            yield scrapy.http.Request(url, callback=self.parse_02)
    #实现翻页并获取当前网页中的每个招聘页面
    def parse_02(self,response):
        job_url = response.xpath('//div[@class="el"]/p//@href').extract()
        for url in job_url:
            self.count1 += 1
            self.logger.info("访问具体的页面次数%s"%self.count1)
            time.sleep(3)
            yield scrapy.http.Request(url,callback=self.parse_03,dont_filter=True)
    # 数据索引
    def parse_03(self,response):
        item = JobItem()
        self.count3+=1
        self.logger.info('开始解析页面次数%s' % self.count3)
        regex=re.compile("[^\t\n\r\xa0 |']+")
        job_tag=response.xpath('//div[@class="tHeader tHjob"]')
        item['jobname']=job_tag.xpath('//div[@class="tHeader tHjob"]//h1/text()').extract()[0]
        item['jobplace']=job_tag.xpath('//div[@class="tHeader tHjob"]//span/text()').extract()[0]
        item['jobsalary']=job_tag.xpath('//div[@class="tHeader tHjob"]//strong/text()').extract()[0]
        item['comparyname']=job_tag.xpath('//div[@class="tHeader tHjob"]//p//a//@title').extract()[0]
        str_compary=job_tag.xpath('//div[@class="tHeader tHjob"]//p[@class="msg ltype"]/text()').extract()[0]
        item['comparyattr']=','.join(regex.findall(str_compary))
        compary_required=response.xpath('//div[@class="tCompany_main"]')
        item['jobtag']=','.join(compary_required.xpath('//div[@class="tCompany_main"]//div[@class="t1"]//span/text()').extract())
        item['jobweal']=','.join(compary_required.xpath('//div[@class="tCompany_main"]//p[@class="t2"]//span/text()').extract())
        item['jobrequired']=compary_required.xpath('//div[@class="tCompany_main"]//div[@class="bmsg job_msg inbox"]//p/text()').extract()
        self.count2 += 1
        self.logger.info('解析页面次数%s' % self.count2)
        return item





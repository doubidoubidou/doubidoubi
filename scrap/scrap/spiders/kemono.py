import scrapy

class Kemonospider(scrapy.Spider):
    name = 'kemono'
    allowed_domains = ['kemono.su']
    start_urls = ['https://kemono.su/fanbox/user/49494721']  # 作者页面

    def start_requests(self):  # 控制爬虫发出的第一个请求
        proxy = "http://127.0.0.1:7890"
        yield scrapy.Request(self.start_urls[0], meta={"proxy": proxy})

    def parse(self, response):
        # 获取每个文章的地址
        websitelist = []
        articles=response.xpath('/html/body/div[2]/main/section/div[3]/div[2]/article')
        for article in articles:
            website_noprefix=article.xpath('./a/@href').extract_first()
            website='https://kemono.su/'+website_noprefix
            websitelist.append(website)

        # 访问每篇文章
        for website in websitelist:
            yield scrapy.Request(url=website, callback=self.parse_webpage)

        # 获取页数
        webnumlist_element=response.xpath('/html/body/div[2]/main/section/div[5]/menu/a')
        webnumlist=[]
        for webnum_element in webnumlist_element:
            num=webnum_element.xpath('./b/text()').extract_first()
            webnumlist.append(num)
        total_webnum=webnumlist[-3]

        # 访问下一页
        page_numbers = [50*i for i in range(1,int(total_webnum))]
        for page_number in page_numbers:
            next_page_url = f'{self.start_urls[0]}?o={page_number}'
            yield scrapy.Request(url=next_page_url, callback=self.parse)


    def parse_webpage(self, response):
        pass


        #     filewebsite=response.xpath('/html/body/div[2]/main/section/div/ul[2]/li/a/@href').extract_first()
            # with open(r'C:\Users\GMH\Desktop\peachpie.csv','a') as f:
            #     f.write(f'{filename},{filewebsite}\n')


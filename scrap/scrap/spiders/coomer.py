import scrapy


class Coomerpider(scrapy.Spider):
    name = 'coomer'
    allowed_domains = ['coomer.su']
    start_urls = ['https://coomer.su/onlyfans/user/yui_peachpie']

    def start_requests(self):  # 控制爬虫发出的第一个请求
        proxy = "http://127.0.0.1:7890"
        yield scrapy.Request(self.start_urls[0], meta={"proxy": proxy})

    def parse(self, response):
        weblist=[]
        names=response.xpath('/html/body/div[2]/main/section/div[3]/div[2]/article')
        for name in names:
            data=name.xpath('./a/@href').extract_first()
            new_data='https://coomer.su'+data
            weblist.append(new_data)

        for url in weblist:
            yield scrapy.Request(url=url, callback=self.parse_webpage)

        base_url = 'https://coomer.su/onlyfans/user/yui_peachpie'
        page_numbers = [50, 100, 150,200,250]  # 不同页码
        for page_number in page_numbers:
            next_page_url = f'{base_url}?o={page_number}'

            # 发送下一页的请求
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_webpage(self, response):
        filename=response.xpath('/html/body/div[2]/main/section/div/ul[2]/li/a/text()').extract_first()
        if filename!=None:
            filename=filename.strip()
            filewebsite=response.xpath('/html/body/div[2]/main/section/div/ul[2]/li/a/@href').extract_first()
            with open(r'C:\Users\GMH\Desktop\peachpie.csv','a') as f:
                f.write(f'{filename},{filewebsite}\n')


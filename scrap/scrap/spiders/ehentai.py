import scrapy

class EhentaiSpider(scrapy.Spider):
    name = 'ehentai'
    allowed_domains = ['hentai']
    start_urls = ['https://e-hentai.org/']

    def start_requests(self):  # 控制爬虫发出的第一个请求
        proxy = "http://127.0.0.1:7897"
        header={
            "authority":"e-hentai.org",
            "method":"GET",
            "scheme":"https",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-HK;q=0.5",
            "Cache-Control": "no-cache",
            "Host":"https://e-hentai.org/",
            "Cookie": "ipb_member_id=3180327; ipb_pass_hash=212d8c2234a54de1e31b549c98544509; igneous=mo61cubem5g4q91av6z;",
            "Pragma": "no-cache",
            "Referer": "https://e-hentai.org/",
            "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
        }
        yield scrapy.Request(self.start_urls[0], meta={"proxy": proxy,"header":header})

    def parse(self, response,**kwargs):
        print(response.text)



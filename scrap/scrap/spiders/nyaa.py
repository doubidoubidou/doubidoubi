import os
import scrapy

key = '短发'


class NyaaSpider(scrapy.Spider):
    name = 'nyaa'
    allowed_domains = ['sukebei.nyaa.si']
    if key:
        start_url = f'https://sukebei.nyaa.si/?f=0&c=2_0&q={key}'
    else:
        start_url = f'https://sukebei.nyaa.si/?f=0&c=2_0'
    proxy = "http://127.0.0.1:7897"
    header = {
        "authority": "sukebei.nyaa.si",
        "method": "GET",
        "scheme": "https",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-HK;q=0.5",
        "Cache-Control": "no-cache",
        "Host": "https://sukebei.nyaa.si/",
        "Cookie": "__ddg1_=aYLLwj98HLcydGa2SUfS; __ddgid_=dBdor89uje4ZKpOB; zone-closed-5208064=true",
        "Pragma": "no-cache",
        "Referer": "https://sukebei.nyaa.si/",
        "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
    }

    def start_requests(self):
        yield scrapy.Request(self.start_url, meta={"proxy": self.proxy, "header": self.header},
                             callback=self.get_pagenum)

    def get_pagenum(self, response):
        pagenum = response.xpath('/html/body/div[1]/div[3]/ul/li[position()=last()-1]/a/text()').extract_first()
        if pagenum is None:
            pagenum = 1
        for i in range(1, int(pagenum) + 1):
            url = self.start_url + f'&p={i}'
            yield scrapy.Request(url, meta={"proxy": self.proxy, "header": self.header}, callback=self.parse)

    def parse(self, response, **kwargs):
        tr_elements = response.xpath('/html/body/div/div[2]/table/tbody/tr')
        datalist=[]
        if not tr_elements:
            datalist.append([key,'未查询到关键词数据！','无链接'])
        else:
            for tr_element in tr_elements:
                title = tr_element.xpath('./td[2]/a/text()').extract_first()
                magnet = tr_element.xpath('./td[3]/a[2]/@href').extract_first()
                datalist.append([key,title,magnet])
        desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
        with open(os.path.join(desktop_path,f'{key}.csv'),'a',encoding='utf-8') as f:
            for data in datalist:
                data=','.join(data)+'\n'
                f.write(data)

import scrapy


class Dividends3mSpider(scrapy.Spider):
    name = 'dividends_3M'
    allowed_domains = ['https://investors.3m.com/stock-information/dividends/default.aspx']
    start_urls = ['https://investors.3m.com/stock-information/dividends/default.aspx']

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            # 'dividendValues.middlewares.RotateProxyMiddleware': 300,
            # 'dividendValues.middlewares.RotateAgentMiddleware': 301,
            'dividendValues.middlewares.SeleniumMiddleware': 302,
            # 'dividendValues.middlewares.NasdaqMiddleware': 303,
        }
    }

    def start_requests(self):
        urls = [
            'https://investors.3m.com/stock-information/dividends/default.aspx',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        tableData = response.xpath('//table//tbody/tr')
        header1 = response.xpath('//table/thead/tr/th[1]/text()')[0].extract()
        header2 = response.xpath('//table/thead/tr/th[2]/text()')[0].extract()
        header3 = response.xpath('//table/thead/tr/th[3]/text()')[0].extract()
        header4 = response.xpath('//table/thead/tr/th[4]/text()')[0].extract()
        header5 = response.xpath('//table/thead/tr/th[5]/text()')[0].extract()

        for rows in tableData:
            textField = rows.xpath('td[1]//text()')[0].extract()

            if "Total" in textField.strip() or len(textField.strip()) == 0:
                break
            # print (rows.xp÷ath('td[1]//text()')[0].extract())
            yield {
                header1 : rows.xpath('td[1]//text()')[0].extract(),
                header2 : rows.xpath('td[2]//text()')[0].extract(),
                header3 : rows.xpath('td[3]//text()')[0].extract(),
                header4 : rows.xpath('td[4]//text()')[0].extract(),
                header5 : rows.xpath('td[5]//text()')[0].extract(),
            }
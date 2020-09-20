import scrapy


class PepsicodividendSpider(scrapy.Spider):
    name = 'pepsicoDividend'
    allowed_domains = ['https://www.dividendmax.com/united-states/nasdaq/beverages/pepsico-inc/dividends']
    start_urls = ['https://www.dividendmax.com/united-states/nasdaq/beverages/pepsico-inc/dividends/']

    def start_requests(self):
        urls = [
            'https://www.dividendmax.com/united-states/nasdaq/beverages/pepsico-inc/dividends/',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        tableData = response.xpath('//div[@class="dividends-table"]//table[@class="dividends"]//tbody/tr')
        header1 = response.xpath('//div[@class="dividends-table"]//table[@class="dividends"]/thead/tr/th[1]//text()')[0].extract()
        header2 = response.xpath('//div[@class="dividends-table"]//table[@class="dividends"]/thead/tr/th[2]//text()')[0].extract()
        header3 = response.xpath('//div[@class="dividends-table"]//table[@class="dividends"]/thead/tr/th[3]//text()')[0].extract()
        header4 = response.xpath('//div[@class="dividends-table"]//table[@class="dividends"]/thead/tr/th[4]//text()')[0].extract()
        header5 = response.xpath('//div[@class="dividends-table"]//table[@class="dividends"]/thead/tr/th[5]//text()')[0].extract()
        header6 = response.xpath('//div[@class="dividends-table"]//table[@class="dividends"]/thead/tr/th[6]//text()')[0].extract()

        for rows in tableData:
            if "Sign" in rows.xpath('td[4]//text()')[0].extract():
                break
            yield {
                header1 : rows.xpath('td[1]//text()')[0].extract(),
                header2 : rows.xpath('td[2]//text()')[0].extract(),
                header3 : rows.xpath('td[3]//text()')[0].extract(),
                header4 : rows.xpath('td[4]//text()')[0].extract(),
                header5 : rows.xpath('td[5]//text()')[0].extract(),
                header6 : rows.xpath('td[6]//text()')[0].extract(),
            }

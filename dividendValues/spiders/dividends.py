import scrapy


class DividendsSpider(scrapy.Spider):
    name = 'dividends'
    allowed_domains = ['http://www.investors.ups.com/financials/dividend-history']
    start_urls = ['http://www.investors.ups.com/financials/dividend-history/']

    def start_requests(self):
        urls = [
            'http://www.investors.ups.com/financials/dividend-history/',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        tableData = response.xpath('//table//tbody/tr')
        header1 = response.xpath('//table//thead/tr/th[1]//text()')[0].extract()
        header2 = response.xpath('//table//thead/tr/th[2]//text()')[0].extract()
        header3 = response.xpath('//table//thead/tr/th[3]//text()')[0].extract()
        header4 = response.xpath('//table//thead/tr/th[4]//text()')[0].extract()
        header5 = response.xpath('//table//thead/tr/th[5]//text()')[0].extract()
        header6 = response.xpath('//table//thead/tr/th[6]//text()')[0].extract()
        
        for rows in tableData:
            textField = rows.xpath('td[1]//text()')[0].extract()
            if "Total" in textField:
                continue
            yield {
                header1 : rows.xpath('td[1]//text()')[0].extract(),
                header2 : rows.xpath('td[2]//text()')[0].extract(),
                header3 : rows.xpath('td[3]//text()')[0].extract(),
                header4 : rows.xpath('td[4]//text()')[0].extract(),
                header5 : rows.xpath('td[5]//text()')[0].extract(),
                header6 : rows.xpath('td[6]//text()')[0].extract(),
            }
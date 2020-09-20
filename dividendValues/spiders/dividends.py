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
        for rows in tableData:
            textField = rows.xpath('td[1]//text()')[0].extract()
            print (textField)
            if "Total" in textField:
                continue
            yield {
                'Declared' : rows.xpath('td[1]//text()')[0].extract(),
                'Ex-Date' : rows.xpath('td[2]//text()')[0].extract(),
                'Record' : rows.xpath('td[3]//text()')[0].extract(),
                'Payale' : rows.xpath('td[4]//text()')[0].extract(),
                'Amount' : rows.xpath('td[5]//text()')[0].extract(),
                'Type' : rows.xpath('td[6]//text()')[0].extract(),
            }
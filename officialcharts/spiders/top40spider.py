import scrapy
from officialcharts.items import OfficialchartsItem


class Top40Spider(scrapy.Spider):
    """docstring for Top40Spider"""
    name = "Top40Singles"

    start_urls = [
        "http://www.officialcharts.com/charts/uk-top-40-singles-chart/"
    ]

    def parse(self, response):
        for i, x in enumerate(response.xpath(
                "//html/body/div/div/article/div/div/section/table/tr")):
            # The 1st <tr> is the header
            # The items are 5 <tr>'s apart
            # For each 30 items add a <tr> e.g. (30 * 5 + 1)
            if (i % 151) % 5 == 2:
                item = OfficialchartsItem()

                data = [x.xpath("//tr[{}]/td[3]/div/div/div/a/text()".format(i))
                        .extract()][0]
                item['pos'] = x.xpath("//tr[{}]/td[1]/span/text()".format(i))\
                    .extract()[0]
                item['artist'] = data[1]
                item['title'] = data[0]

                yield item
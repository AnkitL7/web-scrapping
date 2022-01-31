import scrapy

def check(tex):
    if tex == "Out of Stock":
        return False
    else:
        return True

class TaskSpider(scrapy.Spider):
    name = "details"
    start_urls = ['https://www.midsouthshooterssupply.com/dept/reloading/primers?itemsperpage=30&currentpage=1']

    def parse(self, response):
        # page = response.url.split('=')[-1]
        # filename = f'details-{page}.html'
        # with open(filename,'wb') as f:
        #     f.write(response.body)

        for detail in response.css('div.product'):
            yield{
                'price' : detail.css('.price span::text')[0].get(),
                'title' : detail.css('.product-description a::text')[0].get(),
                'stock' : check(detail.css('.status span::text')[0].get()),
                'maftr' : detail.css('.catalog-item-brand::text')[0].get()
            }
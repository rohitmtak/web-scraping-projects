import scrapy


class SpecDetailsSpider(scrapy.Spider):
    name = "spec_details"
    allowed_domains = ["www.glassesshop.com"]
    start_urls = ["https://www.glassesshop.com/bestsellers"]

    def parse(self, response):
        spec_details = response.xpath("//div[@id='product-lists']/div")
        for product in spec_details:
            yield{
                
                'url' : product.xpath(".//descendant::div[@class='product-img-outer']/a/@href").get(),
                'img_url' : product.xpath(".//img[@class='lazy d-block w-100 product-img-default']/@src").get(),
                'price' : product.xpath(".//div[@class='p-price']//span/text()").get(),
                'name' : product.xpath("normalize-space(.//descendant::div[@class='p-title']/a/text())").get()
               
            }

        next_page = response.xpath("//ul[@class='pagination']/li[position() = last()]/a/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
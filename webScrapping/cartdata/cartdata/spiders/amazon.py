import scrapy

from ..items import CartdataItem

class amazon(scrapy.Spider):
    name="app"
    page_index = 1
    start_urls = [
        "https://www.amazon.in/s?i=grocery&srs=14419476031&dc&qid=1602946072&ref=sr_pg_1"
    ]


    def parse(self,response):
        items = CartdataItem()

        divs = response.css(".s-latency-cf-section")


        for prod in divs:
            if(prod is not None):
                product_name = prod.css(".a-color-base.a-text-normal::text").extract()
                product_price = prod.css(".a-price-whole::text").extract()
                product_review_count = prod.css(".a-size-small .a-size-base::text").extract()
                product_rating = prod.css(".aok-align-bottom .a-icon-alt::text").extract()
                # is_best_seller = prod.css(".a-badge-text::text").extract()

                items["product_rating"] = (product_rating[0]).replace(" out of 5 stars","") if (product_rating and len(product_rating)>0) else product_rating 
                items["product_name"] =  product_name[0] if (product_name and len(product_name)>0) else product_name
                items["product_price"] = product_price[0] if(product_price and len(product_price)>0) else product_price
                items["product_review_count"] = product_review_count[0] if(product_review_count and len(product_review_count)>0) else product_review_count

                # items["product_rating"] = product_rating[0] if len(product_rating) >0 else product_rating
            
                # items["is_best_seller"] = is_best_seller
                yield  items

        self.page_index +=1
        next_page =  "https://www.amazon.in/s?i=grocery&dc&page="+str(self.page_index)
        print(self.page_index)
        print("Current Page Index before search.")
        if(self.page_index <5):
            yield response.follow(next_page,callback=self.parse)
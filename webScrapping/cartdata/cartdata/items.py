# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CartdataItem(scrapy.Item):

    # define the fields for your item here like:
    product_name = scrapy.Field()   #.
    product_price = scrapy.Field()  #.a-price-whole
    product_review_count = scrapy.Field()  #.a-size-small .a-size-base
    product_rating = scrapy.Field() #.aok-align-bottom
    # is_best_seller = scrapy.Field() # .a-badge-text


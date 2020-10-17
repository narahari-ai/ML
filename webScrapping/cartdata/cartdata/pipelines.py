# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class CartdataPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()


    def create_connection(self):
        self.conn = sqlite3.connect("AllProducts.db")
        self.curr = self.conn.cursor()


    def create_table(self):
        self.curr.execute(""" DROP TABLE IF EXISTS groceries_tbl""")
        self.curr.execute(""" create table groceries_tbl(
                        Name text,
                        Cost text,
                        Rating text,
                        reviews_count text)""")

    def process_item(self, item, spider):
        print("Pipe line: "+ item["product_name"])
        self.store_item_db(item)
        return item

    def store_item_db(self,itm):
        self.curr.execute(""" insert into groceries_tbl values (?,?,?,?)
        """,( itm["product_name"],itm["product_price"],itm["product_rating"],itm["product_review_count"]))
        self.conn.commit()

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class QuotetutorialPipeline(object):
    def __init__(self):
        self.create_conn()
        self.create_table()

    def create_conn(self):
        self.conn = sqlite3.connect("quo.db")
        self.cur=self.conn.cursor()

    def create_table(self):
        self.cur.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.cur.execute("""create table quotes_tb(
               title text,
               author text,
               tag text)""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.cur.execute("""insert into quotes_tb values (?,?,?)""",(
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.conn.commit()

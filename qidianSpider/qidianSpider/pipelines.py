# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
import logging
import pymysql
from datetime import datetime
logger = logging.getLogger(__name__)


# 保存到mongodb中
class BookspiderPipeline(object):
    def open_spider(self, spider):
        MONGO_HOST = spider.settings.get("MONGO_HOST")
        client = MongoClient(MONGO_HOST)
        self.collection = client.test.book

    def process_item(self, item, spider):
        logger.warning(item)
        self.collection.update({'url': item['url']}, {'$set': item}, True)
        return item

    def close_spider(self, spider):
        print("完成")

# 保存到mysql中


class MYsqlBookspiderPipeline(object):
    def open_spider(self, spider):
        host = spider.settings.get("MYSQL_HOST")
        port = spider.settings.get("MYSQL_PORT")
        user = spider.settings.get("MYSQL_USERNAME")
        passwd = spider.settings.get("MYSQL_PASSWORD")
        db = spider.settings.get("MYSQL_DATABASE")
        self.conn = pymysql.Connect(
            host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8'
        )

        self.cursor = self.conn.cursor()
        self.conn.autocommit(True)

    def process_item(self, item, spider):
        title = item['title']
        url = item['url']
        imgurl = item['imgurl']
        category = item['category']
        author = (item['author'])
        content = (item['content'])

        if self.cursor.execute("select * from books where url = '{}'".format(url)) == 0:
            print("*"*100)

            self.cursor.execute("insert into books (title,url,author,imgurl,category,content) values ('{}','{}','{}','{}','{}','{}')".format(
                title, url, author, imgurl, category, content))
            # self.cursor.execute("insert into bookview_bookmodel2(bookID,bookName,) values ({},'{}')".format(
            #     bookID, bookName))

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

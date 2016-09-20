# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb

class CrawlerPipeline(object):
    def process_item(self, item, spider):

        mysql_con = spider.settings.get('MYSQL_CONNECT')
        con = MySQLdb.connect(**mysql_con)
        cur = con.cursor()
        sql = ("insert into dy_proxy(ip,port,http_type,position,speed,connect_time,check_time) values(%s,%s,%s,%s,%s,%s,%s)")
        item_list = (item['ip'],item['port'],item['http_type'],item['position'],item['speed'],item['connect_time'], item['check_time'])
        try:
            cur.execute(sql,item_list)
        except Exception,e:
            print "Insert error:",e
            con.rollback()
        else:
            con.commit()
        cur.close()
        con.close()
        return item

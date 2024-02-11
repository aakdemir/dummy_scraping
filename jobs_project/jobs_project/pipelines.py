# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from query import fetch_data_from_table, insert_data_into_table


class JobsProjectPipeline:
    def __init__(self):
        ## Connection Details
        hostname = 'localhost'
        username = 'jobFinder'
        password = 'jobFinder123' # your password
        database = 'postgres'

        ## Create/Connect to database
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        
        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()
    

    def process_item(self, item, spider):
        insert_data_into_table(self, item)
        fetch_data_from_table(self)
        ## Execute insert of data into database
        self.connection.commit()
        return item

    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.connection.close()
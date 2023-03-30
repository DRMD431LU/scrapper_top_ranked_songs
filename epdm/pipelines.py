# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy import create_engine
from .schema import create_db, create_session, Song

class EpdmPipeline:
    def __init__(self):
        self.create_database()
        self.create_connection()

    def process_item(self, item, spider):
        self.store_item_into_db(item)
        return item

    def create_database(self):
        create_db()

    def create_connection(self):
        self.connection = create_session()

    def store_item_into_db(self, item):
        new_song = Song(
                        key_id=item['key'],
                        title=item['name'],
                        author=item['author'],
                        position=item['position'])
        self.connection.add(new_song)
        self.connection.commit()

from data_processing import ContentExtractor
from repository.connect import Connection
import logging as logger

class Scraper:

    def __init__(self):
        self.content_processor = ContentExtractor()

    def start(self):
        try:
            self.conn = Connection('main', 'quavertrail', '1234', 'localhost', '5432')
            self.cursor = self.conn.begin()
        except:
            logger.error('Unable to connect to database')
        self.run()


    def run(self):
        sources = self.load_sources()

        for source in sources:
            logger.info('Extracting content from ' + source[1])
            articles = self.content_processor.extract_urls(source[1], source[2])
            self.content_processor.process_articles(articles)
        logger.info('Processing of sources complete')

    def load_sources(self):
        self.cursor.execute('SELECT * FROM sources;')
        return self.cursor.fetchall()








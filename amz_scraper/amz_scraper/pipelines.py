# useful for handling different item types with a single interface
import os

from itemadapter import ItemAdapter
from dotenv import load_dotenv
import psycopg2

load_dotenv()


class AmzScraperPipeline:
    def __init__(self):
        ## Connection Details
        hostname = os.environ.get('hostname')
        username = os.environ.get('username')
        password = os.environ.get('password')  # your password
        database = os.environ.get('database')

        ## Create/Connect to database
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()

        ## Create data table if none exists

    def process_item(self, item, spider):
        return item

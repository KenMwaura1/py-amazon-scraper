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
        port = os.environ.get('port')
        username = os.environ.get('username')
        password = os.environ.get('password')  # your password
        database = os.environ.get('database')

        ## Create/Connect to database
        if database:
            self.connection = psycopg2.connect(host=hostname, port=port, user=username, password=password,
                                               dbname=database)
        else:
            self.connection = psycopg2.connect(host="localhost", port=5432, user="test", password="testpassword",
                                               dbname="amazon_data")

        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()

        ## Create data table if none exists
        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS amazon_data(
                    id serial PRIMARY KEY, 
                    name VARCHAR(255),
                    asin text,
                    price float,
                    discounted VARCHAR(50)
                )
                """)

    def process_item(self, item, spider):
        # Check to see if text is already in database
        self.cur.execute("select * from amazon_data where content = %s", (item['name'],))
        result =  1# self.cur.fetchone()

        # If it is in DB, create log message
        if result:
            spider.logger.warn("Item already in database: %s" % item['name'])

        # If text isn't in the DB, insert data
        else:
            # Define insert statement
            self.cur.execute("""insert into amazon_data (name, asin, price, discounted) values (%s, %s, %s, %s)""", (
                item["name"],
                item["asin"],
                item["price"],
                item["discounted"]

            ))
            # Execute insert of data into database
            self.connection.commit()

        return item

    def close_spider(self, spider):
        # Close cursor & connection to database
        self.cur.close()
        self.connection.close()

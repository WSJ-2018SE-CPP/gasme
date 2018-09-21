import pymysql
import datetime

class MySQLStorage:

    def __init__(self, password):
        """
        Intializes an object for storing data into the MySQL db

        Args:
          password: the password to the rds gas prices db
        """

        # db information
        self.host="gasme-db.cusrpulgblsj.us-west-1.rds.amazonaws.com"
        self.port=3306
        self.dbname='gasme'
        self.user='gasme'
        self.password=password

        # the sql statement to upload data
        self.sql = "INSERT INTO gas_prices (address, brand, lat, lon, price_1, price_2, price_3, last_update) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE brand=%s, lat=%s, lon=%s, price_1=%s, price_2=%s, price_3=%s, last_update=%s;"


    def store_data(self, data):
        """
        Stores the data into the mysql database.

        Args:
          data: a list of results per gas station
        """

        try:
            # generate connection
            conn = pymysql.connect(self.host, user=self.user, port=self.port, passwd=self.password, db=self.dbname)

            # for each result
            for res in data:

                # check the data is acceptable
                if not self._validate_data(res):
                    continue

                # execute the query
                with conn.cursor() as cursor:
                    cursor.execute(self.sql, self._format_data(res))

                # commit the query
                conn.commit()

        finally:
            conn.close()


    def _validate_data(self, data):
        """
        Tests if the data is acceptable to store.

        Args:
          data: the data

        Returns:
          True if the data is acceptable, false otherwise
        """

        if data['address'] is None:
            return False

        if data['brand'] is None:
            return False

        if data['lat'] is None:
            return False

        if data['lon'] is None:
            return False

        if data['price_1'] is None:
            return False

        return True


    def _format_data(self, data):
        """
        Formats one data entry properly for the sql query.

        Args:
          data: the single data entry to format
        """

        address = data['address']
        brand = data['brand']
        lat = data['lat']
        lon = data['lon']
        price_1 = data['price_1']
        price_2 = data['price_2']
        price_3 = data['price_3']
        last_update = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        price_1 = price_1.replace('$', '') if price_1 is not None else None
        price_2 = price_2.replace('$', '') if price_2 is not None else None
        price_3 = price_3.replace('$', '') if price_3 is not None else None

        return (address, brand, lat, lon, price_1, price_2, price_3, last_update, brand, lat, lon, price_1, price_2, price_3, last_update)


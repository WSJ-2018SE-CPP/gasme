"""
CSV storage medium

Date: 09/13/2018
"""

class CSVStorage:
    """
    Class for csv storage of data.
    """

    def __init__(self, fname, keys):
        """
        Initialize the storage class.

        Args:
          fname: the name of the file
          keys: the parameters keys for the data to store
        """

        # name of file to save
        self.fname = fname

        # format and sort the keys
        self.keys = keys
        self.keys.sort()


    def store(self, data):
        """
        Stores the data.

        Args:
          data: the data to store
        """

        # format the data for writing
        s = ''

        # for each row in the data
        for row in data:

            # do not store if the row is not valid
            if not self._verify_data(row):
                continue

            # new line
            s += '\n'

            # for each parameter
            for i in range(len(self.keys)):

                # add , if not first param
                if i > 0:
                    s += ','

                # get the entry
                e = row[self.keys[i]]

                # add entry
                s += '"%s"'%e if e is not None else '"None"'

        # open the file
        with open(self.fname, 'a') as f:

            # write the data
            f.write(s)


    def _verify_data(self, data):
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





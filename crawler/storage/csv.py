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
        self.keys = [i for i in keys]
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



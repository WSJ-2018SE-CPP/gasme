"""
Tests the Parser.

Date: 09/12/2018
"""

from parser import Parser
from glob import glob


def all_same(items):
    """
    Tests all of the items in the list are the same.

    Args:
      items: the items to test
    """
    return all(x == items[0] for x in items)


class Test:
    """
    Class for defining and executing the tests.
    """

    def __init__(self, data):
        """
        Initializes the testing object.

        Args:
          data: the gas station data as a list of tuples where:
            [0] -> the raw html block level data
            [1] -> a dictionary of parameters to values
        """

        self.data = data
        self.keys = self.data[0][1].keys()
        self.p = Parser()


    def execute(self):
        """
        Executes the tests.
        """

        # path equality testing
        print('Testing All Paths Equal For Parameter:')
        for param in self.keys:
            self.test_path_equal(param)


    def test_path_equal(self, param):
        """
        Tests the path to the data is the same for each block.

        Args:
          param: the parameter to search for
        """

        # resulting lists
        a = []

        # for each data block
        for i in range(len(self.data)):

            # get the path and add to the list
            a.append(self.p.get_path(block=self.data[i][0], text=self.data[i][1][param]))

        # test equality and print results
        if all_same(a):
            print('%s --> %s w/ path = %s' % (param, 'PASSED', str(a[0])))
        else:
            print('%s --> %s w/ paths = %s' % (param, 'FAILED', str(a)))


if __name__ == '__main__':

    # testing filenames
    fnames = glob('./test_data/*raw.txt')

    # data buffer
    data = [[] for _ in range(len(fnames))]

    # for each data parameter pair
    for i in range(len(fnames)):

        # read and append the raw data
        with open(fnames[i], 'r') as f:
            data[i].append(f.read())

        # read and append the parameter data
        with open(fnames[i].replace('raw', 'params'), 'r') as f:
            data[i].append(dict([l.strip().split('=') for l in f]))

    # create and execute test
    t = Test(data)
    t.execute()


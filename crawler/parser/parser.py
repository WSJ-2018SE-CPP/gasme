"""
Parser definition for extracting information from the already extracted html blocks.

Date: 09/12/2018
"""

class Node:
    """
    A Node for the Parser defining the structure of the html data block.
    """

    def __init__(self, children, value:str):
        """
        Initialize the node with children or a string value.
        """
        self.children = children
        self.value = value.replace('"', '') if value is not None else value


    def __str__(self):
        """
        To String method.
        """
        if self.children is None:
            return str(self.value)
        else:
            s = '['
            for c in self.children:
                s += str(c) + ','
            return (s if len(s) == 1 else s[:-1]) + ']'


class Parser:
    """
    Object to parse gas station information from url request.
    """

    def __init__(self):

        # known parameter locations within a block
        self.param_mapping = dict([
            ('address',[14,37,0,0,17,0]),
            ('brand',[14,11]),
            ('price_1',[14,86,0,0,0]),
            ('price_2',[14,86,0,1,0]),
            ('price_3',[14,86,0,2,0]),
            ('lat',[14,9,2]),
            ('lon',[14,9,3])
        ])


    def parse(self, html, gas_station, params):
        """
        Parse the html for gas station data.

        Args:
          html: the html page to parse
          gas_station: the gas station used in the criteria search
          params: a list of parameters to extract
        """

        # result buffer
        res = []

        # for each gas station information block
        for block in self._extract_blocks(html, gas_station):
            
            # parse the block and get the root node
            node = self._parse_block(block)

            # all data for the current block
            block_data = dict()

            # for each parameter of interest
            for param in params:

                # get the data and append to the block dictionary
                block_data[param] = self._search(root=node, path=self.param_mapping[param])

            # append the block data to the total result
            res.append(block_data)

        # return the result
        return res


    def _extract_blocks(self, html, gas_station):
        """
        Extract gas station information blocks from the raw html.

        Args:
          html: the raw html
          gas_station: the gas station
        """

        # array for the resulting blocks
        res = []

        # find the beginning of the first gas station block
        s = '\\"%s gas prices' % gas_station
        beg = html.find(s, 0)
        beg = html.find(s, beg+len(s))
        beg = html.find(s, beg+len(s))
        beg = html.find('[', beg+len(s))

        # extract the gas blocks
        while True:

            # if ] occurs before [, there are no more gas station blocks
            if html[beg:].find(']') < html[beg:].find('['):
                break

            # get the starting index of the block
            beg = html.find('[', beg)

            # counter, +1 for [ and -1 for ]. when x == 0, the block is complete.
            # x will always be incremented from the first character because
            # we have set beg to [. Therefore, we check complete after + or - x.
            x = 0

            # initialize the end of the block
            end = beg

            # for each character in the text starting at the beginning block character
            for c in html[beg:]:

                # increment x
                if c == '[':
                    x += 1

                # decrement x
                elif c == ']':
                    x -= 1

                # append block if closed
                if x == 0:
                    res.append(html[beg:end+1])
                    beg = end + 1
                    break

                # increment end
                end += 1

        # return the blocks
        return res


    def _parse_block(self, text):
        """
        Parse the block and return the root of the data structure.

        Args:
          text: the text block to parse
        """
        
        def parse_rec(node, text):
            """
            Recursive helper function.

            Args:
              node: the current node
              text: the text to parse
            """

            # trim outside [ and ]
            text = text[text.find('[')+1 : text.rfind(']')]

            # test if only one data entry
            if ',' not in text:
                node.children.append(Node(children=None, value=text))
                return node

            # start of data chunk
            beg = 0

            # level seperator counter
            x = 0

            # pause if text is in quotes
            pause = False

            # for each character
            for end in range(len(text)):

                if text[end] == '"':
                    # string value, pause until found closing quote
                    pause = not pause

                elif (text[end] == ',') and (x == 0) and not pause:
                    # found the end of a comma separated value
                    node.children.append(Node(children=None, value=text[beg:end]))
                    beg = end + 1

                elif text[end] == '[' and not pause:
                    # found [, beginning of new level, continue until ] is found
                    x += 1
                elif text[end] == ']' and not pause:
                    x -= 1
                    # found closing ], add new depth and continue search at new head
                    if x == 0:
                        node.children.append(parse_rec(Node(children=[], value=None), text=text[beg:end+1]))
                        beg = end + 1
                    elif x < 0:
                        raise Exception('Error, more ] than [ !!!')
        
            # append the last element
            if beg <= end:
                node.children.append(Node(children=None, value=text[beg:]))

            # return the result
            return node

        # clean the data of \", \n and ],
        text = text.replace('\\"', '"')
        text = text.replace('\\n', '')
        text = text.replace('],', ']')

        # parse the text recursively and return root
        return parse_rec(Node([], None), text)
        

    def get_path(self, block, text):
        """
        Returns a path to the data. Mostly used for testing purposes to find / define paths to relevant information

        Args:
          block: the text of the gas station block
          text: the exact text to find

        Returns:
          The path to the data
        """

        def get_path_rec(node, path):
            """
            Recursive helper function.

            Args:
              path: the current path
            """

            # check text equal if leaf node
            if node.children is None:
                return path if node.value == text else None

            # depth first search
            for i in range(len(node.children)):

                # append stop to the current path
                path.append(i)

                # continue search
                r = get_path_rec(node.children[i], path)

                # return path if not None
                if r is not None:
                    return r

                # pop route and try next
                path.pop()

            # no result found, return None
            return None

        # get the path
        path = get_path_rec(self._parse_block(block), [])

        # test a path exists        
        if path is None:
            raise Exception('Could not find %s !!!' % text)

        # return path
        return path

    
    def _search(self, root, path):
        """
        Get the data at a specified path.

        Args:
          root: the root to search
          path: the path

        Returns:
          The data at the path
        """

        try:
            # start at the root
            node = root

            # traverse the tree
            for d in path:
                node = node.children[d]

            # return result
            return node.value

        except:
            # error, return None
            return None



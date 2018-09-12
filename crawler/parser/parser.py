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
    Object to parse individual data blocks per gas station.
    """

    def __init__(self, text=None):
        """
        Initializes the parser, and parses if data is provided.

        Args:
          text: the text to parse
        """

        # parse if data present
        if text is not None:
            self._parse(text)

    
    def parse(self, text):
        """
        Parse the text and stores the resulting data structure.

        Args:
          text: the text to parse
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

        # parse the text recursively and set to the root
        self.root = parse_rec(Node([], None), text)
        

    def get_path(self, text):
        """
        Returns a path to the data. Mostly used for testing purposes to find / define paths to relevant information

        Args:
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
        path = get_path_rec(self.root, [])

        # test a path exists        
        if path is None:
            raise Exception('Could not find %s !!!' % text)

        # return path
        return path

    
    def search(self, path):
        """
        Get the data at a specified path.

        Args:
          path: the path

        Returns:
          The data at the path
        """

        try:
            # start at the root
            node = self.root

            # traverse the tree
            for d in path:
                node = node.children[d]

            # return result
            return node.value

        except:
            # error, return None
            return None



class Node:
    def __init__(self, children, value:str):
        self.children = children
        self.value = value.replace('"', '') if value is not None else value

    def __str__(self):
        if self.children is None:
            return str(self.value)
        else:
            s = '['
            for c in self.children:
                s += str(c) + ','
            return (s if len(s) == 1 else s[:-1]) + ']'


class Parser:

    def __init__(self, text=None):
        if text is not None:
            self._parse(text)

    
    def parse(self, text):
        
        # clean the data of \", \n and ],
        text = text.replace('\\"', '"')
        text = text.replace('\\n', '')
        text = text.replace('],', ']')

        # parse the text recursively
        self.root = self._parse_rec(Node([], None), text)
        
        
    def _parse_rec(self, node, text):

        # Step 1: Trim outside [ and ]
        text = text[text.find('[')+1 : text.rfind(']')]

        # just one data entry
        if ',' not in text:
            node.children.append(Node(children=None, value=text))
            return node


        # start of data chunk
        beg = 0

        # level seperator counter
        x = 0

        # pause if text is in quotes
        pause = False

        for end in range(len(text)):
            if text[end] == '"':
                pause = not pause
            elif (text[end] == ',') and (x == 0) and not pause:
                node.children.append(Node(children=None, value=text[beg:end]))
                beg = end + 1
            elif text[end] == '[' and not pause:
                x += 1
            elif text[end] == ']' and not pause:
                x -= 1
                if x == 0:
                    node.children.append(self._parse_rec(Node(children=[], value=None), text=text[beg:end+1]))
                    beg = end + 1
                elif x < 0:
                    raise Exception('Error, more ] than [ !!!')
        
        # append the last element
        if beg <= end:
            node.children.append(Node(children=None, value=text[beg:]))

        return node


                
    def get_path(self, text):
        """
        Returns a path to the data. Mostly used for testing purposes to find / define paths to relevant information

        Args:
          text: the exact text to find
        """

        def get_path_rec(node, path):
            if node.children is None:
                return path if node.value == text else None

            for i in range(len(node.children)):
                path.append(i)
                r = get_path_rec(node.children[i], path)
                if r is not None:
                    return r
                path.pop()

            return None

        path = get_path_rec(self.root, [])

        if path is None:
            raise Exception('Could not find %s !!!' % text)

        return path

    
    def search(self, path):
        """
        """

        node = self.root
        for d in path:
            node = node.children[d]
        return node.value



from pprint import pformat
from collections import defaultdict

class MapItems:
    pass


class Map:

    def __init__(self, row=1, col=1, init=0):
        self._value = [[init for c in range(col)] for r in range(row)]
        self._items = defaultdict(list)

    @property
    def items(self):
        return self._items

    @property
    def rows(self):
        return len(self._value)

    @property
    def cols(self):
        return len(self._value[0])

    def init_from_lst(self, init_lst):
        if isinstance(init_lst, list):
            self.__init__(row=len(init_lst), col=len(init_lst[0]))
        for col in range(self.cols):
            for row in range(self.rows):
                self[row, col] = init_lst[row][col]

    def __getitem__(self, item):
        row, col = item
        return self._value[row][col]

    def __setitem__(self, key, value):
        row, col = key
        self._value[row][col] = value

    def __iter__(self):
        return iter(self._value)

    def __repr__(self):
        repr_str = "Map:\n"
        repr_str += '  +| [\n'
        for lst in self:
            repr_str += '  +| ' + ' ' * 4 + str(lst) + ',\n'
        repr_str += '  +| ]\n'
        return repr_str

"""A5-08 ~ Francisco Lopez"""


class Array:
    MIN_INDEX = 0
    DEFAULT_SIZE = 6
    DEFAULT_ITEM = "Tutorial"

    def __init__(self, size=DEFAULT_SIZE, item=DEFAULT_ITEM):
        """Initializes the array class"""
        self._length = size
        self._items = item
        self._array = [item for _ in range(size)]

    def __getitem__(self, index):
        """Gets the value of an item at an index in"""
        if not self.valid_index(index, self._length):
            raise IndexError
        return self._array[index]

    def __setitem__(self, index, value):
        """Sets an item's value into the index of the array"""
        if type(value) is not str:
            raise ValueError
        if not self.valid_index(index, self._length):
            raise IndexError
        self._array[index] = value

    def __len__(self, array):
        """Gets the length of the array"""
        length = len(array)
        return length

    @staticmethod
    def valid_index(index, period):
        """Checks if the index given is inside the list"""
        if 0 <= index < period:
            return True
        # else
        return False

    def __str__(self):
        """Stringifies the array"""
        array_str = ""
        for i in range(len(self._array)):
            if len(self._array) - 1 == i:
                array_str += f"{self._array[i]}"
            else:
                array_str += f"{self._array[i]}, "
        return array_str
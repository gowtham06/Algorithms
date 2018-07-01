import collections


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int

        """
        self.capacity = capacity
        #         self.lru=dict()
        #         self.cache=dict()
        #         self.counter=0
        self.cache = collections.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        try:
            self.cache.pop(key)
        except KeyError:
            if (len(self.cache.keys()) >= self.capacity):
                self.cache.popitem(last=False)
        self.cache[key] = value


if __name__ == '__main__':
    print("Lru Cache implementation")

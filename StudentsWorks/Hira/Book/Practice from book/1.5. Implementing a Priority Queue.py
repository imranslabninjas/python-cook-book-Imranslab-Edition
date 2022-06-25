'''

Problem
You want to implement a queue that sorts items by a given priority and always returns
the item with the highest priority on each pop operation.


'''

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    # Here is an example of how it might be used:
    class Item:
        def __init__(self, name):
            self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

        q = PriorityQueue()
        q.push(Item('foo'), 1)
        q.push(Item('bar'), 5)
        q.push(Item('spam'), 4)
        q.push(Item('grok'), 1)
        q.pop()
        #print(Item('bar'))
        q.pop()
        #print(Item('spam'))
        q.pop()
        Item('foo')
        q.pop()
        #print(Item('grok'))

"""
PriorityQueue class

Based on https://docs.python.org/3.5/library/heapq.html#priority-queue-implementation-notes
"""

import heapq
import itertools as it

class PriorityQueue:
    __REMOVED = object()
    def __init__(self, items=(), heap_type='min', queue_order='fifo'):
        """
        PriorityQueue

        Keyword Arguments:
            items -- iterable of key priority pairs
            heap_type -> 'min'|'max'
            queue_order -> 'fifo'|'lifo'
        """
        self.__pq = []
        self.__ef = {}
        self.__id = it.count()
        if heap_type == 'min':
            self.__m = 1
        elif heap_type == 'max':
            self.__m = -1
        else:
            raise Exception('invalid heap_type ({})'.format(heap_type))
        
        if queue_order == 'fifo':
            self.__c = 1
        elif queue_order == 'lifo':
            self.__c = -1
        else:
            raise Exception('invalid queue_order ({})'.format(queue_order))

        for k,p in items:
            self[k] = p
    
    def __len__(self):
        return len(self.__ef)

    def __setitem__(self, k, priority):
        if k in self:
            del self[k]
        
        count = next(self.__id)
        entry = [priority * self.__m, count * self.__c, k]

        self.__ef[k] = entry
        heapq.heappush(self.__pq, entry)

    def __getitem__(self, k):
        return self.__ef[k][0] * self.__m

    def __delitem__(self, k):
        entry = self.__ef.pop(k)
        entry[-1] = PriorityQueue.__REMOVED

    def __contains__(self, k):
        return k in self.__ef

    def __iter__(self):
        return (i for i in self.__ef)
    
    def add(self, k, priority):
        self[k] = priority
    
    def remove(self, k):
        del self[k]

    def pop(self):
        while self.__pq:
            _, _, k = heapq.heappop(self.__pq)
            if k is not PriorityQueue.__REMOVED:
                del self.__ef[k]
                return k
        raise KeyError('pop from an empty priority queue')
    
    def peek(self):
        while self.__pq:
            _, _, k = self.__pq[0]
            if k is not PriorityQueue.__REMOVED:
                return k
            else:
                heapq.heappop(self.__pq)

        raise KeyError('peek from an empty priority queue')

    
    def keys(self):
        return (i for i in self)

    def items(self):
        return ((i, self[i]) for i in self) 

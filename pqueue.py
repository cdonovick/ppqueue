"""
PriorityQueue class

Based on https://docs.python.org/3.5/library/heapq.html#priority-queue-implementation-notes
"""

import heapq
import itertools as it

class PriorityQueue:
    __REMOVED = object()
    def __init__(self, items=(), max_heap=False):
        """
        PriorityQueue

        Keyword Arguments:
            items -- iterable of key priority pairs
            max_heap -- use max heap instead of min heap
        """
        self.__pq = []
        self.__ef = {}
        self.__id = it.count()
        self.__m = (-1 if max_heap else 1)

        for k,p in items:
            self[k] = p
    
    def __len__(self):
        return len(self.__ef)

    def __setitem__(self, k, priority):
        if k in self:
            del self[k]
        
        count = next(self.__id)
        entry = [priority * self.__m, count, k]

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

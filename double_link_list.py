#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import getsizeof
class LinkListNode(object):
    
    __slots__ = '_prev', 'data', '_next'
    
    def __init__(self, prev, data, next):
        self._prev = prev
        self.data = data
        self._next = next
        
    def __str__(self):
        return "%s" % self.data
    
class DoubleLinkList(object):
    def __init__(self, L=[]):
        self.top = None
        self.length = 0
        self.bottom = None
        self.current_node = None
        if len(L) > 0:
            for each in L:
                self.add(each)
                
    def __len__(self):
        return self.length
    
    def __iter__(self):
        self.current_node = self.top
        return self
    
    def __next__(self):
        if self.current_node is None:
            raise StopIteration
        current_node = self.current_node
        self.current_node = self.current_node._next
        return current_node.data
                
    def __str__(self):
        string = '[ '
        for each in self:
            string += str(each)+', '
        string = string[:-2] + ' ]'
        return string
        
    def add(self, value):
        new_bottom = LinkListNode(self.bottom, value, None)
        self.length += 1
        if self.bottom is not None:
            self.bottom._next = new_bottom
        self.bottom = new_bottom
        if self.top is None:
            self.top = self.bottom
        
    def __getitem__(self, key):
        if self.length == 0:
            raise Exception('empty list')
        if key < 0 or key >= self.length:
            raise IndexError
        if key == 0:
            return self.top.data
        if key <= self.length // 2:
            current_node = self.top
            for i in range(key):
                current_node = current_node._next
            return current_node.data
        else:
            current_node = self.bottom
            for i in range(self.length-key-1):
                current_node = current_node._prev
            return current_node.data
    
    def __setitem__(self, key, value):
        if self.length == 0:
            raise Exception('empty list')
        if key < 0 or key >= self.length:
            raise IndexError
        if key == 0:
            self.top.data = value
            return
        if key <= self.length // 2:
            current_node = self.top
            for i in range(key):
                current_node = current_node._next
            current_node.data = value
        else:
            current_node = self.bottom
            for i in range(self.length-key-1):
                current_node = current_node._prev
            current_node.data = value
            
    def insert(self, key, value):
        if key < 0 or key > self.length:
            raise IndexError
        if key == self.length:
            self.add(value)
            return
        elif key == 0:
            new_top = LinkListNode(None, value, self.top)
            self.top._prev = new_top
            self.top = new_top
        else:
            node = LinkListNode(None, value, None)
            if key <= self.length // 2:
                current_node = self.top
                for i in range(key):
                    current_node = current_node._next
            else:
                current_node = self.bottom
                for i in range(self.length-key-1):
                    current_node = current_node._prev   
            prev = current_node._prev        
            prev._next = node
            current_node._prev = node
            node._prev = prev
            node._next = current_node
        self.length += 1
            
    
    def remove(self, key):
        if self.length ==  0:
            raise Exception('empty list')
        if key < 0 or key >= self.length:
            raise IndexError  
        if key == 0:
            if self.length == 1:
                self.top = None
                self.bottom = None
                self.length = 0
                return
            self.top._next._prev = None
            self.top = self.top._next
        elif key == self.length-1:
            self.bottom._prev._next = None
            self.bottom = self.bottom._prev
        else:
            if key <= self.length // 2:
                current_node = self.top
                for i in range(key):
                    current_node = current_node._next
            else:
                current_node = self.bottom
                for i in range(self.length-key-1):
                    current_node = current_node._prev   
            prev = current_node._prev        
            current_node._next._prev = prev
            prev._next = current_node._next
        self.length -= 1
        
if __name__ == '__main__':
    d = DoubleLinkList()
    for i in range(1000):
        d.add(i)
    print(getsizeof(d.top))
    
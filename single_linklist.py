# -*- coding: utf-8 -*-

class SingleLinkNode(object):
    
    __slots__ = 'data', '_next'
    
    def __init__(self, data, next):
        self.data = data
        self._next = next
        
    def __str__(self):
        return "%s" % self.data
        
        
class SingleLinkList(object):
    def __init__(self, l=[]):
        self.head = None
        self.length = 0
        self.current_node = None        
        if len(l) > 0:
            l.reverse()
            for each in l:
                self.add(each)
        
    def add(self, value):
        self.head = SingleLinkNode(value, self.head)
        self.length += 1
        
    def delete(self, value):
        if self.length == 0:
            raise Exception('empty list')
        if self.head.data == value:
            if self.head._next is None:
                self.head = None
                self.length = 0
                return True
            else:
                self.head = self.head._next
                self.length -= 1
                return True
        else:
            current_node = self.head
            while current_node is not None:
                if current_node._next is not None and current_node._next.data == value:
                    if current_node._next._next is not None:
                        current_node._next = current_node._next._next
                        self.length -= 1
                        return True
                    else:
                        current_node._next = None
                        self.length -= 1
                        return True
                current_node = current_node._next        
            raise Exception('not in the list')
        
    def remove(self, key):
        if self.length == 0:
            raise Exception('empty list')
        if key < 0 or key > self.length - 1:
            raise IndexError
        if key == 0:
            if self.head._next is not None:
                self.head = self.head._next
            else:
                self.head = None
            self.length -= 1
        else:
            current_node = self.head
            for i in range(key-1):
                current_node = current_node._next
            if current_node._next._next is not None:
                current_node._next = current_node._next._next
            else:
                current_node._next = None
            self.length -= 1
        return True
            
    def insert(self, key, value):
        if self.length == 0:
            raise Exception('empty list')
        if key < 0 or key > self.length:
            raise IndexError   
        if key == 0:
            self.head = SingleLinkNode(value, self.head)
            self.length += 1
        else:
            current_node = self.head
            for i in range(key-1):
                current_node = current_node._next
            current_node._next = SingleLinkNode(value, current_node._next)
            self.length += 1
            
    def __len__(self):
        return self.length
    
    def __iter__(self):
        self.current_node = self.head
        return self
    
    def __next__(self):
        for i in range(self.length):
            current_node = self.current_node
            if current_node is None:
                self.current_node = self.head
                raise StopIteration            
            if self.current_node._next is not None:
                self.current_node = self.current_node._next
            else:
                self.current_node = None     
            return current_node.data
        
    def __getitem__(self, key):
        if self.length == 0:
            raise Exception('empty list')
        if key < 0 or key > self.length - 1:
            raise IndexError
        if key == 0:
            return self.head
        else:
            current_node = self.head
            for i in range(key):
                current_node = current_node._next
            return current_node.data
    
    def __setitem__(self, key, value):
        if key < 0 or key > self.length - 1:
            raise IndexError   
        if key == 0:
            self.head.data = value
        else:
            current_node = self.head
            for i in range(key):
                current_node = current_node._next
            current_node.data = value
                
    def __str__(self):
        string = 'SingleLinkList [ '
        current_node = self.head
        string += str(current_node.data)
        for i in range(self.length-1):
            current_node = current_node._next
            string += ' -> '+str(current_node)
        string += ' ]'
        return string
        
class Stack(SingleLinkList):
    def __init__(self, l=[]):
        super(Stack, self).__init__(l)
    
    def push(self, value):
        self.add(value)
        
    def pop(self):
        head = self.head
        self.remove(0)
        return head
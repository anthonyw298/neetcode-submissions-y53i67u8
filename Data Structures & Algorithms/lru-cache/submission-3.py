class Node:
    def __init__(self,key,value, nxt = None, prev = None):
        self.key = key
        self.val = value
        self.next = nxt
        self.prev = prev
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} # key = key, val = Node(key,val)
        self.tail, self.head = Node(0,0), Node(0,0)
        self.tail.next, self.head.prev = self.head, self.tail

    def insert(self,key):
        prev = self.head.prev
        head = self.head
        self.cache[key].next, self.cache[key].prev = head, prev
        prev.next = self.head.prev = self.cache[key]

    def remove(self,key):
        node = self.cache[key]
        node.prev.next, node.next.prev = node.next, node.prev

    def get(self, key):
        if key not in self.cache:
            return -1
        self.remove(key)
        self.insert(key)
        return self.cache[key].val

    def put(self,key,value):
        if key in self.cache:
            self.remove(key)
        node = Node(key,value)
        self.cache[key] = node
        self.insert(key)
        if len(self.cache) > self.capacity:
            lru = self.tail.next
            self.remove(lru.key)
            del self.cache[lru.key]















































'''class Node:
    def __init__(self,key,val):
        self.key,self.val=key,val
        self.prev=self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next,self.right.prev=self.right,self.left
    def insert(self,node):
        prev,nxt=self.right.prev,self.right
        prev.next=nxt.prev=node
        node.next=nxt
        node.prev=prev
    def remove(self,node):
        prev,nxt=node.prev,node.next
        prev.next=nxt
        nxt.prev=prev
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val #access the node val 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache)>self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
# Node: key, val, prev, next

# LRUCache:
  # init: cap, empty hashmap, two dummy nodes tied together
  # remove: rewire neighbors to skip over node
  # insert: slot node just before right dummy
  # get: if missing return -1, else move to MRU and return val
  # put: if key exists remove old, create new node, insert at MRU
  #      if over cap, grab left.next, remove it, delete from hashmap'''
class ListNode:
    def __init__(self,key_,value):
        self.key_ = key_
        self.value = value
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity):
        self.tail = ListNode("tail",None)
        self.head = ListNode("head",None)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = {}
        self.count = 0
        self.capacity = capacity

    def get(self, key_):
        node = self.cache.get(key_,None)
        if node is None:
            return -1
        self.deleteNode(node)
        self.insertNode(node)
        return node.value

    def put(self, key_, value):
        node = self.cache.get(key_,None)
        if node is None:
            node = ListNode(key_,value)
            self.insertCache(node)
            self.evictCache()
            return
        else:
            self.deleteNode(node)
            node.value = value
            self.insertNode(node)
            return
    def evictCache(self):
        if self.count == self.capacity:
            node = self.tail.prev
            self.deleteCache(node)
        else:
            self.count+=1

    def deleteCache(self,node):
        key_ = node.key_
        del self.cache[key_]
        self.deleteNode(node)

    def insertCache(self,node):
        self.cache[node.key_]=node
        self.insertNode(node)

    def deleteNode(self,node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev        

    def insertNode(self,node):
        nxtNode = self.head.next
        self.head.next = node
        node.next = nxtNode
        node.prev = self.head
        nxtNode.prev = node



       

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.add_at_end(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:

        # If Node already exist
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove_node(node)
            self.add_at_end(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.add_at_end(node)

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove_node(lru)
            del self.cache[lru.key]

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_at_end(self, node):
        second_last = self.tail.prev
        second_last.next = node
        node.prev = second_last
        node.next = self.tail
        self.tail.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

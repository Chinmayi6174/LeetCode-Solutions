class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def add_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    def remove_last(self):
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove(node)
        return node
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        self.keyMap = {}                     # key -> node
        self.freqMap = defaultdict(DoublyLinkedList)  # freq -> DLL
    def _update_freq(self, node):
        freq = node.freq
        self.freqMap[freq].remove(node)
        if freq == self.minFreq and self.freqMap[freq].size == 0:
            self.minFreq += 1
        node.freq += 1
        self.freqMap[node.freq].add_front(node)
    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1
        node = self.keyMap[key]
        self._update_freq(node)
        return node.value
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.keyMap:
            node = self.keyMap[key]
            node.value = value
            self._update_freq(node)
            return
        if self.size == self.capacity:
            lfu_node = self.freqMap[self.minFreq].remove_last()
            del self.keyMap[lfu_node.key]
            self.size -= 1
        new_node = Node(key, value)
        self.keyMap[key] = new_node
        self.freqMap[1].add_front(new_node)
        self.minFreq = 1
        self.size += 1

class Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key: int = -1, value: int = -1) -> None:
        self.key: int = key
        self.value: int = value
        self.prev: Node | None = None
        self.next: Node | None = None

    def __repr__(self) -> str:
        return f"Node(key={self.key}, value={self.value})"


class LRUCache:
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self.capacity: int = capacity
        self.cache: dict[int, Node] = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        left = node.prev
        right = node.next
        assert left is not None and right is not None
        left.next = right
        right.prev = left
        node.prev = None
        node.next = None

    def _insert_at_front(self, node_to_insert: Node) -> None:
        first_node = self.head.next
        assert first_node is not None
        node_to_insert.prev = self.head
        node_to_insert.next = first_node
        first_node.prev = node_to_insert
        self.head.next = node_to_insert

    def _move_to_front(self, node: Node) -> None:
        self._remove(node)
        self._insert_at_front(node)

    def get(self, key: int, default: int | None = None) -> int | None:
        node = self.cache.get(key)
        if node is None:
            return default
        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node_to_update = self.cache.get(key)
        if node_to_update is not None:
            node_to_update.value = value
            self._move_to_front(node_to_update)
            return
        if len(self.cache) == self.capacity:
            node_to_remove = self.tail.prev
            assert node_to_remove is not None
            self.cache.pop(node_to_remove.key)
            self._remove(node_to_remove)
        node_to_insert = Node(key, value)
        self._insert_at_front(node_to_insert)
        self.cache[key] = node_to_insert


def main() -> None:
    cache = LRUCache(capacity=2)
    assert cache.get(8) is None
    cache.put(5, 55)
    assert cache.get(5) == 55
    cache.put(6, 66)
    assert cache.get(6) == 66
    cache.put(5, 54)
    assert cache.get(5) == 54
    cache.put(2, 22)
    assert cache.get(6) is None
    assert cache.get(5) == 54
    assert cache.get(2) == 22


main()

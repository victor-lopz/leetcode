from typing import Optional, Dict


class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.next_node: Optional["Node"] = None
        self.previous_node: Optional["Node"] = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError(
                "Input parameter 'capacity' cannot be negative or zero. "
                "It must be a positive integer."
            )
        self.capacity = capacity
        self.cache_dict: Dict[int, Node] = {}
        self.head_node = Node(0, 0)
        self.tail_node = Node(0, 0)
        self.head_node.next_node = self.tail_node
        self.tail_node.previous_node = self.head_node

    def _insert_node_beginning(self, node_to_insert: Node):
        node_to_insert.next_node = self.head_node.next_node
        node_to_insert.previous_node = self.head_node
        self.head_node.next_node.previous_node = node_to_insert  # type: ignore
        self.head_node.next_node = node_to_insert

    def _remove_node(self, node_to_remove: Node):
        next_one = node_to_remove.next_node
        previous_one = node_to_remove.previous_node
        previous_one.next_node = next_one  # type: ignore
        next_one.previous_node = previous_one  # type: ignore

    def get(self, key: int) -> int | None:
        if key not in self.cache_dict:
            return None
        node = self.cache_dict[key]
        self._remove_node(node)
        self._insert_node_beginning(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict:
            node_to_update = self.cache_dict[key]
            self._remove_node(node_to_update)
            self._insert_node_beginning(node_to_update)
            node_to_update.value = value
            return
        # now if key is not in cache:
        if len(self.cache_dict) == self.capacity:
            node_to_delete = self.tail_node.previous_node
            self._remove_node(node_to_delete)  # type: ignore
            self.cache_dict.pop(node_to_delete.key)  # type: ignore
        node_to_insert = Node(key, value)
        self.cache_dict[key] = node_to_insert
        self._insert_node_beginning(node_to_insert)


def test1():
    x = LRUCache(capacity=0)
    max_iter = 10
    for i in range(max_iter):
        x.put(i, i)

    for i in range(max_iter):
        print(x.get(i))


def test2():
    x = LRUCache(capacity=2)
    x.put(1, 1)
    x.put(2, 2)
    print(x.get(1))
    x.put(3, 3)
    print(x.get(2))
    x.put(4, 4)
    print(x.get(1))
    print(x.get(2))
    print(x.get(3))
    print(x.get(4))


if __name__ == "__main__":
    test1()
    test2()

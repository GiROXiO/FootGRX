from utils.nodes.Node import Node
from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class DoubleLinkedCircularList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self.size: int = 0
        
    def is_empty(self) -> bool:
        return self.size == 0
    
    def add(self, value: T) -> None:
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.set_next(new_node)
            new_node.set_prev(new_node)
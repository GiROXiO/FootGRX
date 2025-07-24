from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, value: T):
        self.value: T = value
        self.next: Optional[Node[T]] = None
        self.prev: Optional[Node[T]] = None
        self.index: int = -1 
    
    def get_next(self) -> Optional['Node[T]']:
        return self.next
    
    def get_prev(self) -> Optional['Node[T]']:
        return self.prev
    
    def get_value(self) -> T:
        return self.value
    
    def get_index(self) -> int:
        return self.index
    
    def set_next(self, next_node: Optional['Node[T]']) -> None:
        self.next = next_node
    
    def set_prev(self, prev_node: Optional['Node[T]']) -> None:
        self.prev = prev_node
    
    def set_value(self, value: T) -> None:
        self.value = value 
    
    def set_index(self, index: int) -> None:
        self.index = index
    
    def __repr__(self) -> str:
        return f"{self.value}"
    
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.value == other.value
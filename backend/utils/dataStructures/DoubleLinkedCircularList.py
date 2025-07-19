import sys
sys.path.append("../nodes")  # Adjust the path as necessary to import Node

from nodes.Node import Node
from typing import TypeVar, Generic, Optional, Callable, Any

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
        elif self.head != None and self.tail != None:
            new_node.set_next(self.head)
            new_node.set_prev(self.tail)
            self.tail.set_next(new_node)
            self.head.set_prev(new_node)
            self.tail = new_node
        else:
            raise ValueError("List is in an inconsistent state: head or tail is None")
        self.size += 1
    
    def show(self) -> None:
        if self.is_empty():
            print("List is empty")
            return
        
        current = self.head
        while True:
            if current is not None:
                print(current.get_value(), end=" ")
                current = current.get_next()
            if current == self.head:
                break
        print()
    
    def update(self, old_value: T, new_value: T, key: Callable[[T], Any]) -> None:
        if self.is_empty():
            raise ValueError("Cannot update in an empty list")
        
        current = self.head
        while True:
            if current is not None and key(current.get_value()) == key(old_value):
                current.set_value(new_value)
                break
            if current is not None:
                current = current.get_next()
            if current is self.head:
                break
    
    def remove(self, value: T) -> None:
        if self.is_empty():
            raise ValueError("Cannot remove from an empty list")
        
        if self.head is None or self.tail is None:
            raise ValueError("List is in an inconsistent state: head is None")
        else:
            current = self.head
            while True:
                if current is not None and current.get_value() == value:
                    if (
                        self.head is not None and
                        self.tail is not None and
                        current.get_value() == self.head.get_value() and
                        current.get_value() == self.tail.get_value()
                    ):
                        self.head = None
                        self.tail = None
                        
                    elif current == self.head:
                        self.head = current.get_next()
                        if self.head is not None and self.tail is not None:
                            self.head.set_prev(self.tail)
                            self.tail.set_next(self.head)
                    elif current == self.tail:
                        self.tail = current.get_prev()
                        if self.head is not None and self.tail is not None:
                            self.tail.set_next(self.head)
                            self.head.set_prev(self.tail)
                    else:
                        prev_node = current.get_prev()
                        next_node = current.get_next()
                        if prev_node is not None and next_node is not None:
                            prev_node.set_next(next_node)
                            next_node.set_prev(prev_node)
                    self.size -= 1
                    break
                current = current.get_next()
                if current is None or current == self.head:
                    break
    
    def find(self, match_func: Callable[[T], bool]) -> T:
        if self.is_empty():
            raise ValueError("Cannot find in an empty list")
        current = self.head
        while True:
            if current is not None and match_func(current.get_value()):
                return current.get_value()
            if current is not None:
                current = current.get_next()
            if current is self.head:
                break
        raise ValueError("No matching element found")
    
    def get_size(self) -> int:
        return self.size 
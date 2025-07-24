from src.backend.utils.nodes.Node import Node
from typing import TypeVar, Generic, Optional, Callable, Any
import math

T = TypeVar('T')

class DoubleLinkedCircularList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self.size: int = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def add(self, value: T) -> bool:
        try:
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
                return False 
            new_node.set_index(self.size)
            self.size += 1
            return True
        except Exception as e:
            print(f"AN ERROR OCCURRED WHILE ADDING {value} TO THE MULTILIST: {e}")
            return False

    def show(self) -> None:
        try:
            if self.is_empty():
                print("List is empty")
                return
            
            current = self.head
            while True:
                if current is not None:
                    print(str(current.get_index()) + ". " + str(current.get_value()))
                    current = current.get_next()
                    if current == self.head:
                        break
            print()
        except Exception as e:
            print(f"AN ERROR OCCURRED WHILE SHOWING MULTILIST: {e}")
            return

    def find_node(self, compare_func: Callable[[Any], bool]) -> Optional[Node[T]]:
        try:
            if self.is_empty():
                return None
            
            current = self.head
            while True:
                if current is None:
                    return None
                if compare_func(current.get_value()):
                    return current
                current = current.get_next()
                if current == self.head:
                    break
            return None
        except Exception as e:
            print(f"AN ERROR OCCURRED WHILE FINDING THE NODE REQUIRED: {e}")

    def update_node(self, compare_func: Callable[[Any], bool], update_func: Callable[[Any], Any]) -> bool:
        node = self.find_node(compare_func)
        if node is not None:
            update_func(node.get_value())
            return True
        return False

    def get_size(self) -> int:
        return self.size 

    def update_indexes(self):
        if self.is_empty():
            print("List is empty, cannot update indexes")
            return
        
        current = self.head
        index = 0
        while True:
            if current is not None:
                current.set_index(index)
                index += 1
                current = current.get_next()
                if current is self.head:
                    break
        self.size = index

    def get_by_index(self, index: int) -> Any:
        print("Getting index: " + str(index))
        if self.is_empty():
            print("List is empty, cannot get index")
            return None
        
        if index < 0 or index >= self.size:
            print(f"Index {index} out of bounds")
            return None
        
        step = int(math.sqrt(self.size))
        current = self.head
        temp = None
        realized_steps = 0
        
        while current is not None and realized_steps < index:
            temp = current
            for _ in range(step):
                if current is None:
                    print("Current is None, breaking")
                    break
                if current.get_next() is not self.head and current is not None:
                    current = current.get_next()
                    realized_steps += 1
            if realized_steps >= index:
                temp = current
                if temp is not None:
                    print(f"Reached index {temp.get_index()} with value: {temp.get_value()}")
        
        while temp is not None and temp.get_index() >= index:
            print(f"Checking index {temp.get_index()} with value: {temp.get_value()}")
            if temp.get_index() == index:
                print(f"Found value at index {index}: {temp.get_value()}")
                return temp
            temp = temp.get_prev()
        
        return None
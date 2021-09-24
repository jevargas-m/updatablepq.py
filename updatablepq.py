import heapq

class UpdatablePriorityQueue:
    """Implements a priority queue in which items are unique, if the 
    same item is pushed again the priority gets updated.
    Items must be hashable and comparable for this to work.
    Push and Pop operations are done in O(log N).  updates in O(N)"""
    def __init__(self):
        self.__heap = []  #stores tuples (priority, item)
        self.__set_items = set()

    def __len__(self):
        return len(self.__heap)

    def __repr__(self) -> str:
        tokens = [str(t) for t in self.sorted_list()]
        return f"<{', '.join(tokens)}>"

    def copy(self):
        other = UpdatablePriorityQueue()
        other.__heap = self.__heap[:]
        other.__set_items = self.__set_items.copy()
        return other

    def sorted_list(self):
        heap_cp = self.__heap[:]
        return [heapq.heappop(heap_cp) for _ in range(len(self.__heap))]
    
    def is_empty(self):
        return len(self.__heap) < 1

    def look_min(self):
        """returns item at top of the queue (minimum priority).  O(1)"""
        if self.is_empty():
            return None
        _, item = self.__heap[0]
        return item

    def pop_min(self):
        """Pops and returns item at the top of the queue"""
        if self.is_empty():
            return None
        _, item = heapq.heappop(self.__heap)
        self.__set_items.remove(item)
        return item

    def push_or_update(self, item, priority):
        """Pushes a new item to que queue with given priority in O(log N).  
           If the item is already in the queue it updates its priority to the 
           new one, updating is done in O(N)."""
        if item in self.__set_items:
            new_node = None
            for i, (_, current_item) in enumerate(self.__heap):
                if item == current_item:
                    new_node = (priority, item)
                    self.__heap[i] = new_node
                    break
            heapq.heapify(self.__heap)
        else:
            heapq.heappush(self.__heap, (priority, item))
            self.__set_items.add(item)
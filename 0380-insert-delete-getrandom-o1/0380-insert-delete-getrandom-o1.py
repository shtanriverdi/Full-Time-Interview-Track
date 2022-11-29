class RandomizedSet:
    def __init__(self):
        self.nums_set = set()
        self.nums_list = []
        self.index_map = defaultdict(int)

    def hasElement(self, val):
        return val in self.nums_set
        
    def insert(self, val: int) -> bool:
        if self.hasElement(val):
            return False
        
        self.nums_set.add( val )
        self.nums_list.append( val )
        self.index_map[ val ] = len(self.nums_list) - 1
        return True

    def remove(self, val: int) -> bool:
        if self.hasElement(val) == False:
            return False
        
        index_to_removed = self.index_map[ val ]
        # Remove the Value from map
        self.index_map.pop( val )
        # Update other num's index on the map
        self.index_map[self.nums_list[-1]] = index_to_removed
        # Move val to be removed to the end
        self.nums_list[index_to_removed], self.nums_list[-1] = self.nums_list[-1], self.nums_list[index_to_removed]
        # Remove the Value from list & set
        self.nums_list.pop()
        self.nums_set.discard( val )
        return True

    def getRandom(self) -> int:
        # Generate random number between 0 <= random <= len
        list_length = len(self.nums_list)
        random_index = random.randrange(list_length)
        return self.nums_list[random_index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
class RandomizedSet:

    def __init__(self):
        self.data_list = []
        self.data_dict = {}
        
    def search(self, val: int) -> int:
        return val in self.data_dict


    def insert(self, val: int) -> bool:
        if self.search(val):
            return False
        else:
            self.data_list.append(val)
            self.data_dict[val] = len(self.data_list) - 1
            return True

    def remove(self, val: int) -> bool:
        if not self.search(val):
            return False
        else:
            idx = self.data_dict[val]
            self.data_list[idx] = self.data_list[-1]
            self.data_dict[self.data_list[-1]] = idx
            self.data_list.pop()
            del self.data_dict[val]
            return True

    def getRandom(self) -> int:
        return random.choice(self.data_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

class MyHashSet:

    def __init__(self):
        self.hashMap = []

    def add(self, key: int) -> None:
        if not key in self.hashMap:
            self.hashMap.append(key)

    def remove(self, key: int) -> None:
        if key in self.hashMap:
            self.hashMap.remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.hashMap else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
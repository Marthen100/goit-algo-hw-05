class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        new_node = HashNode(key, value)
        if self.buckets[index] is None:
            self.buckets[index] = new_node
        else:
            current = self.buckets[index]
            while True:
                if current.key == key:
                    current.value = value  # Update the value if key already exists
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node
        self.size += 1

    def search(self, key):
        index = self._hash(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self._hash(key)
        current = self.buckets[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.buckets[index] = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next
        return False  # Return False if the key was not found

    def display(self):
        for i in range(self.capacity):
            print(f"Bucket {i}: ", end="")
            current = self.buckets[i]
            while current:
                print(f"({current.key}, {current.value})", end=" -> ")
                current = current.next
            print("None")

# Example usage
ht = HashTable()
ht.insert("key1", "value1")
ht.insert("key2", "value2")
ht.insert("key3", "value3")

print("Initial Hash Table:")
ht.display()

print("\nDeleting 'key2':")
ht.delete("key2")
ht.display()

print("\nCurrent state after deletion:")
ht.display()
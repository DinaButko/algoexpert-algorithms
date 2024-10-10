class MyHashMap:

    # Time Complexity O(1), space complexity O(n)
    def __init__(self):
        # Initialize the hashMap as an empty dictionary
        self.hashMap = {}

    def put(self, key: int, value: int) -> None:
        # Assign the value to the specified key in the dictionary
        self.hashMap[key] = value

    def get(self, key: int) -> int:
        # Return the value for the key if it exists, otherwise return -1
        return self.hashMap.get(key, -1)  # Use -1 for non-existent keys

    def remove(self, key: int) -> None:
        # Use pop to remove the key, avoiding KeyError if the key does not exist
        self.hashMap.pop(key, None)  # Safely remove the key if it exists

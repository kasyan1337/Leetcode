class MyCircularDeque:
    # Step 1: Initialize the circular toy box with a certain number of slots (capacity).
    def __init__(self, capacity: int):
        self.capacity = capacity  # How many toys the toy box can hold
        self.toy_box = [-1] * capacity  # Empty toy box, represented by -1
        self.front_pointer = 0  # This points to where the front toy is
        self.back_pointer = 0  # This points to the next available spot at the back
        self.current_size = 0  # How many toys are currently in the toy box

    # Step 2: Add a toy to the front of the toy box
    def addToyToFront(self, toy: int) -> bool:
        if self.isToyBoxFull():
            return False  # If the toy box is full, we can't add a toy to the front.

        # Move the front_pointer backward to make space for the new toy (wrap around)
        self.front_pointer = (self.front_pointer - 1 + self.capacity) % self.capacity
        self.toy_box[self.front_pointer] = toy  # Put the toy in the front
        self.current_size += 1  # Increase the number of toys
        return True  # We successfully added the toy!

    # Step 3: Add a toy to the back of the toy box
    def addToyToBack(self, toy: int) -> bool:
        if self.isToyBoxFull():
            return False  # If the toy box is full, we can't add a toy to the back.

        # Add the toy to the back and move the back_pointer forward
        self.toy_box[self.back_pointer] = toy
        self.back_pointer = (self.back_pointer + 1) % self.capacity
        self.current_size += 1  # Increase the number of toys
        return True  # We successfully added the toy!

    # Step 4: Remove a toy from the front of the toy box
    def removeToyFromFront(self) -> bool:
        if self.isToyBoxEmpty():
            return False  # If the toy box is empty, there's no toy to remove.

        # Move the front_pointer forward to remove the toy at the front
        self.front_pointer = (self.front_pointer + 1) % self.capacity
        self.current_size -= 1  # Decrease the number of toys
        return True  # We successfully removed the toy!

    # Step 5: Remove a toy from the back of the toy box
    def removeToyFromBack(self) -> bool:
        if self.isToyBoxEmpty():
            return False  # If the toy box is empty, there's no toy to remove.

        # Move the back_pointer backward to remove the toy at the back
        self.back_pointer = (self.back_pointer - 1 + self.capacity) % self.capacity
        self.current_size -= 1  # Decrease the number of toys
        return True  # We successfully removed the toy!

    # Step 6: Peek at the front toy without removing it
    def peekAtFrontToy(self) -> int:
        if self.isToyBoxEmpty():
            return -1  # If there's no toy, return -1.
        return self.toy_box[self.front_pointer]  # Show the toy at the front

    # Step 7: Peek at the back toy without removing it
    def peekAtBackToy(self) -> int:
        if self.isToyBoxEmpty():
            return -1  # If there's no toy, return -1.
        # Since back_pointer points to the "next available" spot, we look one step back
        return self.toy_box[(self.back_pointer - 1 + self.capacity) % self.capacity]

    # Step 8: Check if the toy box is empty
    def isToyBoxEmpty(self) -> bool:
        return self.current_size == 0  # If there are no toys, it's empty!

    # Step 9: Check if the toy box is full
    def isToyBoxFull(self) -> bool:
        return self.current_size == self.capacity  # If the box is full, no more toys!

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

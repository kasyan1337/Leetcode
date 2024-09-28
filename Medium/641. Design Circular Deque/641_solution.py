class MyCircularDeque:

    def __init__(self, capacity: int):
        self.capacity = capacity

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False  # If the toy box is full, we can't add a toy to the front.

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False  # If the toy box is full, we can't add a toy to the front.

    def deleteFront(self) -> bool:

    def deleteLast(self) -> bool:

    def getFront(self) -> int:

    def getRear(self) -> int:

    def isEmpty(self) -> bool:

    def isFull(self) -> bool:

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

class MyCalendarTwo:
    def __init__(self):
        self.bookings = []  # Store intervals that are booked once
        self.overlaps = []  # Store intervals that are double booked

    def book(self, start: int, end: int) -> bool:
        # Step 1: Check if this event would cause a triple booking
        for o_start, o_end in self.overlaps:
            # If the new event overlaps with any double-booked interval, return False
            if max(start, o_start) < min(end, o_end):
                return False

        # Step 2: Check the new event against the single bookings
        for b_start, b_end in self.bookings:
            # If the new event overlaps with an existing booking, add the overlapping part to overlaps
            overlap_start = max(start, b_start)
            overlap_end = min(end, b_end)
            if overlap_start < overlap_end:
                self.overlaps.append((overlap_start, overlap_end))

        # Step 3: Add the new event to the bookings list since it doesn't cause a triple booking
        self.bookings.append((start, end))
        return True


# Example usage:
myCalendarTwo = MyCalendarTwo()
print(myCalendarTwo.book(10, 20))  # Output: True
print(myCalendarTwo.book(50, 60))  # Output: True
print(myCalendarTwo.book(10, 40))  # Output: True
print(myCalendarTwo.book(5, 15))  # Output: False
print(myCalendarTwo.book(5, 10))  # Output: True
print(myCalendarTwo.book(25, 55))  # Output: True

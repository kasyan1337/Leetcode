# Solution script

class MyCalendar:
    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        for existing_start, existing_end in self.events:
            if start < existing_end and end > existing_start:
                return False

        self.events.append((start, end))
        return True

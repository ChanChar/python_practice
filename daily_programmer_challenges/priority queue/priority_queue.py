class PriorityQueue(object):

    def __init__(self):
        self.queue = []

    def count(self):
        return "There are currently {} item(s) in the queue.".format(len(self.queue))

    def enqueue(self, item, priority_a, priority_b):
        new_entry = {"item": item, "priority_a": float(priority_a), "priority_b": float(priority_b)}
        self.queue.append(new_entry)

    @staticmethod
    def dequeue(current_queue, priority_level):
        next_item, highest_priority = None, 0
        if current_queue:
            for item in current_queue:
                if item[priority_level] > highest_priority:
                    highest_priority = item[priority_level]
                    next_item = item
            current_queue.remove(next_item)
            return "The next item is {}".format(next_item["item"])
        else:
            return "There are no item in queue."

    def dequeue_a(self):
        return self.dequeue(self.queue, "priority_a")

    def dequeue_b(self):
        return self.dequeue(self.queue, "priority_b")

    def normal_dequeue(self):
        if self.queue:
            next_item = self.queue.pop(0)
            return "The next item is {}.".format(next_item["item"])
        else:
            return "There are no items in queue."

    def clear(self):
        print("Are you sure you want to clear the queue? (Y/N)")
        confirmation = input(">>> ")
        if confirmation in "YESyes":
            self.queue = []
            print("Queue has been cleared.")
            print(self.count())
        else:
            print("Aborting current action...")
            print(self.count())
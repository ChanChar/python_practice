from priority_queue import PriorityQueue


def test():

    example_queue = PriorityQueue()

    example_queue.enqueue("lowest priority", 1.00, 1.10)
    example_queue.enqueue("medium priority", 5.00, 5.10)
    example_queue.enqueue("high priority", 10.00, 11.10)
    example_queue.enqueue("low", 1.20, 1.30)

    print(example_queue.count())
    assert example_queue.count() == "There are currently 4 item(s) in the queue."

    print(example_queue.dequeue_a())
    print(example_queue.dequeue_b())
    print(example_queue.normal_dequeue())

    assert example_queue.count() == "There are currently 1 item(s) in the queue."

    example_queue.clear()

test()
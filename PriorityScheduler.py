
import heapq

def priority_scheduler(jobs):
    queue = []

    for job, priority in jobs:
        heapq.heappush(queue, (priority, job))

    release_order = []

    while queue:
        priority, job = heapq.heappop(queue)
        release_order.append(job)
        print("Released:", job, "| Priority:", priority)

    print("Release Order:", release_order)


jobs = [
    ("Job A", 3),
    ("Job B", 1),
    ("Job C", 4),
    ("Job D", 2)
]

priority_scheduler(jobs)

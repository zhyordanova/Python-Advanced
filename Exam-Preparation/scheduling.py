from heapq import heappop, heapify, heappush


def read_input(is_test=True):
    if is_test:
        return [3, 1, 10, 1, 2], 0
    return (
        map(int, input().split(', ')),
        int(input())
    )


def min_cycles_for_job_sort(jobs, job_inex):
    sorted_jobs = sorted(
        [(v, i) for (i, v) in enumerate(jobs)]
    )
    cycles = 0
    for job, index in sorted_jobs:
        cycles += job
        if index == job_index:
            break
    return cycles


def min_cycles_for_job_heap(jobs,job_index):
    heap = []
    for (index, job) in enumerate(jobs):
        heappush(heap, (job,index))

    cycle = 0
    while True:
        job, index = heappop(heap)
        cycle += job
        if index == job_index:
            break

    return cycle


def print_result(result):
    print(result)


jobs, job_index = read_input()
print_result(
    min_cycles_for_job_sort(jobs, job_index)
)
print_result(
    min_cycles_for_job_heap(jobs, job_index)
)







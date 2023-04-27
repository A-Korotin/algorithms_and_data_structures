from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *

from collections import defaultdict


def main():
    votes = defaultdict(int)

    with open('io_folder/input.txt', 'r') as f:
        for line in f:
            candidate, num_votes = line.strip().split()
            votes[candidate] += int(num_votes)

    with open('io_folder/output.txt', 'w') as f:
        for candidate in sorted(votes.keys()):
            f.write(candidate + ' ' + str(votes[candidate]) + '\n')


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)


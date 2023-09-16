from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *


def main():
    with open("input.txt") as f:
        n, m, trump = f.readline().split()
        n, m = int(n), int(m)
        hand = f.readline().split()
        table = f.readline().split()

    ranks = "6789TJQKA"
    hand = [(ranks.find(k[0]) + 6, k[1]) for k in hand]
    table = [(ranks.find(k[0]) + 6, k[1]) for k in table]
    hand.sort()

    z = 0
    while z < m:
        k = 0
        while k < n and (table[z][0] > hand[k][0] or table[z][1] != hand[k][1]):
            k += 1
        if k < n:
            table.pop(z)
            hand.pop(k)
            z -= 1
            n -= 1
            m -= 1
            continue
        k = 0
        while k < n and trump != hand[k][1]:
            k += 1
        if k == n:
            print("NO")
            return
        if table[z][1] != trump:
            table.pop(z)
            hand.pop(k)
            z -= 1
            n -= 1
            m -= 1
            continue
        else:
            while k < n and (trump != hand[k][1] or table[z][0] > hand[k][0]):
                k += 1
            if k < n:
                table.pop(z)
                hand.pop(k)
                z -= 1
                n -= 1
                m -= 1
                continue
            else:
                print("NO")
                return

    if m:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)

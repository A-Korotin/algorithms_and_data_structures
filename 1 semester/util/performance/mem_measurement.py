import tracemalloc


start_mem_trace = tracemalloc.start


def get_max_mem_usage_mb() -> float:
    cur, peak = tracemalloc.get_traced_memory()
    return peak / 10 ** 6


def get_current_mem_usage_mb() -> float:
    cur, peak = tracemalloc.get_traced_memory()
    return cur / 10 ** 6


import time
import psutil

def mt(func, *args, **kwargs):
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    return end_time - start_time

def mc(func, *args, **kwargs):
    process = psutil.Process()
    cpu_percent_start = process.cpu_percent()
    result = func(*args, **kwargs)
    cpu_percent_end = process.cpu_percent()
    return cpu_percent_end - cpu_percent_start

def mm(func, *args, **kwargs):
    process = psutil.Process()
    mem_before = process.memory_info().rss
    result = func(*args, **kwargs)
    mem_after = process.memory_info().rss
    return mem_after - mem_before
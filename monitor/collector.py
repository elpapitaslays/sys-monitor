from . import cpu
from . import memory

def collect_metrics():
    collection = {
        "cpu": cpu.get_cpu_usage(),
        "memory": memory.get_memory_usage()
    }
    return collection

print(collect_metrics())
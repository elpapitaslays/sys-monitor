from . import cpu
from . import memory
from . import disk

def collect_metrics():
    collection = {
        "cpu": cpu.get_cpu_usage(),
        "memory": memory.get_memory_usage(),
        "disk": disk.get_disk_usage()
    }
    return collection
import psutil

def get_memory_usage():
    memory = psutil.virtual_memory()

    items = {
        "total": memory.total,
        "used": memory.used,
        "percent": memory.percent
    }

    return items
import psutil
import platform

os_name = platform.system()

def get_disk_usage():
    if os_name == "Windows":
        path = "C:\\"
    else:
        path = '/'

    usage = psutil.disk_usage(path)

    usage_dict = {
        "total": usage.total,
        "used": usage.used,
        "free": usage.free,
        "percent": usage.percent
    }

    return usage_dict
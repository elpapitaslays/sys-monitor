from monitor import collector
import time
import os
import platform

os_name = platform.system()

def run():
    while True:
        metrics = collector.collect_metrics()
        cpu_usage = list(metrics.values())[0]
        total_memory = list(metrics.values())[1]

        print("SYSTEM USAGE")
        print("============")
        print(f"CPU: {cpu_usage}%")
        print("============")
        for key, value in metrics['memory'].items():
            print(f"Memory {key}: {value}")
        
        time.sleep(1)
        if os_name == "Windows":
            os.system("cls")
        else:
            os.system("clear")
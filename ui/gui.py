from monitor import collector
import tkinter as tk
from tkinter import ttk

def update_metrics():
    metrics = collector.collect_metrics()
    
    cpu_label.config(text=f"CPU Usage: {metrics['cpu']}%")
    
    memory_text = ""
    for key, value in metrics['memory'].items():
        if key != "percent":
            value = value / (1024**3)
            memory_text += f"{key.capitalize()}: {value:.2f} GB\n"
        else:
            memory_text += f"{key.capitalize()}: {value}%\n"
    memory_label.config(text=memory_text)
    root.after(1000, update_metrics)

root = tk.Tk()
root.title("System Metrics")
root.geometry("300x200")

cpu_label = ttk.Label(root, text="CPU Usage: ", font=("Arial", 12))
cpu_label.pack(pady=10)

memory_label = ttk.Label(root, text="Memory Usage: ", font=("Arial", 12))
memory_label.pack(pady=10)

update_metrics()
root.mainloop()
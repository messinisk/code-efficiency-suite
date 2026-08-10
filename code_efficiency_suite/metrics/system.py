# metrics/system.py
import os, psutil

def system_info():
    process = psutil.Process(os.getpid())
    return {
        "cpu_count": os.cpu_count(),
        "threads": process.num_threads(),
        "is_single_thread": process.num_threads() == 1
    }

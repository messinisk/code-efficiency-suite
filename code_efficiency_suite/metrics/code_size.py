# metrics/code_size.py
import sys

def analyze_code_size(code_string):
    disk_b = len(code_string.encode('utf-8'))
    ram_b = sys.getsizeof(code_string)
    return {
        "disk_bytes": disk_b,
        "disk_kb": disk_b / 1024,
        "ram_bytes": ram_b,
        "ram_kb": ram_b / 1024
    }

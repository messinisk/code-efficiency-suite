import psutil
import os

def measure_memory(func, *args, **kwargs):
    """
    Μετράει την αύξηση RAM που προκαλεί η εκτέλεση μιας μεθόδου.
    Επιστρέφει bytes.
    """
    process = psutil.Process(os.getpid())

    before = process.memory_info().rss
    func(*args, **kwargs)
    after = process.memory_info().rss

    return after - before

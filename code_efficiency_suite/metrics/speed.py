import time

def measure_speed(func, *args, **kwargs):
    """
    Μετράει τον συνολικό χρόνο εκτέλεσης μιας μεθόδου.
    Επιστρέφει χρόνο σε δευτερόλεπτα (float).
    """
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start


import numpy as np

history: list[float] = []

def regression_point(value):
    history.append(value)

    # Αν έχουμε λιγότερα από 2 σημεία → δεν γίνεται regression
    if len(history) < 2:
        return {
            "slope": 0.0,
            "intercept": history[0],
            "points": history.copy()
        }

    x = np.arange(len(history))
    y = np.array(history)

    try:
        m, b = np.polyfit(x, y, 1)
    except (np.linalg.LinAlgError, ValueError):

        # Fallback σε περίπτωση SVD error
        return {
            "slope": 0.0,
            "intercept": float(y.mean()),
            "points": history.copy()
        }

    return {
        "slope": float(m),
        "intercept": float(b),
        "points": history.copy()
    }

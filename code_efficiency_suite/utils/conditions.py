# utils/conditions.py
from .units import parse_units

def check_condition(value, rule):
    if rule is None:
        return True

    parts = rule.split("|")
    for part in parts:
        part = part.strip()
        op, threshold = part.split(" ", 1)
        threshold = parse_units(threshold)

        if op == ">=" and value >= threshold:
            return True
        if op == "<=" and value <= threshold:
            return True
        if op == "==" and value == threshold:
            return True
        if op == "!=" and value != threshold:
            return True

    return False

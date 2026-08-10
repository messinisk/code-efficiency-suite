def parse_units(value):
    """
    Μετατρέπει τιμές όπως:
    '10KB', '2MB', '1.5GB'
    σε bytes (int).
    
    Αν δεν υπάρχει μονάδα, επιστρέφει float(value).
    """
    value = value.strip().upper()

    units = {
        "KB": 1024,
        "MB": 1024 ** 2,
        "GB": 1024 ** 3,
        "TB": 1024 ** 4,
    }

    for unit, multiplier in units.items():
        if value.endswith(unit):
            number = float(value.replace(unit, "").strip())
            return int(number * multiplier)

    # Χωρίς μονάδα → απλό float
    return float(value)

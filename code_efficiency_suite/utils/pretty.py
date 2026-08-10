def pretty_report(data: dict, method_name: str = "method"):
    print("\n=== Code Efficiency Report ===")
    print(f"Method: {method_name}")
    print("----------------------------------------")

    # Time
    print(f"Time:        {data['time']:.6f} sec")

    # Memory
    mem_kb = data['memory'] / 1024
    print(f"Memory:      {mem_kb:.2f} KB")

    # Object Size
    size_kb = data['size'] / 1024
    print(f"Object Size: {size_kb:.2f} KB")

    # Code Size
    if data.get("code"):
        print("\nCode Size:")
        print(f"  Disk:      {data['code']['disk_bytes']} bytes ({data['code']['disk_kb']:.2f} KB)")
        print(f"  RAM:       {data['code']['ram_bytes']} bytes ({data['code']['ram_kb']:.2f} KB)")

    # System Info
    sys = data["system"]
    print("\nSystem:")
    print(f"  CPU Count:        {sys['cpu_count']}")
    print(f"  Threads:          {sys['threads']}")
    print(f"  Single Thread:    {'Yes' if sys['is_single_thread'] else 'No'}")

    # Regression
    reg = data["regression"]
    print("\nRegression:")
    print(f"  Slope:            {reg['slope']}")
    print(f"  Intercept:        {reg['intercept']}")
    print(f"  Points:           {reg['points']}")

    # Results
    print("\nResults:")
    for key, val in data["results"].items():
        print(f"  {key.capitalize()}:   {'PASS' if val else 'FAIL'}")

    print("----------------------------------------\n")

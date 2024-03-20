for i in range(1, 10):
    if i == 3:
        continue  # Skip number 3
    print(f"Outer loop: {i}")
    for j in range(1, 10):
        if j == 3:
            continue  # Skip number 3
        print(f"Inner loop: {j}")
        if j == 7:
            break  # Break out of the outer loop when reaching 7

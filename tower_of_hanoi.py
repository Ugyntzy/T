def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from rod {source} to rod {target}.")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from rod {source} to rod {target}.")
    tower_of_hanoi(n - 1, auxiliary, source, target)

# Example usage
n = 4
tower_of_hanoi(n, 'A', 'B', 'C')

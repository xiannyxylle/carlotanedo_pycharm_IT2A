def run_array_program():

    max_size = 6
    arr = [None] * max_size
    print(f"Initial Empty Array: {arr}")
    print("-" * 50)


    print("[Phase 1: Insertion / Adding Elements]")
    elements_to_insert = ['T', 'A', 'Ñ', 'E', 'D', 'O']

    for i in range(max_size):
        arr[i] = elements_to_insert[i]
        print(f"Step {i + 1}: Set arr[{i}] = '{arr[i]}' --> Output: {arr}")

    print("Array status: FULL\n")
    print("-" * 50)


    print("[Phase 2: Deletion / Removing Elements]")
    for i in range(max_size - 1, -1, -1):
        removed_val = arr[i]
        arr[i] = None
        step_num = 8 + (max_size - 1 - i)
        print(f"Step {step_num}: Delete arr[{i}] ('{removed_val}') --> Output: {arr}")

    print("Array status: EMPTY (FULL)")


if __name__ == "__main__":
    run_array_program()
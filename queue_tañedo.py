# ALGORITHM: Queue_TAÑEDO
# Dynamic implementation of Queue Enqueue and Dequeue operations using letters: T, A, Ñ, E, D, O

from collections import deque

def run_queue_program():
    queue = deque()
    print(f"Step 1: Initialize queue = [] --> Output: {list(queue)}")
    print("-" * 50)

    # Phase 1: Enqueue / Adding Elements
    print("[Phase 1: Enqueue / Adding Elements]")
    letters = ['T', 'A', 'Ñ', 'E', 'D', 'O']
    for idx, letter in enumerate(letters, start=2):
        queue.append(letter)
        print(f"Step {idx}: Enqueue('{letter}') --> Output: {list(queue)}")

    print("\n" + "-" * 50)

    # Phase 2: Dequeue / Removing Elements
    print("[Phase 2: Dequeue / Removing Elements]")
    for idx in range(8, 14):
        if queue:
            removed = queue.popleft()
            print(f"Step {idx}: Dequeue()  (Removes '{removed}') --> Output: {list(queue)}")

if __name__ == "__main__":
    run_queue_program()
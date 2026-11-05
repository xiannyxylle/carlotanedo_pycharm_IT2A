# ALGORITHM: Stack_TAÑEDO
# Dynamic implementation of Stack Push and Pop operations using letters: T, A, Ñ, E, D, O

def run_stack_program():
    stack = []
    print(f"Step 1: Initialize stack = [] --> Output / Top: {stack}")
    print("-" * 50)

    # Phase 1: Push / Adding Elements
    print("[Phase 1: Push / Adding Elements]")
    letters = ['T', 'A', 'Ñ', 'E', 'D', 'O']
    for idx, letter in enumerate(letters, start=2):
        stack.append(letter)
        print(f"Step {idx}: Push('{letter}') --> Output / Top: {stack}")

    print("\n" + "-" * 50)

    # Phase 2: Pop / Removing Elements
    print("[Phase 2: Pop / Removing Elements]")
    for idx in range(8, 14):
        if stack:
            removed = stack.pop()
            print(f"Step {idx}: Pop()  (Removes '{removed}') --> Output / Top: {stack}")

if __name__ == "__main__":
    run_stack_program()
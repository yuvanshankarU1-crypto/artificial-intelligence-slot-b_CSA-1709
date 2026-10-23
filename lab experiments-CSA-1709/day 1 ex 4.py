import itertools

def solve_cryptarithmetic(formula):
    # Split formula into words
    parts = formula.replace('+', '=').split('=')
    words = [word.strip() for word in parts[:-1]]
    result = parts[-1].strip()
    
    # Extract unique letters
    unique_letters = set(c for word in words + [result] for c in word)
    assert len(unique_letters) <= 10, "Too many letters for digits 0-9"
    
    letters = list(unique_letters)
    first_letters = {word[0] for word in words + [result]}
    
    # Try all permutations of digits for the unique letters
    for perm in itertools.permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        
        # Leading letters cannot be zero
        if any(mapping[char] == 0 for char in first_letters):
            continue
            
        def evaluate(word):
            return sum(mapping[c] * (10 ** i) for i, c in enumerate(reversed(word)))
            
        left_sum = sum(evaluate(w) for w in words)
        right_val = evaluate(result)
        
        if left_sum == right_val:
            return mapping
            
    return None

if __name__ == "__main__":
    puzzle = "SEND + MORE = MONEY"
    print(f"Solving puzzle: {puzzle}")
    solution = solve_cryptarithmetic("SEND+MORE=MONEY")
    if solution:
        print("Letter to Digit Mapping:", solution)
    else:
        print("No solution found.")

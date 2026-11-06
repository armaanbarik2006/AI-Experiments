def objective_function(x):
    # Evaluates f(x) = -4(x - 5)^2 + 100
    return -4 * (x - 5)**2 + 100

def hill_climbing(start, step_size, max_iteration):
    current = start
    current_value = objective_function(current)
    
    for i in range(max_iteration):
        left = current - step_size
        right = current + step_size
        
        left_value = objective_function(left)
        right_value = objective_function(right)
        
        # Check if moving left increases the objective value
        if left_value > current_value:
            current = left
            current_value = left_value
        # Check if moving right increases the objective value
        elif right_value > current_value:
            current = right
            current_value = right_value
        # If neither neighbor is better, a local maximum is reached
        else:
            break
            
    return current, current_value

# User input execution
if __name__ == "__main__":
    start = float(input("Enter the starting value: "))
    step_size = float(input("Enter the step size: "))
    max_iteration = int(input("Enter maximum iterations: "))

    best_position, best_value = hill_climbing(start, step_size, max_iteration)

    print(f"\nBest position = {best_position}")
    print(f"Maximum value = {best_value}")

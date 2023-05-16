# Define the runners' parameters
runners = [
    {'name': 'John', 'speed': 10, 'run_time': 6, 'rest_time': 20},
    {'name': 'James', 'speed': 8, 'run_time': 8, 'rest_time': 25},
    {'name': 'Jenna', 'speed': 12, 'run_time': 5, 'rest_time': 16},
    {'name': 'Josh', 'speed': 7, 'run_time': 7, 'rest_time': 23},
    {'name': 'Jacob', 'speed': 9, 'run_time': 4, 'rest_time': 32},
    {'name': 'Jerry', 'speed': 5, 'run_time': 9, 'rest_time': 18}
]

# Initialize the runners' distances to zero
distances = {runner['name']: 0 for runner in runners}

# Simulate the race for 1234 seconds
for second in range(1, 1235):
    for runner in runners:
        # Calculate the current cycle for the runner
        cycle_length = runner['run_time'] + runner['rest_time']
        current_cycle = (second - 1) // cycle_length + 1
        
        # Determine if the runner is running or resting during this second
        if (second - 1) % cycle_length < runner['run_time']:
            distances[runner['name']] += runner['speed']
            
# Print the final distances for each runner
for name, distance in distances.items():
    print(f'{name}: {distance} meters')

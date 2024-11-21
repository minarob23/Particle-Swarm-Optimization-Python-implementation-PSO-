import numpy as np

def fitness_function(x, powers, coeffs):
    """Calculate the fitness of the particle based on the given powers and coefficients."""
    fitness = sum(coeff * (x[i] ** powers[i]) for i, coeff in enumerate(coeffs))
    return fitness

def pso(num_particles, dimensions, phi1, phi2, iterations, powers, coeffs, x, velocity, p, p_global):
    # Calculate initial fitness for particles and print them
    x_fit = p_best = np.array([fitness_function(x[i], powers, coeffs) for i in range(num_particles)]) # fitness for x
    p_best = np.array([fitness_function(p[i], powers, coeffs) for i in range(num_particles)])  # fitness for personal bests
    g_best = fitness_function(p_global, powers, coeffs)  # global best fitness

    # Print initial fitness
    print("\n")
    print("The initial fitness for particles is:")
    for i in range(num_particles):
        print(f"The fitness for X{i + 1}={x_fit[i]:.6f}")
        print(f"The fitness for PBest{i + 1}={p_best[i]:.6f}")
    print(f"The fitness for gbest={g_best:.6f}\n")

    # PSO loop
    for t in range(iterations):
        print(f"At time t+{t + 1}:")
        
        # Update velocity and position for each particle
        for i in range(num_particles):
            # Update velocity
            velocity[i] = velocity[i] + phi1 * (p[i] - x[i]) + phi2 * (p_global - x[i])
            # Update position
            x[i] = x[i] + velocity[i]
            
            # Calculate fitness for the new position
            fitness = fitness_function(x[i], powers, coeffs)
            
            # Update personal best
            if fitness < p_best[i]:
                p_best[i] = fitness
                p[i] = x[i]
            
        # Update global best
        min_fitness_idx = np.argmin(p_best)
        if p_best[min_fitness_idx] < g_best:
            g_best = p_best[min_fitness_idx]
            p_global = p[min_fitness_idx]

        # Print fitness for each particle and update best positions
        for i in range(num_particles):
            print(f"for point X{i + 1}:\n The velocity V{i + 1} is calculated as v={velocity[i]}")
            print(f" The updated position for X{i + 1} is calculated as x={x[i]}")
            print(f"The fitness for X{i + 1} ={fitness_function(x[i], powers, coeffs):.6f}")
            print(f"The updated PBest for X{i + 1}={p[i]}")
        
        print(f"The updated gBest={p_global}\n")

# Example usage:

# User inputs
num_particles = int(input("Enter the number of particles: "))
dimensions = int(input("Enter the number of dimensions: "))
phi1 = float(input("Enter the value for phi1: "))
phi2 = float(input("Enter the value for phi2: "))
iterations = int(input("Enter the number of iterations: "))

# Input coefficients and powers
coeffs = []
powers = []
for i in range(dimensions):
    coeff = float(input(f"Enter coefficient for x{i + 1}: "))
    power = int(input(f"Enter power for x{i + 1}: "))
    coeffs.append(coeff)
    powers.append(power)

# Input x (positions), velocity, p (personal best positions), and p_global (global best position)
print("Enter the position matrix (x):")
x = np.array([list(map(float, input(f"Enter particle {i + 1} position (space-separated): ").split())) for i in range(num_particles)])

print("Enter the velocity matrix (velocity):")
velocity = np.array([list(map(float, input(f"Enter particle {i + 1} velocity (space-separated): ").split())) for i in range(num_particles)])

print("Enter the personal best positions matrix (p):")
p = np.array([list(map(float, input(f"Enter particle {i + 1} personal best position (space-separated): ").split())) for i in range(num_particles)])

print("Enter the global best position (p_global):")
p_global = list(map(float, input("Enter the global best position (space-separated): ").split()))

# Run PSO with the inputs
pso(num_particles, dimensions, phi1, phi2, iterations, powers, coeffs, x, velocity, p, p_global)

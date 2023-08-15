import numpy as np
import pandas as pd
import gzip
import matplotlib.pyplot as plt

#EUCLIDEAN DISTANCE
def euclidean_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#TOUR DISTANCE
def tour_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(x_cord[tour[i]], y_cord[tour[i]], x_cord[tour[i+1]], y_cord[tour[i+1]])
    total_distance += euclidean_distance(x_cord[tour[-1]], y_cord[tour[-1]], x_cord[tour[0]], y_cord[tour[0]])  # Return to starting point
    return total_distance

#WHALE SWARM ALGORITHM
def initialize_whales(num_whales, num_cities):
    return np.array([np.random.permutation(num_cities) for _ in range(num_whales)])

def whale_swarm_algorithm(num_whales, num_iterations):
    whales = initialize_whales(num_whales, num_cities)
    best_whale = whales[0]
    best_whale_distance = tour_distance(best_whale)

    for _ in range(num_iterations):
        for whale in whales:
            neighbor_whale = whale.copy()
            idx1, idx2 = np.random.choice(num_cities, 2, replace=False)
            neighbor_whale[idx1], neighbor_whale[idx2] = neighbor_whale[idx2], neighbor_whale[idx1]

            neighbor_distance = tour_distance(neighbor_whale)

            if neighbor_distance < best_whale_distance:
                best_whale = neighbor_whale
                best_whale_distance = neighbor_distance
        
        for i in range(len(whales)):
            whales[i] = best_whale.copy()

    return best_whale, best_whale_distance

#OPTIMAL FILE READ
print("OPTIMAL FILE")
opt_data = pd.read_csv('pr76.opt.tour.gz', compression='gzip', header=0, sep=',', quotechar='"')
tour_column_name = opt_data.columns[0]
opt_tour_array = opt_data[opt_data[tour_column_name].astype(str).str.isdigit()][tour_column_name].astype(int).values
opt_tour_array = np.append(opt_tour_array, opt_tour_array[0])
#print("Optimal Tour Path:",opt_tour_array)

#TEST FILE READ
with gzip.open('pr76.tsp.gz', 'rt') as f:
    content = f.read()

node_number = []
x_cord = []
y_cord = []
reading_data = False

lines = content.split('\n')
for line in lines:
    if line.startswith("NODE_COORD_SECTION"):
        reading_data = True
        continue
    if reading_data and line.strip() != "" and not line.startswith("EOF"):
        parts = line.split()
        node_number.append(int(parts[0]))
        x_cord.append(float(parts[1]))
        y_cord.append(float(parts[2]))

node_number = np.array(node_number)
x_cord = np.array(x_cord)
y_cord = np.array(y_cord)

#OPTIMAL DISTANCE RUN
total_distance_optimal = 0
for i in range(len(opt_tour_array) - 1):
    total_distance_optimal += euclidean_distance(x_cord[opt_tour_array[i] - 1], y_cord[opt_tour_array[i] - 1],
                                                 x_cord[opt_tour_array[i + 1] - 1], y_cord[opt_tour_array[i + 1] - 1])

total_distance_optimal += euclidean_distance(x_cord[opt_tour_array[-1] - 1], y_cord[opt_tour_array[-1] - 1],
                                             x_cord[opt_tour_array[0] - 1], y_cord[opt_tour_array[0] - 1])

print("Total Distance of Optimal Path:", total_distance_optimal)

#WHALE SWARM RUN
print()
print("WHALE SWARM")
print()
print("POPULATION 50")
a50 = []
a100 = []
a250 = []
a500 = []
num_cities = len(node_number)
num_iterations = 1000
for i in range(0, 50):
    num_whales = 50
    best_whale, best_distance = whale_swarm_algorithm(num_whales, num_iterations)
    best_whale = np.append(best_whale, best_whale[0])
    best_whale_x = x_cord[best_whale]
    best_whale_y = y_cord[best_whale]
    a50.append(best_distance)

for i in range(0, 50):
    print("Run", i+1, end="")
    print(": ", end="")
    print(a50[i])

print()
print("POPULATION 100")
for i in range(0, 50):
    num_whales = 100
    best_whale, best_distance = whale_swarm_algorithm(num_whales, num_iterations)
    best_whale = np.append(best_whale, best_whale[0])
    best_whale_x = x_cord[best_whale]
    best_whale_y = y_cord[best_whale]
    a100.append(best_distance)

for i in range(0, 50):
    print("Run", i+1, end="")
    print(": ", end="")
    print(a100[i])

print()
print("POPULATION 250")
for i in range(0, 50):
    num_whales = 250
    best_whale, best_distance = whale_swarm_algorithm(num_whales, num_iterations)
    best_whale = np.append(best_whale, best_whale[0])
    best_whale_x = x_cord[best_whale]
    best_whale_y = y_cord[best_whale]
    a250.append(best_distance)

for i in range(0, 50):
    print("Run", i+1, end="")
    print(": ", end="")
    print(a250[i])

print()
print("POPULATION 500")
for i in range(0, 50):
    num_whales = 500
    best_whale, best_distance = whale_swarm_algorithm(num_whales, num_iterations)
    best_whale = np.append(best_whale, best_whale[0])
    best_whale_x = x_cord[best_whale]
    best_whale_y = y_cord[best_whale]
    a500.append(best_distance)

for i in range(0, 50):
    print("Run", i+1, end="")
    print(": ", end="")
    print(a500[i])

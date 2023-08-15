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

#OPTIMAL FILE READ
print("OPTIMAL FILE")
opt_data = pd.read_csv('pr76.opt.tour.gz', compression='gzip', header=0, sep=',', quotechar='"')
tour_column_name = opt_data.columns[0]
opt_tour_array = opt_data[opt_data[tour_column_name].astype(str).str.isdigit()][tour_column_name].astype(int).values

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

#HILL CLIMBING RUN
print()
print("HILL CLIMBING")
best_distanceHC = []
for i in range(0, 50):
    num_cities = len(node_number)
    initial_tour = np.random.permutation(num_cities)

    best_tour = initial_tour
    best_distance = tour_distance(best_tour)
    num_iterations = 1000

    for i in range(num_iterations):
        neighbor_tour = best_tour.copy()
        idx1, idx2 = np.random.choice(num_cities, 2, replace=False)
        neighbor_tour[idx1], neighbor_tour[idx2] = neighbor_tour[idx2], neighbor_tour[idx1]

        neighbor_distance = tour_distance(neighbor_tour)

        if neighbor_distance < best_distance:
            best_tour = neighbor_tour
            best_distance = neighbor_distance

    best_distanceHC.append(best_distance)

for i in range(0, 50):
    print("Run", i+1, end="")
    print(": ", end="")
    print(best_distanceHC[i])
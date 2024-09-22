import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Load the JSON file
with open('../data/building_data.json') as f:
    data = json.load(f)

# Extract gfaUnits data for each floor
floors_urns = [
    "urn:adsk-forma-elements:basicbuilding:pro_2wet97vhty:25hkfvyuu9_0:1726954794039",  # First floor
    "urn:adsk-forma-elements:basicbuilding:pro_2wet97vhty:25hkfvyuu9_1:1726954794039",  # Second floor
    "urn:adsk-forma-elements:basicbuilding:pro_2wet97vhty:25hkfvyuu9_2:1726954794039"   # Third floor
]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Function to plot a floor with its elevation
def plot_floor(floor_data, color):
    gfa_units = floor_data["representations"]["gfaUnits"]["data"]
    
    # Extract the first set of coordinates (assuming there's only one set)
    for area in gfa_units[0]["areas"]:
        coordinates = area["coordinates"][0]  # Extract the coordinates for the polygon
        elevation = area["elevation"]  # Get the elevation

        xs = [coord[0] for coord in coordinates]
        ys = [coord[1] for coord in coordinates]
        zs = [elevation] * len(xs)  # Set z as the elevation for all points

        # Plotting the floor
        ax.plot(xs, ys, zs, color=color)
        ax.add_collection3d(Poly3DCollection([list(zip(xs, ys, zs))], facecolors=color, linewidths=1, edgecolors='r', alpha=0.25))

# Plot each floor with different colors
plot_floor(data["elements"][floors_urns[0]], 'blue')    # First floor
plot_floor(data["elements"][floors_urns[1]], 'green')   # Second floor
plot_floor(data["elements"][floors_urns[2]], 'red')     # Third floor

# Set the labels and title
ax.set_xlabel('X coordinate')
ax.set_ylabel('Y coordinate')
ax.set_zlabel('Elevation (Z)')
ax.set_title('3D Plot of Building Floors')

# Show the plot
plt.show()

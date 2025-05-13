import numpy as np
import matplotlib.pyplot as plt

# Sample grayscale image (5x5)
image = np.array([
    [52, 55, 61, 66, 70],
    [63, 59, 55, 90, 109],
    [85, 104, 117, 123, 136],
    [130, 139, 145, 150, 155],
    [160, 165, 170, 175, 180]
])

# Flatten image to 1D array
flat = image.flatten()

# Define custom bin edges and labels (e.g., 0–9, 10–19, ..., 250–255)
bin_edges = list(range(0, 256, 10)) + [256]
bin_labels = [f"{bin_edges[i]}-{bin_edges[i+1]-1}" for i in range(len(bin_edges)-1)]

# Count frequencies per bin
binned_freq = [0] * len(bin_labels)
for val in flat:
    for i in range(len(bin_edges)-1):
        if bin_edges[i] <= val < bin_edges[i+1]:
            binned_freq[i] += 1
            break

# Plot histogram
plt.figure(figsize=(10, 6))
plt.bar(bin_labels, binned_freq, color='royalblue', edgecolor='black')
plt.title("Histogram of Grayscale Image (Binned)", fontsize=14)
plt.xlabel("Pixel Intensity Range", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

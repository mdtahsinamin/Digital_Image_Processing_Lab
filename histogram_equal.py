import numpy as np
import matplotlib.pyplot as plt

# Step 1: 5x5 grayscale image input
image = np.array([
    [52, 55, 61, 66, 70],
    [63, 59, 55, 90, 109],
    [85, 104, 117, 123, 136],
    [130, 139, 145, 150, 155],
    [160, 165, 170, 175, 180]
])

# Step 2: Flatten and compute original histogram
flat = image.flatten()
hist, _ = np.histogram(flat, bins=256, range=(0, 255))

# Step 3: Compute CDF and equalization map
cdf = hist.cumsum()
cdf_normalized = cdf * 255 / cdf[-1]
cdf_normalized = cdf_normalized.astype('uint8')

# Step 4: Equalize the image
equalized_image = cdf_normalized[flat].reshape(image.shape)
equalized_flat = equalized_image.flatten()

# Step 5: Define bin edges and labels (e.g., 0–9, 10–19, ..., 250–255)
bin_edges = list(range(0, 256, 10)) + [256]
bin_labels = [f"{bin_edges[i]}-{bin_edges[i+1]-1}" for i in range(len(bin_edges)-1)]

# Step 6: Compute frequency for original and equalized images
def compute_custom_hist(flat_data):
    bins = [0] * len(bin_labels)
    for val in flat_data:
        for i in range(len(bin_edges)-1):
            if bin_edges[i] <= val < bin_edges[i+1]:
                bins[i] += 1
                break
    return bins

original_binned = compute_custom_hist(flat)
equalized_binned = compute_custom_hist(equalized_flat)

# Step 7: Plot original and equalized histograms
plt.figure(figsize=(12, 5))

# Original Histogram
plt.subplot(1, 2, 1)
plt.bar(bin_labels, original_binned, color='cornflowerblue', edgecolor='black')
plt.title("Original Image Histogram")
plt.xlabel("Pixel Intensity Range")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Equalized Histogram
plt.subplot(1, 2, 2)
plt.bar(bin_labels, equalized_binned, color='mediumseagreen', edgecolor='black')
plt.title("Equalized Image Histogram")
plt.xlabel("Pixel Intensity Range")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

# Step 8: Show matrices
print("Original Image:\n", image)
print("\nEqualized Image:\n", equalized_image)

import numpy as np
import matplotlib.pyplot as plt
import cv2  # Only for image loading (not used for processing)

# Load image and convert to grayscale manually
image = cv2.imread('./lena.png', cv2.IMREAD_GRAYSCALE)  # Read as grayscale
image = np.array(image, dtype=np.float32)  # Convert to float for calculations

# Define Sobel kernels
Gx_kernel = np.array([[-1, 0, 1], 
                       [-2, 0, 2], 
                       [-1, 0, 1]])

Gy_kernel = np.array([[-1, -2, -1], 
                       [0,  0,  0], 
                       [1,  2,  1]])

# Get image dimensions
rows, cols = image.shape
gradient_x = np.zeros((rows, cols))  # To store Gx result
gradient_y = np.zeros((rows, cols))  # To store Gy result
gradient_magnitude = np.zeros((rows, cols))  # To store final edges

# Apply convolution (ignore edges to avoid boundary issues)
for i in range(1, rows-1):
    for j in range(1, cols-1):
        # Extract 3x3 region
        region = image[i-1:i+2, j-1:j+2]
        
        # Apply Sobel filters
        gx = np.sum(region * Gx_kernel)  # Convolution with Gx
        gy = np.sum(region * Gy_kernel)  # Convolution with Gy
        
        # Store results
        gradient_x[i, j] = gx
        gradient_y[i, j] = gy
        
        # Compute gradient magnitude
        gradient_magnitude[i, j] = np.sqrt(gx**2 + gy**2)

# Normalize output to 0-255 for visualization
gradient_magnitude = (gradient_magnitude / np.max(gradient_magnitude)) * 255

# Display results
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1), plt.imshow(gradient_x, cmap='gray'), plt.title('Sobel X')
plt.subplot(1, 3, 2), plt.imshow(gradient_y, cmap='gray'), plt.title('Sobel Y')
plt.subplot(1, 3, 3), plt.imshow(gradient_magnitude, cmap='gray'), plt.title('Edge Magnitude')
plt.show()

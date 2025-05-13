import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread('./images.jpg', cv2.IMREAD_GRAYSCALE)

# Find the minimum and maximum pixel values in the image
I_min = np.min(image)
I_max = np.max(image)

# Apply histogram stretching
stretched_image = np.uint8(((image - I_min) / (I_max - I_min)) * 255)

# Plot the original and stretched images and their histograms
plt.figure(figsize=(12, 6))

# Original Image
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Stretched Image
plt.subplot(2, 2, 2)
plt.imshow(stretched_image, cmap='gray')
plt.title('Stretched Image')
plt.axis('off')

# Histogram of the original image
plt.subplot(2, 2, 3)
plt.hist(image.ravel(), bins=256, range=(0, 256), color='black')
plt.title('Histogram of Original Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

# Histogram of the stretched image
plt.subplot(2, 2, 4)
plt.hist(stretched_image.ravel(), bins=256, range=(0, 256), color='black')
plt.title('Histogram of Stretched Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = cv2.imread('./lena.png', 0)  # 0 for grayscale

# Simple Gaussian noise
def simple_gaussian_noise(img):
    noise = np.random.normal(0, 20, img.shape)
    noisy = np.clip(img + noise, 0, 255).astype(np.uint8)
    return noisy

# Simple salt & pepper noise
def simple_salt_pepper(img):
    noisy = img.copy()
    # Salt
    num_pixels = int(img.size * 0.01)  # 1% of pixels
    x_coords = np.random.randint(0, img.shape[0], num_pixels)
    y_coords = np.random.randint(0, img.shape[1], num_pixels)
    noisy[x_coords, y_coords] = 255
    
    # Pepper
    x_coords = np.random.randint(0, img.shape[0], num_pixels)
    y_coords = np.random.randint(0, img.shape[1], num_pixels)
    noisy[x_coords, y_coords] = 0
    
    return noisy

# Add noise
gaussian_img = simple_gaussian_noise(img)
sp_img = simple_salt_pepper(img)

# Display results
plt.figure(figsize=(10, 4))
plt.subplot(131), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(132), plt.imshow(gaussian_img, cmap='gray'), plt.title('Gaussian')
plt.subplot(133), plt.imshow(sp_img, cmap='gray'), plt.title('Salt & Pepper')
plt.tight_layout()
plt.show()
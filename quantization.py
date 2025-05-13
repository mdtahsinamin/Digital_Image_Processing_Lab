import cv2
import numpy as np

def generate_mask(bits_to_reduce):
    """
    Generate a bit mask for quantization.
    The first (8 - bits_to_reduce) bits are 1's, and the last bits are 0's.
    """
    return (0xFF >> bits_to_reduce) << bits_to_reduce

# Load a grayscale image
image_path = './lena.png'  # Change this to your image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if image is None:
    print("Error: Could not load image. Check the file path.")
    exit()

# Define how many bits to reduce (change this value)
bits_to_reduce = 4  # Example: Reduce 3 bits (adjust as needed)

# Generate the mask dynamically
mask = generate_mask(bits_to_reduce)
print(f"Generated Mask: {bin(mask)} (Decimal: {mask})")

# Apply the AND operation for quantization
quantized_image = np.bitwise_and(image, mask)

# Display the images
cv2.imshow('Original Image', image)
cv2.imshow(f'Quantized Image (Reduced {bits_to_reduce} bits)', quantized_image)

# Save the quantized image
output_path = 'quantized_image.jpg'
cv2.imwrite(output_path, quantized_image)
print(f"Quantized image saved as: {output_path}")

cv2.waitKey(0)
cv2.destroyAllWindows()

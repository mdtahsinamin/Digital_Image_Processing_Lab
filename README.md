# 📸 Image Processing Algorithms (C++ and Python)

This repository contains various digital image processing algorithms implemented in both **C++** and **Python**, including histogram operations, edge detection, quantization, and filtering.

---

## 📂 Folder Structure

```
├── 2-prewitt.cpp              # Prewitt edge detection (C++)
├── Sobel.cpp                  # Sobel edge detection (C++)
├── sobel.py                   # Sobel edge detection (Python)
├── histogram_equal.py         # Histogram Equalization (Python)
├── histogram_stretching.py    # Histogram Stretching (Python)
├── histogram-stretching.py    # Alternate version of stretching
├── histogram.py               # Custom binned histogram plot (Python)
├── Histogram.cpp              # Histogram computation (C++)
├── quantization.cpp           # Image quantization (C++)
├── quantization.py            # Image quantization (Python)
├── nosie.py                   # Noise simulation (Python)
├── images.jpg                 # Sample image
├── lena.png                   # Classic test image
├── quantized_image.jpg        # Output of quantization
```

---

## 🧠 Features Implemented

- ✅ Histogram Plotting (custom binned)
- ✅ Histogram Equalization
- ✅ Histogram Stretching
- ✅ Quantization (bitmask-based)
- ✅ Noise Addition
- ✅ Sobel Operator (Edge detection)
- ✅ Prewitt Operator
- ✅ Image Visualization and Processing

---

## ▶️ How to Run

### 🐍 Python Scripts

Make sure Python and `matplotlib`, `numpy` are installed.

```bash
pip install matplotlib numpy
python sobel.py
python histogram_equal.py
```

### 💻 C++ Programs

Use a C++ compiler like `g++`:

```bash
g++ Sobel.cpp -o sobel
./sobel
```

---

## 🛠 Requirements

- Python 3.7+
- C++17 compatible compiler (g++, clang)
- Python packages:
  - numpy
  - matplotlib
  - opencv-python (optional for real images)

---

## 🖼 Sample Outputs

- Binned histograms (0–10, 11–20…)
- Enhanced contrast via histogram equalization
- Accurate edge maps using Sobel/Prewitt
- Pixel-level quantization & reduction

---

## 📌 Notes

- You can edit image arrays in `.py` files for custom tests.
- Use `lena.png` or `images.jpg` with OpenCV if you want to test real image behavior.
- All outputs are printed in terminal or plotted via `matplotlib`.

---

## 🙌 Author

Developed for academic purposes and computer vision practice.

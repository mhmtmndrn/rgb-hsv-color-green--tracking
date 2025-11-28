# Real-Time Green Color Tracking

This project detects and tracks green objects in real-time using Python and OpenCV via a webcam. It includes two different approaches for color detection: **HSV** and **BGR**.

## 📂 Files

* **`HSV_colour(green)_tracking.py` (Recommended):** Uses the **HSV** (Hue, Saturation, Value) color space for detection. This method is more robust against lighting changes and shadows, providing more stable results.
* **`RGB_colour(green)_tracking.py`:** Uses the standard **BGR** (Blue, Green, Red) color space. It has a simpler logic but is more sensitive to environmental lighting conditions.

## 🚀 Features

* Real-time video feed from the webcam.
* Color masking to isolate green pixels.
* Contour detection with bounding boxes and "Green" labels drawn around objects.
* Noise filtering: Only tracks objects larger than a specific size (area > 500).
* Live visualization of both the original frame and the binary mask.

## 🛠️ Installation

You need Python installed to run this project. Install the required libraries using pip:

pip install opencv-python numpy
💻 Usage
After downloading the files, open your terminal and run the recommended version with the following command:


python HSV_colour(green)_tracking.py
To try the alternative BGR version:


python RGB_colour(green)_tracking.py
Controls
Quit: Press q on your keyboard to close the windows and stop the program.

⚙️ Settings (Sensitivity)
If the program struggles to detect your green object or detects incorrect objects, you may need to adjust the lower_green and upper_green values in the code according to your room's lighting.

Current HSV Range:

Lower: (35, 80, 80)

Upper: (85, 255, 255)
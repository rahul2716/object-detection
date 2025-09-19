# YOLO Realtime Object Detection

This repository demonstrates how to run **YOLO (You Only Look Once)** for real-time object detection using the [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) library.

## 🚀 Features

* Real-time object detection from webcam (`model(0)`).
* Easy-to-use Ultralytics YOLO interface.
* Custom model loading support.
* Live visualization with bounding boxes.

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/yolo-realtime-detection.git
   cd yolo-realtime-detection
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install ultralytics
   ```

   (Optional) For GPU support, ensure you have **CUDA** installed with the correct PyTorch version.

## 🖥️ Usage

```python
from ultralytics import YOLO

# Load your YOLO model (replace with your trained weights if needed)
model_path = "yolov8n.pt"  # default lightweight YOLOv8 model
model = YOLO(model_path)

# Run real-time detection from webcam
model(0, show=True)
```

### 🎯 Arguments

* `model_path`: Path to YOLO weights (`.pt` file).
* `0`: Use webcam (default camera). You can replace with a video path or image path.
* `show=True`: Displays the live detection window.

## 🛠️ Customization

* **Run on a video file**

  ```python
  model("video.mp4", show=True)
  ```

* **Save results instead of showing**

  ```python
  model(0, save=True)
  ```

* **Use your own trained model**

  ```python
  model = YOLO("runs/detect/train/weights/best.pt")
  ```

## 📷 Example Output

When running the script, you will see bounding boxes around detected objects in real-time, with labels and confidence scores.

---

## 📚 References

* [Ultralytics YOLO Documentation](https://docs.ultralytics.com/)
* [YOLOv8 GitHub Repository](https://github.com/ultralytics/ultralytics)

---

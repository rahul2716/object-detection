from ultralytics import YOLO
model = YOLO("/Users/krahul/Downloads/yolo11n.pt")
model(0, show=True)

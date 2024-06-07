from ultralytics import YOLO

# Load a YOLOv8 model (pre-trained model can be used as a base)
model = YOLO("models/yolov8n.pt")

# Train the model on your dataset
model.train(
    data="data/data.yaml",
    epochs=100,
    imgsz=640,
    project="runs/train",
    name="exp",
)

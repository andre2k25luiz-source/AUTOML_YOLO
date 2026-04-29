from ultralytics import YOLO
import shutil
import os

def train_model(data_path):
    model = YOLO("yolov8n.pt")

    results = model.train(
        data=data_path,
        epochs=30,
        imgsz=640
    )

    # caminho padrão do YOLO
    best_path = "runs/detect/train/weights/best.pt"

    os.makedirs("models", exist_ok=True)
    shutil.copy(best_path, "models/best.pt")
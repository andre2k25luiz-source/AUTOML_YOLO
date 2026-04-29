from ultralytics import YOLO
import os

model = None

def load_model():
    global model
    if model is None:
        if not os.path.exists("models/best.pt"):
            raise Exception("Modelo ainda não treinado!")
        model = YOLO("models/best.pt")
    return model

def predict(image_path):
    model = load_model()
    results = model(image_path)
    return results[0].boxes.data.tolist()
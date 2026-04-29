from flask import Flask, request, jsonify
import os

from generator import generate_dataset
from train import train_model
from predict import predict

app = Flask(__name__)

@app.route("/train", methods=["POST"])
def train():
    file = request.files["image"]

    input_path = "data/input/input.jpg"
    file.save(input_path)

    generate_dataset(
        input_path,
        "data/backgrounds",
        "data/output",
        num_images=200
    )

    # cria data.yaml
    with open("data/output/data.yaml", "w") as f:
        f.write("""
path: data/output
train: images
val: images
names:
  0: objeto
""")

    train_model("data/output/data.yaml")

    return jsonify({"status": "modelo treinado"})

@app.route("/predict", methods=["POST"])
def do_predict():
    try:
        file = request.files["image"]
        path = "temp.jpg"
        file.save(path)

        preds = predict(path)
        return jsonify(preds)

    except Exception as e:
        return jsonify({"erro": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
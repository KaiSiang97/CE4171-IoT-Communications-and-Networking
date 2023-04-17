from werkzeug.utils import secure_filename
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from keras import models
# TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

from flask import Flask, request, make_response

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = models.load_model("keras_Model.h5", compile=False)

# Note Classification
note_classes = ['$2', '$5', '$10', '$50']

def predict(pillow_image_path):
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(pillow_image_path).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    a = np.argmax(prediction)
    return note_classes[prediction.argmax()]

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        f = request.files['file']
        f.save(secure_filename(f.filename))
        print('file uploaded successfully')
        pillow_image_path = (os.path.realpath(f.filename))
        prediction = predict(pillow_image_path)
        print(str(prediction))
        os.remove(pillow_image_path)
    response = make_response(prediction, 200)
    response.mimetype = "text/plain"
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

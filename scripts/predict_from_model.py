import joblib
import numpy as np
import os
import sys

# Resolve model path from project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "svm_iris_model.pkl")

# Load the model
model = joblib.load(model_path)

# Expecting 4 inputs: sepal length, sepal width, petal length, petal width
if len(sys.argv) != 5:
    print("Usage: python3 predict_from_model.py <sepal_length> <sepal_width> <petal_length> <petal_width>")
    sys.exit(1)

# Parse inputs from command-line arguments
try:
    sample = np.array([[float(x) for x in sys.argv[1:5]]])
except ValueError:
    print("Error: All inputs must be numeric.")
    sys.exit(1)

# Predict
prediction = model.predict(sample)
print("Predicted Species:", prediction[0])


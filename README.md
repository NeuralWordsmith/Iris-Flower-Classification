# Iris Flower Classification

This project builds and compares three machine learning models to classify Iris flower species using scikit-learn:

- Decision Tree
- Random Forest
- Support Vector Machine (SVM)

The dataset used is the classic Iris dataset, containing 150 samples of 3 flower species: Setosa, Versicolor, and Virginica.

## Project Structure

```
iris-flower-classification/
├── data/                  # (empty - dataset loaded from scikit-learn)
├── models/                # Contains saved SVM model
├── notebooks/             # Data exploration and model training notebooks
├── scripts/               # CLI script to load model and predict
├── results/               # (empty - can be used for plots if needed later)
├── main.py                # (Optional) Entry script placeholder
└── README.md              # Project documentation
```

## Features

- Loads and visualizes the Iris dataset
- Trains three classifiers and evaluates accuracy
- Displays confusion matrices for model comparison
- Saves the best-performing model (SVM)
- Provides a CLI script for predictions on custom input

## Usage

### 1. Clone the repository

```
git clone https://github.com/yourusername/iris-flower-classification.git
cd iris-flower-classification
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

Or install manually:

```
pip install numpy pandas matplotlib seaborn scikit-learn joblib
```

### 3. Run the prediction script

```
python3 scripts/predict_from_model.py <sepal_length> <sepal_width> <petal_length> <petal_width>
```

Example:

```
python3 scripts/predict_from_model.py 6.1 2.8 4.7 1.2
Predicted Species: versicolor
```

## Model Performance

| Model         | Accuracy |
| ------------- | -------- |
| Decision Tree | 93.33%   |
| Random Forest | 90.00%   |
| SVM           | 96.67%   |

The SVM model achieved the best results and is saved in the models/ directory.

## References

- Scikit-learn Documentation: [https://scikit-learn.org/](https://scikit-learn.org/)
- Iris Dataset UCI Repository: [https://archive.ics.uci.edu/ml/datasets/iris](https://archive.ics.uci.edu/ml/datasets/iris)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def train_and_save_model():
    # 1. Load the Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # 2. Split into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3. Train Logistic Regression model
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # 4. Save the trained model
    joblib.dump(model, "iris_logreg.joblib")
    print("Model saved to iris_logreg.joblib")


def load_and_test_model():
    # 5. Load the saved model
    loaded_model = joblib.load("iris_logreg.joblib")
    print("Model loaded from iris_logreg.joblib")

    # 6. Make a prediction
    # Let's predict the class of a single sample
    sample = np.array([[5.9, 3.0, 5.1, 1.8]])
    prediction = loaded_model.predict(sample)
    print(f"Predicted class for sample {sample}: {prediction}")


if __name__ == "__main__":
    train_and_save_model()
    load_and_test_model()

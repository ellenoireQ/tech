import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_model(d: dict):
    # 1. Load the dataset
    # -------
    # We first load the data
    df = pd.DataFrame(d["data"])

    # 2. Prepare variables learning.
    # -------
    # # In this step we prepare the feature variables that will be used to train the model.
    # From dataset, we need:
    #   - jumlah_penjualan
    #   - harga
    #   - diskon
    # These column will be used as input features for the machine learning model.
    X = df[["jumlah_penjualan", "harga", "diskon"]]

    # 3. Set target variables.
    # -------
    # Meaning is model will targeting the target variable that the model will predict.
    y = df["status"]

    # 4. Split dataset into training and testing
    # -------
    # 80% of the data will be used for training
    # 20% of the data will be used for testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 5. Train the model
    # -------
    # We training the model after splitting the dataset
    model = LogisticRegression(max_iter=1000, random_state=14)
    model.fit(X_train, y_train)

    # 6. Make predictions using the test dataset
    # -------
    predict = model.predict(X_test)

    # 7. Evaluate model performance
    # -------
    accuracy = accuracy_score(y_test, predict)

    print(f"model accuracy score: {accuracy * 100}%")
    print(f"model prediction: {list(predict)}")
    print(f"actuals answer : {list(y_test)}")

    # 8. Dump the model
    # -------
    # Dump the model after learning
    joblib.dump(model, "model.pkl")

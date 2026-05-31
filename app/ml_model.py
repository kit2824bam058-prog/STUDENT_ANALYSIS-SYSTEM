from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    r2_score
)

import pandas as pd
import joblib


def train_model(df):

    X = df[
        [
            "math score",
            "reading score"
        ]
    ]

    Y = df["writing score"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()

    model.fit(
        X_train,
        Y_train
    )

    # Save trained model
    joblib.dump(
        model,
        "student_model.pkl"
    )

    predictions = model.predict(
        X_test
    )

    mae = mean_absolute_error(
        Y_test,
        predictions
    )

    r2 = r2_score(
        Y_test,
        predictions
    )

    return (
        model,
        predictions,
        Y_test,
        mae,
        r2
    )


def load_saved_model():

    model = joblib.load(
        "student_model.pkl"
    )

    return model


def custom_prediction(
    model,
    math_mark,
    reading_mark
):

    input_data = pd.DataFrame({
        "math score": [math_mark],
        "reading score": [reading_mark]
    })

    prediction = model.predict(
        input_data
    )

    return prediction[0]
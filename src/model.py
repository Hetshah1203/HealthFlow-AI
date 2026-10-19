# Model utilities for HealthFlow-AI

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from typing import Any

# Global model placeholder (in a real app you'd manage state more cleanly)
_model: Any = None

def _build_pipeline(model_type: str) -> Pipeline:
    """Create a scikit‑learn pipeline for the requested model type.
    Supports "random_forest" and "logistic_regression".
    """
    if model_type == "random_forest":
        estimator = RandomForestClassifier(n_estimators=100, random_state=42)
    elif model_type == "logistic_regression":
        estimator = LogisticRegression(max_iter=1000)
    else:
        raise ValueError(f"Unsupported model_type: {model_type}")
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("estimator", estimator),
    ])
    return pipeline

def train_model(df: pd.DataFrame, model_type: str = "random_forest") -> Any:
    """Fit a model on the provided pre‑processed DataFrame.

    The convention is that the last column is the target label.
    """
    global _model
    if df.shape[1] < 2:
        raise ValueError("DataFrame must contain at least one feature column and one target column")
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    pipeline = _build_pipeline(model_type)
    pipeline.fit(X, y)
    _model = pipeline
    return pipeline

def predict(features: list) -> Any:
    """Return a prediction for a single feature vector.

    The model must have been trained previously via ``train_model``.
    """
    if _model is None:
        raise RuntimeError("Model has not been trained yet")
    import numpy as np
    arr = np.array(features).reshape(1, -1)
    return _model.predict(arr).tolist()[0]

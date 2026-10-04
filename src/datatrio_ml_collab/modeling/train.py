from pathlib import Path

import joblib
import pandas as pd
import yaml
from loguru import logger
import typer

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from datatrio_ml_collab.config import MODELS_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    features_path: Path = PROCESSED_DATA_DIR / "features.csv",
    labels_path: Path = PROCESSED_DATA_DIR / "labels.csv",
    model_path: Path = MODELS_DIR / "model.pkl",
):
    logger.info("Loading features and labels...")

    X = pd.read_csv(features_path)
    y = pd.read_csv(labels_path).iloc[:, 0]

    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)

    train_params = params["train"]

    logger.info(f"Features: {X.shape}")
    logger.info(f"Labels: {y.shape}")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    logger.info("Training Random Forest model...")

    model = RandomForestClassifier(
        n_estimators=train_params["n_estimators"],
        max_depth=train_params["max_depth"],
        random_state=42,
        n_jobs=-1,
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    logger.success(f"Model accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)

    logger.success(f"Model saved to {model_path}")


if __name__ == "__main__":
    app()

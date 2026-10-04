from pathlib import Path

import joblib
import pandas as pd
from loguru import logger
import typer

from datatrio_ml_collab.config import MODELS_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    features_path: Path = PROCESSED_DATA_DIR / "features.csv",
    model_path: Path = MODELS_DIR / "model.pkl",
    predictions_path: Path = PROCESSED_DATA_DIR / "predictions.csv",
):
    logger.info("Loading features...")
    X = pd.read_csv(features_path)

    logger.info("Loading trained model...")
    model = joblib.load(model_path)

    logger.info("Generating predictions...")
    predictions = model.predict(X)

    predictions_df = pd.DataFrame({"prediction": predictions})
    predictions_df.to_csv(predictions_path, index=False)

    logger.success(f"Predictions saved to {predictions_path}")
    logger.info(f"Total predictions: {len(predictions)}")


if __name__ == "__main__":
    app()
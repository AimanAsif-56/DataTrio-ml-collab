from pathlib import Path

import pandas as pd
from loguru import logger
import typer

from datatrio_ml_collab.config import PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    input_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    features_path: Path = PROCESSED_DATA_DIR / "features.csv",
    labels_path: Path = PROCESSED_DATA_DIR / "labels.csv",
):
    logger.info("Generating features from dataset...")

    df = pd.read_csv(input_path)

    X = df.drop(columns=["label"])
    y = df["label"]

    categorical_columns = ["protocol_type", "service", "flag"]

    X = pd.get_dummies(
        X,
        columns=categorical_columns,
        dtype=int,
    )

    X.to_csv(features_path, index=False)
    y.to_csv(labels_path, index=False)

    logger.success(f"Features saved to {features_path}")
    logger.success(f"Labels saved to {labels_path}")
    logger.info(f"Feature shape: {X.shape}")


if __name__ == "__main__":
    app()
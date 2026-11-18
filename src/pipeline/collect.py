"""Collect the Breast Cancer Wisconsin dataset as a CSV.

The ``diagnosis`` target keeps scikit-learn's encoding: 0 is malignant and
1 is benign.
"""

from pathlib import Path

import pandas as pd
from sklearn.datasets import load_breast_cancer


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATASET_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "breast_cancer.csv"
)


def load_dataset() -> pd.DataFrame:
    """Load the built-in dataset and rename its target column to diagnosis."""
    dataset = load_breast_cancer(as_frame=True)
    frame = dataset.frame.copy()
    if "target" not in frame.columns:
        raise ValueError("Expected the scikit-learn dataset to include a target column.")
    return frame.rename(columns={"target": "diagnosis"})


def save_dataset(output_path: Path = DATASET_PATH) -> pd.DataFrame:
    """Save the dataset as a CSV without a pandas index column."""
    frame = load_dataset()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output_path, index=False)
    return frame


def main() -> None:
    """Create the raw dataset CSV and report its dimensions."""
    frame = save_dataset()
    feature_count = len(frame.columns) - 1
    print(
        f"Saved {len(frame)} rows and {feature_count} features to "
        f"{DATASET_PATH.relative_to(PROJECT_ROOT).as_posix()}"
    )


if __name__ == "__main__":
    main()

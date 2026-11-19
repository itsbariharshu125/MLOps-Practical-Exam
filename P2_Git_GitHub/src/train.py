"""Train and evaluate a Random Forest on the Phase 1 breast cancer dataset."""

from dataclasses import dataclass
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from numpy.typing import NDArray
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
DATASET_PATH = REPOSITORY_ROOT / "data" / "raw" / "breast_cancer.csv"
MODEL_PATH = (
    Path(__file__).resolve().parents[1]
    / "models"
    / "breast_cancer_random_forest.joblib"
)
TARGET_COLUMN = "diagnosis"


@dataclass(frozen=True)
class TrainingResult:
    """Evaluation results and sample counts from one training run."""

    accuracy: float
    report: str
    confusion_matrix: NDArray[np.int64]
    train_size: int
    test_size: int


def train_and_evaluate(
    dataset_path: Path = DATASET_PATH,
    model_path: Path = MODEL_PATH,
) -> TrainingResult:
    """Train, evaluate, and save the classifier using a stratified split."""
    data = pd.read_csv(dataset_path)
    if TARGET_COLUMN not in data.columns:
        raise ValueError(f"Dataset must contain a {TARGET_COLUMN!r} target column.")

    features = data.drop(columns=[TARGET_COLUMN])
    target = data[TARGET_COLUMN]
    x_train, x_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=0.2,
        random_state=42,
        stratify=target,
    )

    model = RandomForestClassifier(random_state=42)
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    report = classification_report(
        y_test,
        predictions,
        labels=[0, 1],
        target_names=["malignant (0)", "benign (1)"],
        zero_division=0,
    )
    matrix = confusion_matrix(y_test, predictions, labels=[0, 1])
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)

    return TrainingResult(
        accuracy=accuracy_score(y_test, predictions),
        report=report,
        confusion_matrix=matrix,
        train_size=len(x_train),
        test_size=len(x_test),
    )


def main() -> None:
    """Run training and print the evaluation metrics."""
    result = train_and_evaluate()
    print(f"Accuracy: {result.accuracy:.4f}")
    print("\nClassification report:")
    print(result.report)
    print("Confusion matrix (rows=true, columns=predicted; labels=0, 1):")
    print(result.confusion_matrix)
    print(f"Model saved to {MODEL_PATH.relative_to(REPOSITORY_ROOT).as_posix()}")


if __name__ == "__main__":
    main()

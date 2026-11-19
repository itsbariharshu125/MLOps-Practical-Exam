from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import pytest
from sklearn.ensemble import RandomForestClassifier

from P2_Git_GitHub.src.train import (
    DATASET_PATH,
    TARGET_COLUMN,
    TrainingResult,
    train_and_evaluate,
)


@pytest.fixture(scope="module")
def trained_artifact(
    tmp_path_factory: pytest.TempPathFactory,
) -> tuple[TrainingResult, Path]:
    model_path = tmp_path_factory.mktemp("models") / "breast_cancer.joblib"
    result = train_and_evaluate(model_path=model_path)
    return result, model_path


def test_training_uses_stratified_split_and_reports_metrics(
    trained_artifact: tuple[TrainingResult, Path],
) -> None:
    result, _ = trained_artifact

    assert result.train_size == 455
    assert result.test_size == 114
    assert result.train_size + result.test_size == 569
    assert 0.0 <= result.accuracy <= 1.0
    assert "precision" in result.report
    assert "malignant (0)" in result.report
    assert "benign (1)" in result.report
    assert result.confusion_matrix.shape == (2, 2)
    np.testing.assert_array_equal(
        result.confusion_matrix.sum(axis=1),
        np.array([42, 72]),
    )


def test_saved_model_loads_and_predicts(
    trained_artifact: tuple[TrainingResult, Path],
) -> None:
    _, model_path = trained_artifact

    assert model_path.is_file()
    model = joblib.load(model_path)
    assert isinstance(model, RandomForestClassifier)

    features = pd.read_csv(DATASET_PATH).drop(columns=[TARGET_COLUMN])
    predictions = model.predict(features)
    assert predictions.shape == (569,)

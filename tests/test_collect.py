import pandas as pd
from sklearn.datasets import load_breast_cancer

from src.pipeline.collect import load_dataset, save_dataset


def test_load_dataset_renames_target_and_preserves_encoding() -> None:
    source = load_breast_cancer(as_frame=True)
    frame = load_dataset()

    assert frame.shape == (569, 31)
    assert frame.columns[-1] == "diagnosis"
    assert frame["diagnosis"].equals(source.frame["target"])
    assert set(frame["diagnosis"].unique()) == {0, 1}


def test_save_dataset_writes_csv_without_an_index(tmp_path) -> None:
    output_path = tmp_path / "nested" / "breast_cancer.csv"

    frame = save_dataset(output_path)
    saved_frame = pd.read_csv(output_path)

    assert output_path.is_file()
    assert saved_frame.shape == frame.shape
    assert list(saved_frame.columns) == list(frame.columns)

# Practical 2: Git and GitHub

This practical adds a baseline Random Forest classifier using the Breast
Cancer Wisconsin dataset collected in Phase 1.

## Dataset

The workflow reads `data/raw/breast_cancer.csv` from the repository root. It
expects 30 numeric feature columns and a `diagnosis` target column (`0` =
malignant, `1` = benign). The original dataset is not modified.

## Run the workflow

From the repository root, run:

```powershell
python P2_Git_GitHub/src/train.py
```

The script uses an 80/20 stratified train/test split with `random_state=42`,
trains a `RandomForestClassifier`, and prints accuracy, a classification
report, and a confusion matrix. It saves the trained model to
`P2_Git_GitHub/models/breast_cancer_random_forest.joblib`.

## Run the tests

From the repository root:

```powershell
python -m pytest P2_Git_GitHub/tests
```

The tests check the split and evaluation results and verify that the saved
model can be loaded and used for prediction.

## Git and GitHub workflow

See [docs/GIT_WORKFLOW.md](docs/GIT_WORKFLOW.md) for the Practical 2 Git and
GitHub collaboration workflow.

# MLOps Practical Exam

A shared, reproducible foundation for the MLOps practical exam using the
Breast Cancer Wisconsin Diagnostic dataset. The repository will support
Practicals 2–6 while keeping their implementations for the exam exercises.

## Project overview

Phase 1 establishes the common environment, dataset, documentation, and test
baseline. Each team member can create the same Python environment, collect the
same dataset, and verify the setup before beginning a practical.

The Practical 2–6 directories are structure only at this stage. Their
practical-specific implementations, configurations, and workflows are not
included yet.

## Dataset

The project uses the Breast Cancer Wisconsin Diagnostic dataset bundled with
scikit-learn, loaded with `sklearn.datasets.load_breast_cancer(as_frame=True)`.
It contains 569 observations and 30 numeric input features. The label is named
`diagnosis` in the project CSV:

- `0` = malignant
- `1` = benign

The script writes the real dataset to `data/raw/breast_cancer.csv`; it does not
generate synthetic data. See [DATA_DICTIONARY.md](DATA_DICTIONARY.md) for the
feature list and encoding details.

## Practical scope

| Practical | Planned topic | Phase 1 status |
| --- | --- | --- |
| Practical 2 | Git version control and collaboration | Directory only |
| Practical 3 | DVC data and artifact versioning | Directory only |
| Practical 4 | Reproducible ML pipeline | Directory only |
| Practical 5 | Feast feature store | Directory only |
| Practical 6 | MLflow experiment tracking | Directory only |

## Team workflow

1. Use the same Python 3.14 environment and install the pinned dependencies.
2. Generate and test the shared dataset foundation before starting practical work.
3. Coordinate practical ownership and agree on shared paths and interfaces before
   working in parallel.
4. Use a separate Git branch for each task, review changes with the team, and
   merge only after the relevant checks pass.
5. Keep practical-specific changes in their matching `practicalN_*` directory
   unless the team agrees they belong in a shared component.

## Setup

Run these commands from the repository root. Python 3.14 is the environment
used to check the pinned dependency set.

### Create and activate a virtual environment

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Command Prompt:

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

macOS or Linux:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```sh
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The requirements use one compatible environment for the common Python tools,
DVC, Feast, and MLflow. The package versions were checked together with Python
3.14.3; see `requirements.txt` for the compatibility rationale.

### Prepare and test the dataset

```sh
python src/pipeline/collect.py
python -m pytest
```

The first command creates `data/raw/` if needed and writes the CSV. The second
runs the focused dataset-loading and CSV-output tests.

## Repository layout

```text
docs/practical-guides/   Guides for practical exercises
data/raw/                Collected source dataset
data/processed/          Reserved for later processed data
src/pipeline/            Shared pipeline foundation
practical2_git/          Practical 2 workspace
practical3_dvc/          Practical 3 workspace
practical4_pipeline/     Practical 4 workspace
practical5_feast/        Practical 5 workspace
practical6_mlflow/       Practical 6 workspace
models/                  Reserved for model artifacts
reports/                 Reserved for generated reports
tests/                   Automated tests
```

Git does not store empty directories; the empty practical and reserved folders
will appear in Git as files are added to them.

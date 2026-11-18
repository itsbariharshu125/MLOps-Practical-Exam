# Breast Cancer Wisconsin Diagnostic Data Dictionary

## Source and shape

The data comes from scikit-learn's built-in Breast Cancer Wisconsin Diagnostic
dataset, loaded with `sklearn.datasets.load_breast_cancer(as_frame=True)`.

- **Rows:** 569 observations
- **Input features:** 30 numeric measurements
- **Target column:** `diagnosis`
- **CSV path:** `data/raw/breast_cancer.csv`
- **CSV columns:** the 30 features below, followed by `diagnosis`

## Target encoding

The scikit-learn dataset's numeric target is retained and renamed from `target`
to `diagnosis`:

| Value | Diagnosis |
| --- | --- |
| `0` | Malignant |
| `1` | Benign |

The values are class labels, not probabilities. The collector does not invert
or otherwise recode them.

## Feature columns

Each feature is a numeric measurement computed from a digitized image of a
fine-needle aspirate of a breast mass. The three feature groups are:

- **Mean:** mean value for the measurement.
- **Error:** standard error for the measurement.
- **Worst:** mean of the three largest values for the measurement.

| Measurement | Mean column | Error column | Worst column |
| --- | --- | --- | --- |
| Radius | `mean radius` | `radius error` | `worst radius` |
| Texture | `mean texture` | `texture error` | `worst texture` |
| Perimeter | `mean perimeter` | `perimeter error` | `worst perimeter` |
| Area | `mean area` | `area error` | `worst area` |
| Smoothness | `mean smoothness` | `smoothness error` | `worst smoothness` |
| Compactness | `mean compactness` | `compactness error` | `worst compactness` |
| Concavity | `mean concavity` | `concavity error` | `worst concavity` |
| Concave points | `mean concave points` | `concave points error` | `worst concave points` |
| Symmetry | `mean symmetry` | `symmetry error` | `worst symmetry` |
| Fractal dimension | `mean fractal dimension` | `fractal dimension error` | `worst fractal dimension` |

There are ten measurements in each of the three groups, for 30 input feature
columns total. The dataset does not include patient identifiers in this
project's exported table.

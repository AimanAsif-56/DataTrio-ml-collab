# DataTrio-ml-collab

Git-based collaborative machine learning project developed for the
Git-Based Collaboration for an ML Project assignment.

The project demonstrates collaborative Git workflows, reproducible machine
learning experiments, data/model versioning, automated quality checks, and
continuous integration.

## Dataset

### KDD Cup 10% Dataset

This project uses the **KDD Cup 10% dataset**, a network intrusion detection
dataset derived from the KDD Cup 1999 dataset.

The dataset is used to develop a binary classification model that distinguishes
normal network connections from attack connections.

The dataset was approved for use in this project by the course instructor.

> The raw dataset will be managed using DVC rather than committed directly to
> the Git repository.

## Team

| Member | Role |
|---|---|
| Aiman | Platform Owner |
| Arooj | Data Owner |
| Rabia | Model Owner |

## Project Structure

```text
DataTrio-ml-collab/
├── .github/
│   └── workflows/          # GitHub Actions workflows
├── configs/                # Project configuration
├── data/                   # Dataset files (managed with DVC)
├── models/                 # Trained models
├── notebooks/              # Jupyter notebooks
├── reports/                # Generated reports and figures
├── src/
│   └── datatrio_ml_collab/ # Project source code
├── tests/                  # Automated tests
├── .gitignore              # Files excluded from Git
├── CONTRIBUTING.md         # Contribution and Git workflow rules
├── pyproject.toml          # Python project and tool configuration
├── README.md               # Project documentation
└── uv.lock                 # Locked Python dependencies
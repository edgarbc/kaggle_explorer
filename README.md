# Kaggle Data Explorer 🧭

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Built with uv](https://img.shields.io/badge/Built%20with-uv-%23f7df1e)](https://github.com/astral-sh/uv)

A lightweight CLI utility to search, access, and extract datasets from Kaggle.  
Originally developed as part of an AI Bootcamp project, **Kaggle Data Explorer** supports dataset construction for machine learning tasks—including training models for **Tiler**, an AI-powered Medium title quality predictor.

---

## 🚀 Features

- 🔍 Search Kaggle datasets and competitions programmatically
- ⬇️ Download datasets with a single command
- 📁 Automatically unpack and organize data
- 📦 Built using [`uv`](https://github.com/astral-sh/uv) for fast, modern Python dependency management

---
## Repo structure

```
kaggle-data-explorer/
│
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
├── datasets.yaml               # optional config for batch mode
│
├── download.py                 # simple CLI utility script
│
├── src/                        # source code and modules
│   └── kaggle_explorer/        # actual Python package namespace
│       ├── __init__.py
│       └── downloader.py       # logic to handle API calls
│
├── data/                       # default download folder (can be gitignored)
│
└── tests/                      # future unit tests (optional)
    └── test_downloader.py
```
---

## 📂 Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/kaggle-data-explorer.git
cd kaggle-data-explorer
```

### 2. Install Dependencies

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # on Windows, use `.venv\Scripts\activate`

# Install dependencies
uv pip install --editable ".[dev]"
```

### 3. Configure Kaggle API

Create a `.env` file in the project root with your Kaggle credentials:

```bash
KAGGLE_USERNAME=your_kaggle_username
KAGGLE_KEY=your_kaggle_api_key
```

## 🛠️ Usage

### Command Line Interface

The package provides a CLI for easy dataset downloads:

```bash
# Download competition datasets
python -m src.cli --type competition --name titanic --output data/raw

# Download regular datasets
python -m src.cli --type dataset --name owner/dataset-name --output data/raw
```

Options:
- `--type`: Type of download (`competition` or `dataset`)
- `--name`: For competitions, use the competition name. For datasets, use `owner/dataset-name` format
- `--output`: Directory where to save the dataset
- `--no-unzip`: Optional flag to keep the downloaded files zipped

### Python API

You can also use the package programmatically:

```python
from kaggle_utils.config import load_config
from kaggle_utils.downloader import download_competition_dataset

# Load environment variables
load_config()

# Download a competition dataset
download_competition_dataset("titanic", "data/raw")
```

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
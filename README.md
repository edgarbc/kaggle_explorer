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

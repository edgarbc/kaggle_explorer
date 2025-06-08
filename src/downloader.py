# src/kaggle_explorer/downloader.py

from kaggle.api.kaggle_api_extended import KaggleApi


def download_dataset(slug: str, output_path: str):
    api = KaggleApi()
    api.authenticate()

    print(f"Downloading dataset: {slug}")
    api.dataset_download_files(
        dataset=slug,
        path=output_path,
        unzip=True
    )
    print(f"Dataset downloaded and extracted to: {output_path}")
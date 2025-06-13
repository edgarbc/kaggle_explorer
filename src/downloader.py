# src/kaggle_explorer/downloader.py
"""Module for handling Kaggle dataset downloads."""
from pathlib import Path
import os
from typing import Optional
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile



def download_competition_dataset(
    competition_name: str,
    output_path: str
) -> Path:
    """
    Download a competition dataset from Kaggle.
    
    Args:
        competition_name: Name of the Kaggle competition
        output_path: Path where to save the dataset
        
    Returns:
        Path: Path where the dataset was saved
    """
    # Get project root and construct full path
    project_root = Path(__file__).parent.parent
    full_output_path = project_root / output_path
    
    # Create directory
    full_output_path.mkdir(parents=True, exist_ok=True)
    
    # Initialize and authenticate API
    api = KaggleApi()
    api.authenticate()
    
    print(f"Downloading competition dataset: {competition_name}")
    api.competition_download_files(
        competition=competition_name,
        path=str(full_output_path),
        quiet=False
    )
    print(f"Dataset downloaded to: {full_output_path}")

    # Get the zip file path
    zip_path = full_output_path / f"{competition_name}.zip"

    print(f"Zip file path: {zip_path}")

    # Check if the zip file exists
    if not zip_path.exists():
        print(f"Zip file {zip_path} does not exist")
        return full_output_path

    # Unzip the downloaded file
    if zip_path.exists():
        print(f"Unzipping {zip_path}")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(full_output_path)
        # Optionally remove the zip file after extraction
        zip_path.unlink()
    
    
    return full_output_path

def download_dataset(
    owner: str,
    dataset_name: str,
    output_path: str,
    unzip: bool = True
) -> Path:
    """
    Download a regular dataset from Kaggle.
    
    Args:
        owner: Dataset owner username
        dataset_name: Name of the dataset
        output_path: Path where to save the dataset
        unzip: Whether to unzip the downloaded files
        
    Returns:
        Path: Path where the dataset was saved
    """
    output_path = Path(output_path)
    output_path.mkdir(parents=True, exist_ok=True)
    
    api = KaggleApi()
    api.authenticate()
    
    dataset_path = f"{owner}/{dataset_name}"
    api.dataset_download_files(
        dataset=dataset_path,
        path=str(output_path),
        unzip=unzip
    )
    
    return output_path
# src/kaggle_explorer/downloader.py
"""Module for handling Kaggle dataset downloads."""
from pathlib import Path
import os
from typing import Optional
from kaggle.api.kaggle_api_extended import KaggleApi

def download_competition_dataset(
    competition_name: str,
    output_path: str,
    unzip: bool = True
) -> Path:
    """
    Download a competition dataset from Kaggle.
    
    Args:
        competition_name: Name of the Kaggle competition
        output_path: Path where to save the dataset
        unzip: Whether to unzip the downloaded files
        
    Returns:
        Path: Path where the dataset was saved
    """
    output_path = Path(output_path)
    output_path.mkdir(parents=True, exist_ok=True)
    
    api = KaggleApi()
    api.authenticate()
    
    api.competition_download_files(
        competition=competition_name,
        path=str(output_path),
        quiet=False,
        unzip=unzip
    )
    
    return output_path

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
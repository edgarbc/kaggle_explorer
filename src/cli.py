"""Command-line interface for Kaggle dataset operations."""
import argparse
from pathlib import Path
from utils.config import load_config
from downloader import download_competition_dataset, download_dataset

def main():
    parser = argparse.ArgumentParser(description='Download Kaggle datasets')
    parser.add_argument('--type', choices=['competition', 'dataset'], required=True,
                       help='Type of download: competition or dataset')
    parser.add_argument('--name', required=True,
                       help='Competition name or dataset path (owner/dataset-name)')
    parser.add_argument('--output', required=True,
                       help='Output directory path')
    parser.add_argument('--no-unzip', action='store_true',
                       help='Do not unzip the downloaded files')
    
    args = parser.parse_args()
    
    # Load environment variables
    load_config()
    
    if args.type == 'competition':
        download_competition_dataset(
            competition_name=args.name,
            output_path=args.output
        )
    else:
        owner, dataset_name = args.name.split('/')
        download_dataset(
            owner=owner,
            dataset_name=dataset_name,
            output_path=args.output,
            unzip=not args.no_unzip
        )

if __name__ == '__main__':
    main()
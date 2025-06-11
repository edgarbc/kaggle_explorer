"""Configuration handling for Kaggle utilities."""
from pathlib import Path
from dotenv import load_dotenv
import os

def load_config() -> None:
    """Load environment variables from .env file."""
    # Find the project root (where .env is located)
    project_root = Path(__file__).parent.parent.parent
    env_path = project_root / '.env'
    
    load_dotenv(env_path)
    
    # Validate required environment variables
    required_vars = ['KAGGLE_USERNAME', 'KAGGLE_KEY']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing_vars)}"
        )
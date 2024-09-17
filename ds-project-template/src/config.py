from pathlib import Path
from dotenv import load_dotenv
import logging

# Load environment variables from .env file if it exists
load_dotenv()

# Configure the logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log message format
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file
        logging.StreamHandler()  # Log to the console
    ]
)

# Create a logger
logger = logging.getLogger(__name__)

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[1]
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")

MODEL_DIR = PROJ_ROOT / "models"
DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# If tqdm is installed, configure logging with tqdm.write
try:
    from tqdm import tqdm

    # Remove existing handlers before adding new ones (compatible with logging)
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Add tqdm-compatible handler
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    handler.emit = lambda record: tqdm.write(handler.format(record), end="")

    logger.addHandler(handler)
    logger.info("TQDM logging setup complete.")
except ModuleNotFoundError:
    logger.warning("tqdm not installed, using default logging.")
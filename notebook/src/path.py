from pathlib import Path


FILE_PATH = Path(__file__)
SRC_PATH = FILE_PATH.parent
NOTEBOOK_PATH = SRC_PATH.parent
PROJECT_PATH = NOTEBOOK_PATH.parent

DATA_PATH = Path(PROJECT_PATH, "data")
OUTPUT_PATH = PROJECT_PATH / "output"

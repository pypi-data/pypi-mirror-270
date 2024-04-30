# Core Library modules
from pathlib import Path

# Third party modules
import chardet
import psutil

# Local modules
from .config import config


def determine_chunking(file_path: Path) -> bool:
    """Examine file size and file size to available memory ratio to determing if
    chunking is necessary
    """
    filesize = Path(file_path).stat().st_size
    filesize_mb = filesize / (1024 * 1024)
    mem = psutil.virtual_memory()
    memory_available = mem.available
    ratio = (filesize / memory_available) * 100
    if ratio > config.memory_threshold or filesize_mb > config.filesize_threshold:
        return True
    return False


def detect_encoding(file_path: Path) -> str:
    """Utility to detect the file encoding"""
    with open(file_path, "rb") as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
    return result["encoding"]


def is_binary(file_path: Path, num_bytes_to_check: int = 1024) -> bool:
    """Check if a file is binary by examining the first few bytes."""
    with open(file_path, "rb") as f:
        # Read the first few bytes
        data = f.read(num_bytes_to_check)
        # Check for null bytes or non-printable ASCII characters
        for byte in data:
            if byte == 0:  # Null byte
                return True
            elif byte < 32 and byte not in (
                9,
                10,
                13,
            ):  # Non-printable ASCII characters
                return True
    return False

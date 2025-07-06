from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True) # now this becomes entity
class DataIngestionConfig:
    """Data Ingestion Configuration."""
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
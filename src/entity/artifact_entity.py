from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    """
    Artifact for data ingestion.
    """
    trained_file_path: str
    test_file_path: str
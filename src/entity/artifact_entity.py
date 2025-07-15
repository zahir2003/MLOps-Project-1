from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    """
    Artifact for data ingestion.
    """
    trained_file_path: str
    test_file_path: str

@dataclass
class DataValidationArtifact:
    """
    Artifact for data validation.
    """
    validation_status: bool
    message: str
    validation_report_file_path: str
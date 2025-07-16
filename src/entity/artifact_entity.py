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

@dataclass
class DataTransformationArtifact:
    """
    Artifact for data transformation.
    """
    transformed_object_file_path: str
    transformed_train_file_path: str
    transformed_test_file_path: str

@dataclass
class ClassificationMetricArtifact:
    """
    Artifact for classification metrics.
    """
    def __init__(self, accuracy, f1_score, precision, recall):
        self.accuracy = accuracy
        self.f1_score = f1_score
        self.precision = precision
        self.recall = recall

@dataclass
class ModelTrainerArtifact:
    """
    Artifact for model training.
    """
    trained_model_file_path: str
    metric_artifact: ClassificationMetricArtifact
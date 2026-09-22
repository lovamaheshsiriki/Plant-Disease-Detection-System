from typing import List, Dict, Any, Optional

from pydantic import BaseModel


class Prediction(BaseModel):
    class_name: str
    confidence: float


class ImageResolution(BaseModel):
    width: int
    height: int


class ImageQuality(BaseModel):
    score: float
    status: str
    brightness: float
    sharpness: float
    resolution: ImageResolution
    warnings: List[str]


class DiseaseInformation(BaseModel):
    plant: str
    disease: str
    category: str
    description: str

    symptoms: List[str]

    management: List[str]

    prevention: List[str]


class PredictionResponse(BaseModel):

    predicted_class: str

    confidence: float

    predictions: List[Prediction]

    image_quality: ImageQuality

    disease_information: DiseaseInformation

    real_world_warning: Optional[str] = None
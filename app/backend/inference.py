from pathlib import Path
import sys

import cv2
import numpy as np
import torch
from PIL import Image
from torchvision import transforms


# ============================================================
# PROJECT ROOT
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# ============================================================
# PROJECT MODEL
# ============================================================

from src.models.cnn import PlantDiseaseCNN


# ============================================================
# CONFIGURATION
# ============================================================

from config import (
    MODEL_PATH,
    NUM_CLASSES,
    IMAGE_SIZE,
    IMAGENET_MEAN,
    IMAGENET_STD,
    CLASS_NAMES,
)


# ============================================================
# DEVICE
# ============================================================

DEVICE = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)


# ============================================================
# IMAGE TRANSFORMATION
# ============================================================

transform = transforms.Compose([
    transforms.Resize(
        (IMAGE_SIZE, IMAGE_SIZE)
    ),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=IMAGENET_MEAN,
        std=IMAGENET_STD
    ),
])


# ============================================================
# MODEL LOADING
# ============================================================

def load_model():

    if not MODEL_PATH.exists():

        raise FileNotFoundError(
            f"Model checkpoint not found:\n"
            f"{MODEL_PATH}"
        )

    model = PlantDiseaseCNN(
        num_classes=NUM_CLASSES
    )

    checkpoint = torch.load(
        MODEL_PATH,
        map_location=DEVICE,
        weights_only=False
    )

    model.load_state_dict(
        checkpoint["model_state_dict"]
    )

    model.to(DEVICE)

    model.eval()

    return model


model = load_model()


# ============================================================
# IMAGE QUALITY ANALYSIS
# ============================================================

def analyze_image_quality(
    image: Image.Image
):
    """
    Analyze basic image quality before inference.

    Checks:
    - resolution
    - brightness
    - blur

    Returns a quality score, status,
    and user-facing warnings.
    """

    warnings = []

    # --------------------------------------------------------
    # Convert to RGB
    # --------------------------------------------------------

    image = image.convert("RGB")

    width, height = image.size

    # --------------------------------------------------------
    # Resolution check
    # --------------------------------------------------------

    min_dimension = min(
        width,
        height
    )

    if min_dimension < 150:

        warnings.append(
            "Image resolution is very low. "
            "Use a higher-resolution photo."
        )

        resolution_score = 0.2

    elif min_dimension < 224:

        warnings.append(
            "Image resolution is relatively low."
        )

        resolution_score = 0.6

    else:

        resolution_score = 1.0

    # --------------------------------------------------------
    # Convert to NumPy
    # --------------------------------------------------------

    image_array = np.array(image)

    # --------------------------------------------------------
    # Brightness analysis
    # --------------------------------------------------------

    gray = cv2.cvtColor(
        image_array,
        cv2.COLOR_RGB2GRAY
    )

    brightness = float(
        np.mean(gray)
    )

    if brightness < 45:

        warnings.append(
            "Image appears too dark. "
            "Try taking the photo in better lighting."
        )

        brightness_score = 0.2

    elif brightness < 75:

        warnings.append(
            "Image is somewhat dark."
        )

        brightness_score = 0.6

    elif brightness > 220:

        warnings.append(
            "Image appears overexposed. "
            "Avoid very bright lighting."
        )

        brightness_score = 0.4

    elif brightness > 195:

        warnings.append(
            "Image is quite bright."
        )

        brightness_score = 0.7

    else:

        brightness_score = 1.0

    # --------------------------------------------------------
    # Blur detection
    # --------------------------------------------------------

    laplacian_variance = float(
        cv2.Laplacian(
            gray,
            cv2.CV_64F
        ).var()
    )

    if laplacian_variance < 50:

        warnings.append(
            "Image appears blurry. "
            "Try taking a sharper photo."
        )

        blur_score = 0.2

    elif laplacian_variance < 120:

        warnings.append(
            "Image may be slightly blurry."
        )

        blur_score = 0.6

    else:

        blur_score = 1.0

    # --------------------------------------------------------
    # Overall quality score
    # --------------------------------------------------------

    quality_score = (
        0.30 * resolution_score
        + 0.35 * brightness_score
        + 0.35 * blur_score
    )

    quality_score = round(
        quality_score,
        3
    )

    # --------------------------------------------------------
    # Quality status
    # --------------------------------------------------------

    if quality_score >= 0.75:

        status = "good"

    elif quality_score >= 0.50:

        status = "moderate"

    else:

        status = "poor"

    return {
        "score": quality_score,
        "status": status,
        "brightness": round(
            brightness,
            2
        ),
        "sharpness": round(
            laplacian_variance,
            2
        ),
        "resolution": {
            "width": width,
            "height": height
        },
        "warnings": warnings
    }


# ============================================================
# CONFIDENCE INTERPRETATION
# ============================================================

def interpret_confidence(
    confidence: float
):
    """
    Convert raw model confidence into
    a simple user-facing interpretation.
    """

    if confidence >= 0.80:

        return {
            "level": "high",
            "message": (
                "The model has high confidence "
                "in this prediction."
            )
        }

    elif confidence >= 0.50:

        return {
            "level": "moderate",
            "message": (
                "The model has moderate confidence. "
                "Consider uploading a clearer image "
                "for a stronger prediction."
            )
        }

    else:

        return {
            "level": "low",
            "message": (
                "The model has low confidence. "
                "Try uploading a clearer image "
                "with the leaf clearly visible."
            )
        }


# ============================================================
# PREDICTION
# ============================================================

def predict(
    image: Image.Image,
    top_k: int = 3
):

    # --------------------------------------------------------
    # Ensure RGB
    # --------------------------------------------------------

    image = image.convert("RGB")

    # --------------------------------------------------------
    # Analyze image quality
    # --------------------------------------------------------

    quality = analyze_image_quality(
        image
    )

    # --------------------------------------------------------
    # Transform image
    # --------------------------------------------------------

    image_tensor = transform(
        image
    )

    image_tensor = image_tensor.unsqueeze(
        0
    )

    image_tensor = image_tensor.to(
        DEVICE
    )

    # --------------------------------------------------------
    # Model inference
    # --------------------------------------------------------

    with torch.inference_mode():

        outputs = model(
            image_tensor
        )

        probabilities = torch.softmax(
            outputs,
            dim=1
        )

    # --------------------------------------------------------
    # Top-K predictions
    # --------------------------------------------------------

    top_k = min(
        top_k,
        NUM_CLASSES
    )

    top_probabilities, top_indices = (
        torch.topk(
            probabilities,
            k=top_k,
            dim=1
        )
    )

    predictions = []

    for probability, index in zip(
        top_probabilities[0],
        top_indices[0]
    ):

        class_index = index.item()

        confidence = probability.item()

        predictions.append({
            "class_name": CLASS_NAMES[
                class_index
            ],
            "confidence": round(
                confidence,
                4
            )
        })

    # --------------------------------------------------------
    # Primary prediction
    # --------------------------------------------------------

    predicted_class = (
        predictions[0]["class_name"]
    )

    confidence = (
        predictions[0]["confidence"]
    )

    # --------------------------------------------------------
    # Confidence interpretation
    # --------------------------------------------------------

    confidence_info = interpret_confidence(
        confidence
    )

    # --------------------------------------------------------
    # Final response
    # --------------------------------------------------------

    return {
        "predicted_class": predicted_class,

        "confidence": confidence,

        "confidence_level":
            confidence_info["level"],

        "confidence_message":
            confidence_info["message"],

        "predictions": predictions,

        "image_quality": quality,

        "real_world_warning": (
            "This is an AI-assisted prediction. "
            "The model was trained on controlled "
            "PlantVillage images, so performance "
            "may differ on real-world photographs."
        )
    }
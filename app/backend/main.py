from pathlib import Path
import io

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image

from inference import predict
from knowledge.plant_disease_info import get_disease_information


# ============================================================
# APPLICATION
# ============================================================

app = FastAPI(
    title="Plant Disease AI API",
    description="AI-powered plant disease detection API using a PyTorch CNN model.",
    version="4.0.0",
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://plant-disease-detection-system-seven.vercel.app"
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():
    return {
        "message": "Plant Disease AI API",
        "version": "4.0.0",
        "status": "running",
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Plant Disease AI API",
    }


# ============================================================
# PREDICTION
# ============================================================

@app.post("/predict")
async def predict_plant_disease(
    file: UploadFile = File(...)
):
    """
    Analyze an uploaded plant image.

    Returns:
    - predicted disease
    - confidence
    - top-3 predictions
    - confidence interpretation
    - image quality information
    - real-world warning
    """

    # --------------------------------------------------------
    # Validate file type
    # --------------------------------------------------------

    allowed_types = {
        "image/jpeg",
        "image/jpg",
        "image/png",
        "image/webp",
    }

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail=(
                "Unsupported image format. "
                "Please upload JPG, PNG, or WEBP."
            ),
        )

    # --------------------------------------------------------
    # Read image
    # --------------------------------------------------------

    try:

        contents = await file.read()

        if not contents:
            raise HTTPException(
                status_code=400,
                detail="Uploaded image is empty.",
            )

        image = Image.open(
            io.BytesIO(contents)
        ).convert("RGB")

    except HTTPException:
        raise

    except Exception as exc:

        raise HTTPException(
            status_code=400,
            detail=f"Unable to read image: {str(exc)}",
        )

    # --------------------------------------------------------
    # Run CNN inference
    # --------------------------------------------------------

    try:

        result = predict(
            image=image,
            top_k=3,
        )

    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(exc)}",
        )


    # --------------------------------------------------------
    # Add disease information
    # --------------------------------------------------------

    predicted_class = result.get("predicted_class")

    result["disease_information"] = get_disease_information(
        predicted_class
    )
    # --------------------------------------------------------
    # Add uploaded image information
    # --------------------------------------------------------

    result["image"] = {
        "filename": file.filename,
        "content_type": file.content_type,
    }

    # --------------------------------------------------------
    # V4 status
    # --------------------------------------------------------

    result["api_version"] = "4.0.0"

    return result


# ============================================================
# STARTUP MESSAGE
# ============================================================

@app.on_event("startup")
async def startup_event():

    print("=" * 70)
    print("PLANT DISEASE AI API")
    print("=" * 70)
    print("Version : 4.0.0")
    print("Status  : Ready")
    print("=" * 70)

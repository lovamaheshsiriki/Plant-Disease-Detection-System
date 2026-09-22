# 🌱 PlantAI — Plant Disease Detection System

PlantAI is an AI-powered plant disease detection application that analyzes a plant leaf image and predicts its disease using a Convolutional Neural Network (CNN).

The application combines a PyTorch deep-learning model with a FastAPI backend and React frontend to provide disease predictions along with useful plant information, symptoms, management guidance, and prevention recommendations.

## 🚀 Features

- 🌿 Plant disease classification
- 🤖 CNN-based image prediction
- 🎯 38 PlantVillage disease/healthy classes
- 📊 Top-3 predictions with confidence scores
- 🖼️ Image quality analysis
- 💡 AI-assisted disease explanation
- 🌱 Plant and disease information
- 🔍 Common symptoms
- 🩺 General disease-management guidance
- 🛡️ Prevention recommendations
- ⚠️ Real-world image limitation warning
- ⚡ FastAPI REST API
- 💻 React + Vite frontend

## 🧠 Machine Learning

**Dataset:** PlantVillage  
**Classes:** 38  
**Model:** Custom PyTorch CNN  
**Input:** 224 × 224 RGB image  
**Framework:** PyTorch

The model was trained using data augmentation, batch normalization, AdamW optimization, learning-rate scheduling, and early stopping.

The final trained model is stored as:

```text
models/baseline_cnn_best.pth


🏗️ Architecture
React + Vite
     │
     │ HTTP
     ▼
FastAPI Backend
     │
     ├── Image Validation
     ├── CNN Inference
     ├── Confidence Analysis
     ├── Image Quality Analysis
     └── Disease Knowledge Base
             │
             ▼
      Plant Disease Result
📁 Project Structure
plant-disease-cnn/
│
├── app/
│   ├── backend/
│   │   ├── main.py
│   │   ├── inference.py
│   │   └── knowledge/
│   │       └── plant_disease_info.py
│   │
│   └── frontend/
│
├── models/
│   └── baseline_cnn_best.pth
│
├── src/
│   ├── data/
│   ├── models/
│   ├── training/
│   ├── evaluation/
│   └── utils/
│
├── notebooks/
├── results/
├── requirements.txt
├── README.md
└── .gitignore
⚙️ Local Setup
Backend
cd app/backend
python -m uvicorn main:app --reload

Backend:

http://localhost:8000

API documentation:

http://localhost:8000/docs
Frontend
cd app/frontend
npm install
npm run dev

Frontend:

http://localhost:5173
🔌 API
POST /predict

Upload a plant image using multipart form-data.

The API returns:

predicted class
confidence
top-3 predictions
image quality information
disease explanation
plant information
symptoms
management recommendations
prevention recommendations
⚠️ Disclaimer

PlantAI provides AI-assisted predictions for educational and demonstration purposes.

The model was trained on controlled PlantVillage images, so performance may differ on real-world photographs. Disease-management information is general and should not replace guidance from qualified agricultural professionals or local agricultural authorities.

🛠️ Technologies
Python
PyTorch
Torchvision
FastAPI
React
Vite
JavaScript
HTML/CSS
PlantVillage
Hugging Face Datasets
👨‍💻 Author

Lova Mahesh Siriki

B.Tech — Computer Science & Engineering (Data Science)


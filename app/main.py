from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

app = FastAPI(title="AI Inference Service")

# Load a simple model (we'll create a dummy one)
model = None

class InputData(BaseModel):
    features: list[float]

@app.on_event("startup")
async def load_model():
    global model
    # Create a simple dummy model for demo
    from sklearn.linear_model import LogisticRegression
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y = np.array([0, 0, 1, 1])
    model = LogisticRegression().fit(X, y)
    joblib.dump(model, "model.joblib")
    print("Model loaded")

@app.get("/")
def home():
    return {"message": "AI Inference Service is running!"}

@app.post("/predict")
def predict(data: InputData):
    if model is None:
        return {"error": "Model not loaded"}
    prediction = model.predict([data.features])
    return {"prediction": int(prediction[0])}

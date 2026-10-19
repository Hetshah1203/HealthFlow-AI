from fastapi import FastAPI, UploadFile, File
from typing import List
import uvicorn

from .data import load_data, preprocess_data
from .model import train_model, predict

app = FastAPI(title="HealthFlow-AI API")

@app.post("/train")
async def train_endpoint(files: List[UploadFile] = File(...), model_type: str = "random_forest"):
    """Upload CSV/JSON files, train the selected model, and return a summary."""
    dfs = []
    for f in files:
        content = await f.read()
        df = load_data(content, f.filename)
        dfs.append(df)
    data = preprocess_data(dfs)
    model = train_model(data, model_type=model_type)
    return {"status": "trained", "model_type": model_type}

@app.post("/predict")
async def predict_endpoint(data: List[float]):
    """Provide a feature vector and receive a prediction."""
    pred = predict(data)
    return {"prediction": pred}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

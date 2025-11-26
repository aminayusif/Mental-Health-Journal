from .load_model import load_ml_components

model, vectorizer = load_ml_components()

def predict_sentiment(text):
    model, vectorizer = load_ml_components()

    if model is None or vectorizer is None:
        return "MODEL_NOT_READY"

    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]
    return prediction
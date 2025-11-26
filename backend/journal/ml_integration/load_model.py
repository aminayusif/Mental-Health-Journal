import os
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "..", "ml", "models", "best_model.pkl")
VEC_PATH = os.path.join(BASE_DIR, "..", "ml", "models", "vectorizer.pkl")

def load_ml_components():
    """Safely load model + vectorizer only if files exist."""
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VEC_PATH):
        return None, None  # <-- IMPORTANT SAFETY RETURN
    
    if os.path.getsize(MODEL_PATH) == 0 or os.path.getsize(VEC_PATH) == 0:
        return None, None

    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    with open(VEC_PATH, "rb") as f:
        vectorizer = pickle.load(f)

    return model, vectorizer

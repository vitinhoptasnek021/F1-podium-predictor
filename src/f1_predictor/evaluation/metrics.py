from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, brier_score_loss
)

def evaluate_binary_classifier(y_true, y_pred, y_probability):
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
        "brier": brier_score_loss(y_true, y_probability),
    }

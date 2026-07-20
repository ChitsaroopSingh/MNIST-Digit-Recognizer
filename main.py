import joblib
from draw import draw_digit

models = {
    "SGD" : joblib.load("models/sgd_model.joblib"),
    "Decision Tree" : joblib.load("models/dt_model.joblib"),
    "KNN" : joblib.load("models/knn_model.joblib"),
}

digit = draw_digit()

for name, model in models.items():
    prediction = model.predict(digit)[0]
    print(f"{name}: {prediction}")
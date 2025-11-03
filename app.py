from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        feature_names = [
            'danceability', 'energy', 'key', 'loudness', 'mode',
            'speechiness', 'acousticness', 'instrumentalness', 'liveness',
            'valence', 'tempo', 'duration_ms', 'time_signature'
        ]
        # Extract features from form in the fixed order
        features = [float(request.form[name]) for name in feature_names]

        final_input = np.array(features).reshape(1, -1)
        scaled = scaler.transform(final_input)
        output = int(model.predict(scaled)[0])
        
        result = "Popular 🎵" if output == 1 else "Not Popular 😔"
        return render_template("result.html", prediction=result)
    except Exception as e:
        return render_template("result.html", prediction=f"Error: {e}")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def get_risk_level(probability):
    if probability < 20:
        return "extremely low"
    elif probability < 40:
        return "low"
    elif probability < 60:
        return "medium"
    elif probability < 80:
        return "high"
    else:
        return "extremely high"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    probability = 10
    risk_level = get_risk_level(probability)
    return render_template('predict.html', risk_level=risk_level, probability=probability)


if __name__ == "__main__":
    app.run(debug=True)
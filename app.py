from flask import Flask, request, render_template
from activity_score import calculate_activity_score

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health", methods=["GET"])
def health():
    return {
        "status": "ok",
        "service": "activity-health-api"
    }

@app.route("/predict", methods=["POST"])
def predict():

    age = int(request.form["age"])
    gender = request.form["gender"]

    walking = float(request.form["walking"])
    running = float(request.form["running"])
    standing = float(request.form["standing"])
    sitting = float(request.form["sitting"])
    sleeping = float(request.form["sleeping"])

    score, grade, recommendation = calculate_activity_score(
        walking, running, standing, sitting, sleeping
    )

    return render_template(
        "index.html",
        score=f"{score:.2f}",
        grade=grade,
        recommendation=recommendation
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

@app.route("/api/predict", methods=["POST"])
def api_predict():

    data = request.get_json()

    walking = float(data["walking"])
    running = float(data["running"])
    standing = float(data["standing"])
    sitting = float(data["sitting"])
    sleeping = float(data["sleeping"])

    score, grade, recommendation = calculate_activity_score(
        walking, running, standing, sitting, sleeping
    )

    return {
        "activity_score": score,
        "grade": grade,
        "recommendation": recommendation
    }
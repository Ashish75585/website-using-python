from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Bengaluru, India",
        "salary": "Rs. 10,00,000"
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Noida, India",
        "salary": "Rs. 15,00,000"
    },
    {
        "id": 3,
        "title": "Frontend Developer",
        "location": "Deoria, India",
        "salary": "Rs. 12,00,000"
    },
    {
        "id": 4,
        "title": "Backend Developer",
        "location": "Gorakhpur, India",
        "salary": "Rs. 12,00,000"
    },
]


@app.route("/")  # this is called as decorator.
def home():
    return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
    return jsonify()


if __name__ == "__main__":
    app.run(debug=True)

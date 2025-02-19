from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

def get_weekday(birthdate: str) -> str:
    try:
        date_obj = datetime.strptime(birthdate, "%Y-%m-%d")
        return date_obj.strftime("%A")
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

@app.route("/", methods=["GET", "POST"])
def index():
    weekday = None
    if request.method == "POST":
        birthdate = request.form.get("birthdate")
        if birthdate:
            weekday = get_weekday(birthdate)
    return render_template("index.html", weekday=weekday)

if __name__ == "__main__":
    app.run(debug=True)

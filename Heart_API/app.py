from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Heart", methods=['GET', 'POST'])
def heart():
    if request.method == 'POST':
        # Generate a random percentage (between 0 and 100)
        prediction_percentage = random.randint(0, 100)
        # Render the result.html template with the generated percentage
        return render_template("result.html", prediction_percentage=prediction_percentage)
    return render_template("heart.html")

if __name__ == "__main__":
    app.run(debug=True)

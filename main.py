from flask import Flask, request, render_template
from comprehend import analyze_sentiment

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    if request.method == "POST":
        text = request.form["text"]
        sentiment = analyze_sentiment(text)
    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

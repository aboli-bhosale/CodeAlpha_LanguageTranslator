from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    if request.method == "POST":
        text = request.form["text"]
        src = request.form["source"]
        dest = request.form["target"]

        translated_text = GoogleTranslator(source=src, target=dest).translate(text)

    return render_template("index.html", output=translated_text)

if __name__ == "__main__":
    app.run(debug=True)

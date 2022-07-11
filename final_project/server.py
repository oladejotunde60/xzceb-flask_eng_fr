from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench", methods=['GET'])
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return render_template("index.html", textToTranslate=textToTranslate)

@app.route("/frenchToEnglish", methods=['GET'])
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return render_template("index.html", textToTranslate=textToTranslate)


@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

import os
import openai
import json
from flask import Flask, render_template, request
from transcriber import Transcriber
from dotenv import load_dotenv

load_dotenv()

openai.organization = "org-GWTlDTkGDJ1EuqobAkHvrPan"
openai.api_key = "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"
openai.Model.list()

app = Flask(__name__,template_folder="template")

print("hola")
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [
        {
            "role": "user",
            "content": "dame una lista de proyectos para crear con python"
        }
    ],
)
print(response)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/audio", methods=["POST"])
def audio():
    audio = request.files.get("audio")
    text = Transcriber().transcribe(audio)

    return {"result":"ok", "text":text}
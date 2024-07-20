from flask import Flask, jsonify
import random

app = Flask(__name__)

questions = [
    "What is your favorite color?",
    "What is the capital of France?",
    "Who wrote 'To Kill a Mockingbird'?",
    # Add more questions here
]

@app.route('/random_question')
def random_question():
    question = random.choice(questions)
    return jsonify(question=question)

def handler(event, context):
    return app(event, context)

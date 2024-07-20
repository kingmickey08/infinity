from flask import Flask, jsonify
import random

app = Flask(__name__)

questions = [
    "Komponen biotik dalam ekosistem terdiri dari ...",
    "Produsen dalam rantai makanan adalah ...",
    "Dalam ekosistem, aliran energi dimulai dari ...",
    "Ekosistem yang terbentuk akibat aktivitas manusia disebut ...",
    "Sebutkan contoh ekosistem darat!",
    "Konsumen tingkat pertama dalam rantai makanan adalah ...",
    "Pengurai memiliki peran penting dalam ekosistem karena ...",
    "Aliran energi dalam ekosistem umumnya digambarkan dalam bentuk ...",
    "Komponen abiotik yang mempengaruhi ekosistem termasuk ....",
    "Siklus nitrogen sangat penting dalam ekosistem karena ...",


    # Add more questions here
]

@app.route('/random_question')
def random_question():
    question = random.choice(questions)
    return jsonify(question=question)

def handler(event, context):
    return app(event, context)

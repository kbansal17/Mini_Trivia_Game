from flask import Flask, render_template, jsonify

app = Flask(__name__)

questions = [
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Madrid", "Paris"],
        "answer": "Paris"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Shakespeare", "Hemingway", "Tolkien", "Austen"],
        "answer": "Shakespeare"
    },
    {
        "question": "What gas do plants absorb?",
        "options": ["Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "Which ocean is the largest?",
        "options": ["Atlantic", "Pacific", "Arctic", "Indian"],
        "answer": "Pacific"
    },
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/questions")
def get_questions():
    return jsonify(questions)

if __name__ == "__main__":
    app.run(debug=True)

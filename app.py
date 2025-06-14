from flask import Flask, render_template, request, jsonify
from transformers import pipeline, set_seed

app = Flask(__name__)
chatbot = pipeline("text-generation", model="gpt2")
set_seed(42)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.json["msg"]
    response = chatbot(f"Human: {user_text}\nAI:", max_length=100, num_return_sequences=1)
    bot_reply = response[0]['generated_text'].split("AI:")[-1].strip().split("Human:")[0].strip()
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)

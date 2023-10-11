from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Web Application [3]" + "\n"

#flask를 5000번 포트로 실행
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
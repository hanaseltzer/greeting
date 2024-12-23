from flask import Flask

app = Flask(__name__)
@app.route('/health')
def health():
    return "Healthy", 200

@app.route('/')
def hello_world():
    return "GoodBye, World!", 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="80")
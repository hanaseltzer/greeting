from flask import Flask

app = Flask(__name__)

@app.route('/health')
def health_check():
    return "OK", 200

@app.route('/')
def hello_world():
    return "Hello, World!", 200

@app.route('/hello')
def hello():
    return "Hello, There!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80")
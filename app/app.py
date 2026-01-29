from flask import Flask

app = Flask(__name__)

@app.get('/')
def init():
    return "Vanakam da Maapla, Pipeline correct aa work aaguthu...."

if __name__ == "__main__":
    app.run('0.0.0.0',5000)

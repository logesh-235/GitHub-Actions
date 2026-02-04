from flask import Flask

app = Flask(__name__)

@app.get('/')
def init():
    return "Ashok intha Annamalaya ithuvaraikkum nanbana than pathu iruka"

if __name__ == "__main__":
    app.run('0.0.0.0',5000)
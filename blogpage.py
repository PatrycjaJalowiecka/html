from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/blog', methods=['GET'])
def blog_main():
    return f"This is a main blog page"

@app.route('/blog/<id>', methods=['GET'])
def blog(id):
    return f"This is blog entry #{id}"

blog(2)

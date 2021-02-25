from flask import Flask

app = Flask(__name__)

@app.route('/')
def blog_main():
    return f"This is a main blog page"

##@app.route('/hello')
##def hello():
  ##  my_name = "John"
    ##return f'Hello, {my_name}!'

@app.route('/blog', methods=['GET'])
def blog_main():
    return f"This is a main blog page"

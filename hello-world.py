from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/home/')
def hello_world(home):
    return 'Hello' + home


if __name__ =="__main__":
    app.run(host='0.0.0.0')


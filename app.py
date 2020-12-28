from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'Homepage'

@app.route('/onlyget', methods=['GET'])
def get_req():
  return 'You can only get this webpage.'

@app.route('/home/<string:name>')
def hello(name):
  return 'Hello, ' + name

if __name__ == "__main__":
  app.run(debug=True)

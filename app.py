from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/onlyget', methods=['GET'])
def get_req():
  return 'You can only get this webpage.'

@app.route('/home/<string:name>')
def hello(name):
  return 'Hello, ' + name

if __name__ == "__main__":
  app.run(debug=True)
